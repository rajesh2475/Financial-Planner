def calculate_tax(salary, deductions):
    # Max limits
    limits = {
        "sec80c": 150000,
        "nps": 50000,
        "sec80d": 75000,
        "home_loan": 200000,
        "standard": 50000,
    }

    # Cap deductions
    capped = {k: min(deductions.get(k, 0), limits.get(k, 999999)) for k in limits}
    total_deductions = sum(capped.values()) + deductions.get("hra", 0) + deductions.get("other", 0)

    # Old regime
    taxable_old = salary - total_deductions
    base_tax_old = slab_tax(taxable_old)
    total_tax_old = base_tax_old * 1.04

    # New regime
    taxable_new = salary - capped["standard"] + 25000
    base_tax_new = slab_tax_new(taxable_new)
    total_tax_new = base_tax_new * 1.04

    # Suggestions
    suggestions = []
    if deductions.get("sec80c", 0) < limits["sec80c"]:
        suggestions.append(f"Invest ₹{limits['sec80c'] - deductions['sec80c']} more in 80C (ELSS, PPF, EPF, LIC).")
    if deductions.get("nps", 0) < limits["nps"]:
        suggestions.append(f"Invest ₹{limits['nps'] - deductions['nps']} more in NPS (Tier I).")
    if deductions.get("sec80d", 0) < 25000:
        suggestions.append("Add health insurance premiums up to ₹25000.")
    if deductions.get("home_loan", 0) < limits["home_loan"]:
        suggestions.append("Home loan interest eligible up to ₹200000.")

    return {
        "salary": salary,
        "better": "New Regime" if total_tax_new < total_tax_old else "Old Regime",
        "savings": abs(total_tax_old - total_tax_new),
        "old": {
            "taxable_income": taxable_old,
            "base_tax": base_tax_old,
            "total_tax": total_tax_old,
            "deductions": total_deductions,
            "suggestions": suggestions,
            "invested_items": [k for k, v in deductions.items() if v > 0],
            "additional_savings": total_tax_old - total_tax_new if total_tax_old > total_tax_new else 0,
        },
        "new": {
            "taxable_income": taxable_new,
            "base_tax": base_tax_new,
            "total_tax": total_tax_new,
            "deductions": capped["standard"] + 25000,
        },
        "inputs_used": [k for k, v in deductions.items() if v > 0],
        "missing_inputs": [k for k in limits if deductions.get(k, 0) == 0],
        "max_savings": total_tax_old - total_tax_new if total_tax_old > total_tax_new else 0,
    }

def slab_tax(income):
    # Simplified old regime slabs
    if income <= 250000: return 0
    elif income <= 500000: return (income - 250000) * 0.05
    elif income <= 1000000: return 12500 + (income - 500000) * 0.2
    else: return 112500 + (income - 1000000) * 0.3

def slab_tax_new(income):
    # Simplified new regime slabs
    if income <= 300000: return 0
    elif income <= 600000: return (income - 300000) * 0.05
    elif income <= 900000: return 15000 + (income - 600000) * 0.1
    elif income <= 1200000: return 45000 + (income - 900000) * 0.15
    else: return 90000 + (income - 1200000) * 0.2
