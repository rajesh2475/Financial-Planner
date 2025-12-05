from flask import Blueprint, request, render_template
from app.utils.helpers import safe_float, safe_int

tax_full_bp = Blueprint("tax_full", __name__)

def compute_total_deductions(data):
    sections = [
        "life_insurance", "ulip", "elss", "tuition_fees", "epf_nps", "ppf", "ssy",
        "tax_saving_fd", "nsc", "home_loan_principal", "nps_80ccd_1b", "hra_80gg",
        "edu_loan_80e", "home_loan_interest_80eea", "health_self", "health_parents",
        "home_loan_interest_24b", "ev_interest_80eeb", "standard_deduction",
        "lta_10_5", "others"
    ]
    return sum(safe_float(data.get(field, 0)) for field in sections)

def calculate_tax_slabs(taxable_income, regime, age):
    slabs = []
    tax = 0

    if regime == "old":
        if age < 60:
            limits = [(250000, 0), (500000, 0.05), (1000000, 0.20)]
        else:
            limits = [(300000, 0), (500000, 0.05), (1000000, 0.20)]
        for i, (limit, rate) in enumerate(limits):
            prev_limit = limits[i - 1][0] if i > 0 else 0
            slab_value = min(taxable_income, limit) - prev_limit
            slab_value = max(slab_value, 0)
            slab_tax = slab_value * rate
            tax += slab_tax
            slabs.append({"range": f"{prev_limit+1} to {limit}", "rate": rate, "value": slab_value, "tax": slab_tax})
        if taxable_income > limits[-1][0]:
            slab_value = taxable_income - limits[-1][0]
            slab_tax = slab_value * 0.30
            tax += slab_tax
            slabs.append({"range": f"above {limits[-1][0]}", "rate": 0.30, "value": slab_value, "tax": slab_tax})

    elif regime == "new":
        limits = [(300000, 0), (600000, 0.05), (900000, 0.10), (1200000, 0.15), (1500000, 0.20)]
        for i, (limit, rate) in enumerate(limits):
            prev_limit = limits[i - 1][0] if i > 0 else 0
            slab_value = min(taxable_income, limit) - prev_limit
            slab_value = max(slab_value, 0)
            slab_tax = slab_value * rate
            tax += slab_tax
            slabs.append({"range": f"{prev_limit+1} to {limit}", "rate": rate, "value": slab_value, "tax": slab_tax})
        if taxable_income > limits[-1][0]:
            slab_value = taxable_income - limits[-1][0]
            slab_tax = slab_value * 0.30
            tax += slab_tax
            slabs.append({"range": f"above {limits[-1][0]}", "rate": 0.30, "value": slab_value, "tax": slab_tax})

    tax_with_cess = round(tax * 1.04, 2)
    return slabs, round(tax, 2), tax_with_cess

@tax_full_bp.route("/tax/full", methods=["GET", "POST"])
def full_tax_calculator():
    if request.method == "GET":
        form_data = {key: "" for key in [
            "income", "age", "life_insurance", "ulip", "elss", "tuition_fees", "epf_nps", "ppf", "ssy",
            "tax_saving_fd", "nsc", "home_loan_principal", "nps_80ccd_1b", "hra_80gg", "edu_loan_80e",
            "home_loan_interest_80eea", "health_self", "health_parents", "home_loan_interest_24b",
            "ev_interest_80eeb", "standard_deduction", "lta_10_5", "others"
        ]}
        return render_template("tax_full.html", form=form_data, result=None)

    form_data = {key: request.form.get(key, "0") for key in request.form}
    income = safe_float(form_data.get("income", 0))
    age = safe_int(form_data.get("age", 0))
    deductions = compute_total_deductions(form_data)
    taxable_old = max(0, income - deductions)
    taxable_new = max(0, income)  # no deductions in new regime

    old_slabs, old_tax, old_tax_with_cess = calculate_tax_slabs(taxable_old, "old", age)
    new_slabs, new_tax, new_tax_with_cess = calculate_tax_slabs(taxable_new, "new", age)

    result = {
        "deductions": round(deductions, 2),
        "taxable_old": taxable_old,
        "taxable_new": taxable_new,
        "old": {"slabs": old_slabs, "gross": old_tax, "cess": old_tax_with_cess},
        "new": {"slabs": new_slabs, "gross": new_tax, "cess": new_tax_with_cess}
    }

    return render_template("tax_full.html", form=form_data, result=result)
