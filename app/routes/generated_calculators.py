from flask import Blueprint, render_template, request, jsonify
from app.utils.helpers import safe_float, safe_int
from pathlib import Path

calc_bp = Blueprint("calculators", __name__)

# Auto-generated calculator routes

@calc_bp.route("/500-to-1-crore-building-calculator", methods=["GET", "POST"])
def _500_to_1_crore_building_calculator():
    """Calculator page for 500 to 1 crore building Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "500-to-1-crore-building-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("500-to-1-crore-building-calculator.html", form={}, result=None)

@calc_bp.route("/500-to-1-crore-building-calculator/api", methods=["POST"])
def _500_to_1_crore_building_calculator_api():
    """API endpoint for 500 to 1 crore building Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        age = safe_int(data.get("input_0") or 0)
        sip_investment = safe_float(data.get("input_1") or 0)
        invest_till_age = safe_int(data.get("input_2") or 0)
        expected_return = safe_float(data.get("input_3") or 0)
        lumpsum = safe_float(data.get("input_4") or 0)
        monthly = safe_float(data.get("input_5") or 0)

        years = invest_till_age - age
        n = years * 12
        r = expected_return / 100 / 12

        # Future value of SIP: FV = P * [((1+r)^n - 1)/r] * (1+r)
        fv_sip = monthly * (((1 + r) ** n - 1) / r) * (1 + r) if r > 0 and n > 0 else monthly * n
        # Future value of lumpsum: FV = P * (1+r)^n
        fv_lumpsum = lumpsum * ((1 + r) ** n) if r > 0 and n > 0 else lumpsum

        total_future_value = fv_sip + fv_lumpsum

        result = {
            "sip_investment": f"₹{sip_investment:,.0f}",
            "future_value_sip": f"₹{fv_sip:,.0f}",
            "future_value_lumpsum": f"₹{fv_lumpsum:,.0f}",
            "total_future_value": f"₹{total_future_value:,.0f}"
        }
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/ask-06th-feb-2026", methods=["GET", "POST"])
def ask_06th_feb_2026():
    """Calculator page for ASK 06th Feb 2026.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "ask-06th-feb-2026.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("ask-06th-feb-2026.html", form={}, result=None)

@calc_bp.route("/ask-06th-feb-2026/api", methods=["POST"])
def ask_06th_feb_2026_api():
    """API endpoint for ASK 06th Feb 2026.xlsx."""
    data = request.get_json() or {}
    try:
        nums = []
        for v in data.values():
            try:
                nums.append(safe_float(v))
            except Exception:
                continue

        if nums:
            summary = {
                "count": len(nums),
                "sum": round(sum(nums), 2),
                "avg": round(sum(nums) / len(nums), 2),
                "min": round(min(nums), 2),
                "max": round(max(nums), 2),
            }
        else:
            summary = {"count": 0}

        return jsonify({"success": True, "file": "ASK 06th Feb 2026.xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/ask-15th-march-2026-show", methods=["GET", "POST"])
def ask_15th_march_2026_show():
    """Calculator page for ASK 15TH MARCH 2026 show.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "ask-15th-march-2026-show.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("ask-15th-march-2026-show.html", form={}, result=None)

@calc_bp.route("/ask-15th-march-2026-show/api", methods=["POST"])
def ask_15th_march_2026_show_api():
    """API endpoint for ASK 15TH MARCH 2026 show.xlsx."""
    data = request.get_json() or {}
    try:
        nums = []
        for v in data.values():
            try:
                nums.append(safe_float(v))
            except Exception:
                continue
        if nums:
            summary = {"count": len(nums), "sum": round(sum(nums), 2), "avg": round(sum(nums) / len(nums), 2)}
        else:
            summary = {"count": 0}
        return jsonify({"success": True, "file": "ASK 15TH MARCH 2026 show.xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/ask", methods=["GET", "POST"])
def ask():
    """Calculator page for ASK.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "ask.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("ask.html", form={}, result=None)

@calc_bp.route("/ask/api", methods=["POST"])
def ask_api():
    """API endpoint for ASK.xlsx."""
    data = request.get_json() or {}
    try:
        nums = []
        for v in data.values():
            try:
                nums.append(safe_float(v))
            except Exception:
                continue
        summary = {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}
        return jsonify({"success": True, "file": "ASK.xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/annexure-february-2023", methods=["GET", "POST"])
def annexure_february_2023():
    """Calculator page for Annexure_February_2023.xls."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "annexure-february-2023.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("annexure-february-2023.html", form={}, result=None)

@calc_bp.route("/annexure-february-2023/api", methods=["POST"])
def annexure_february_2023_api():
    """API endpoint for Annexure_February_2023.xls."""
    data = request.get_json() or {}
    try:
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        summary = {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}
        return jsonify({"success": True, "file": "Annexure_February_2023.xls", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/askmoneypurse-272", methods=["GET", "POST"])
def askmoneypurse_272():
    """Calculator page for Askmoneypurse 272.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "askmoneypurse-272.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("askmoneypurse-272.html", form={}, result=None)

@calc_bp.route("/askmoneypurse-272/api", methods=["POST"])
def askmoneypurse_272_api():
    """API endpoint for Askmoneypurse 272.xlsx."""
    data = request.get_json() or {}
    try:
        nums = []
        for v in data.values():
            try:
                nums.append(safe_float(v))
            except Exception:
                continue
        return jsonify({"success": True, "file": "Askmoneypurse 272.xlsx", "result": {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/banking-funds-portfolio-overlap-data", methods=["GET", "POST"])
def banking_funds_portfolio_overlap_data():
    """Calculator page for Banking Funds Portfolio Overlap data.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "banking-funds-portfolio-overlap-data.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("banking-funds-portfolio-overlap-data.html", form={}, result=None)

@calc_bp.route("/banking-funds-portfolio-overlap-data/api", methods=["POST"])
def banking_funds_portfolio_overlap_data_api():
    """API endpoint for Banking Funds Portfolio Overlap data.xlsx."""
    data = request.get_json() or {}
    try:
        nums = []
        for k, v in data.items():
            try:
                nums.append(safe_float(v))
            except Exception:
                continue
        summary = {"count": len(nums), "total": round(sum(nums), 2) if nums else 0}
        return jsonify({"success": True, "file": "Banking Funds Portfolio Overlap data.xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/budget-2024-income-tax-calculation-sheet", methods=["GET", "POST"])
def budget_2024_income_tax_calculation_sheet():
    """Calculator page for Budget 2024 Income Tax Calculation Sheet.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "budget-2024-income-tax-calculation-sheet.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("budget-2024-income-tax-calculation-sheet.html", form={}, result=None)

@calc_bp.route("/budget-2024-income-tax-calculation-sheet/api", methods=["POST"])
def budget_2024_income_tax_calculation_sheet_api():
    """API endpoint for Budget 2024 Income Tax Calculation Sheet.xlsx."""
    data = request.get_json() or {}
    try:
        # If user provides income fields, compute a simplified tax estimate (10% of income)
        income = safe_float(data.get("income") or data.get("input_0") or 0)
        taxable = income
        tax = round(taxable * 0.10, 2)
        return jsonify({"success": True, "file": "Budget 2024 Income Tax Calculation Sheet.xlsx", "result": {"taxable_income": taxable, "tax_estimate": tax}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/cng-vs-ev-vs-petrol", methods=["GET", "POST"])
def cng_vs_ev_vs_petrol():
    """Calculator page for CNG VS EV VS PETROL.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "cng-vs-ev-vs-petrol.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("cng-vs-ev-vs-petrol.html", form={}, result=None)

@calc_bp.route("/cng-vs-ev-vs-petrol/api", methods=["POST"])
def cng_vs_ev_vs_petrol_api():
    """API endpoint for CNG VS EV VS PETROL.xlsx."""
    data = request.get_json() or {}
    try:
        # Compare running cost per km if provided
        cng = safe_float(data.get("cng_per_km") or data.get("input_0") or 0)
        ev = safe_float(data.get("ev_per_km") or data.get("input_1") or 0)
        petrol = safe_float(data.get("petrol_per_km") or data.get("input_2") or 0)
        costs = {"cng": cng, "ev": ev, "petrol": petrol}
        cheapest = None
        if any([cng, ev, petrol]):
            cheapest = min(costs, key=costs.get)
        return jsonify({"success": True, "file": "CNG VS EV VS PETROL.xlsx", "result": {"costs": costs, "cheapest": cheapest}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/car-purchase-vs-ride-hailing-apps", methods=["GET", "POST"])
def car_purchase_vs_ride_hailing_apps():
    """Calculator page for Car Purchase vs Ride Hailing Apps.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "car-purchase-vs-ride-hailing-apps.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("car-purchase-vs-ride-hailing-apps.html", form={}, result=None)

@calc_bp.route("/car-purchase-vs-ride-hailing-apps/api", methods=["POST"])
def car_purchase_vs_ride_hailing_apps_api():
    """API endpoint for Car Purchase vs Ride Hailing Apps.xlsx."""
    data = request.get_json() or {}
    try:
        owning_monthly = safe_float(data.get("owning_monthly") or data.get("input_0") or 0)
        rides_monthly = safe_float(data.get("rides_monthly") or data.get("input_1") or 0)
        recommendation = "own" if owning_monthly and owning_monthly < rides_monthly else "ride"
        return jsonify({"success": True, "file": "Car Purchase vs Ride Hailing Apps.xlsx", "result": {"owning_monthly": owning_monthly, "rides_monthly": rides_monthly, "recommendation": recommendation}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/checklist-for-health-insurance-selection", methods=["GET", "POST"])
def checklist_for_health_insurance_selection():
    """Calculator page for Checklist for Health Insurance Selection.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "checklist-for-health-insurance-selection.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("checklist-for-health-insurance-selection.html", form={}, result=None)

@calc_bp.route("/checklist-for-health-insurance-selection/api", methods=["POST"])
def checklist_for_health_insurance_selection_api():
    """API endpoint for Checklist for Health Insurance Selection.xlsx."""
    data = request.get_json() or {}
    return jsonify({
        "file": "Checklist for Health Insurance Selection.xlsx",
        "slug": "checklist-for-health-insurance-selection",
        "title": "Checklist For Health Insurance Selection",
        "status": "placeholder",
        "message": "Calculator API not yet implemented",
        "input_data": data
    })

@calc_bp.route("/credit-cards-data-2", methods=["GET", "POST"])
def credit_cards_data_2():
    """Calculator page for Credit cards data 2.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "credit-cards-data-2.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("credit-cards-data-2.html", form={}, result=None)

@calc_bp.route("/credit-cards-data-2/api", methods=["POST"])
def credit_cards_data_2_api():
    """API endpoint for Credit cards data 2.xlsx."""
    data = request.get_json() or {}
    try:
        # summarize any numeric card rewards/costs provided
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        summary = {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}
        return jsonify({"success": True, "file": "Credit cards data 2.xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/dcf-calculator", methods=["GET", "POST"])
def dcf_calculator():
    """Calculator page for DCF Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "dcf-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("dcf-calculator.html", form={}, result=None)

@calc_bp.route("/dcf-calculator/api", methods=["POST"])
def dcf_calculator_api():
    """API endpoint for DCF Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        # Basic DCF helper: if cashflows provided, compute simple NPV using discount rate
        cashflows = data.get("cashflows") or data.get("input_0") or []
        # Expect cashflows as comma-separated or list
        if isinstance(cashflows, str):
            parts = [p.strip() for p in cashflows.split(",") if p.strip()]
            cashflows = [safe_float(p) for p in parts]
        discount = safe_float(data.get("discount") or data.get("input_1") or 10) / 100
        npv = 0
        for i, cf in enumerate(cashflows, start=1):
            npv += cf / ((1 + discount) ** i)
        return jsonify({"success": True, "file": "DCF Calculator.xlsx", "result": {"npv": round(npv, 2), "cashflows_count": len(cashflows)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/dream-house-calculator", methods=["GET", "POST"])
def dream_house_calculator():
    """Calculator page for DREAM HOUSE CALCULATOR.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "dream-house-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("dream-house-calculator.html", form={}, result=None)

@calc_bp.route("/dream-house-calculator/api", methods=["POST"])
def dream_house_calculator_api():
    """API endpoint for DREAM HOUSE CALCULATOR.xlsx."""
    data = request.get_json() or {}
    try:
        price = safe_float(data.get("house_price") or data.get("input_0") or 0)
        downpayment_pct = safe_float(data.get("downpayment_pct") or data.get("input_1") or 20) / 100
        downpayment = round(price * downpayment_pct, 2)
        loan_needed = round(price - downpayment, 2)
        return jsonify({"success": True, "file": "DREAM HOUSE CALCULATOR.xlsx", "result": {"downpayment": downpayment, "loan_needed": loan_needed}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/defence-sector", methods=["GET", "POST"])
def defence_sector():
    """Calculator page for Defence Sector.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "defence-sector.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("defence-sector.html", form={}, result=None)

@calc_bp.route("/defence-sector/api", methods=["POST"])
def defence_sector_api():
    """API endpoint for Defence Sector.xlsx."""
    data = request.get_json() or {}
    try:
        # Simple summary of numeric values
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        return jsonify({"success": True, "file": "Defence Sector.xlsx", "result": {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/dream-house-with-etf-strategy", methods=["GET", "POST"])
def dream_house_with_etf_strategy():
    """Calculator page for Dream House With ETF Strategy.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "dream-house-with-etf-strategy.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("dream-house-with-etf-strategy.html", form={}, result=None)

@calc_bp.route("/dream-house-with-etf-strategy/api", methods=["POST"])
def dream_house_with_etf_strategy_api():
    """API endpoint for Dream House With ETF Strategy.xlsx."""
    data = request.get_json() or {}
    try:
        target = safe_float(data.get("target_amount") or data.get("input_0") or 0)
        years = safe_int(data.get("years") or data.get("input_1") or 5)
        annual_return = safe_float(data.get("annual_return") or data.get("input_2") or 8) / 100
        # Simplified required SIP to reach target: PMT formula
        r = annual_return / 12
        n = years * 12
        if r > 0:
            sip = target * r / (((1 + r) ** n) - 1)
        else:
            sip = target / n if n > 0 else 0
        return jsonify({"success": True, "file": "Dream House With ETF Strategy.xlsx", "result": {"monthly_sip": round(sip, 2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/dream-vehicle-eleigibility-calculator", methods=["GET", "POST"])
def dream_vehicle_eleigibility_calculator():
    """Calculator page for Dream Vehicle Eleigibility Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "dream-vehicle-eleigibility-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("dream-vehicle-eleigibility-calculator.html", form={}, result=None)

@calc_bp.route("/dream-vehicle-eleigibility-calculator/api", methods=["POST"])
def dream_vehicle_eleigibility_calculator_api():
    """API endpoint for Dream Vehicle Eleigibility Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        salary = safe_float(data.get("salary") or data.get("input_0") or 0)
        max_emi = salary * 0.5  # simplistic: up to 50% of salary
        return jsonify({"success": True, "file": "Dream Vehicle Eleigibility Calculator.xlsx", "result": {"max_emi": round(max_emi, 2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/ev-vs-petrol-claculator", methods=["GET", "POST"])
def ev_vs_petrol_claculator():
    """Calculator page for Ev vs Petrol Claculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "ev-vs-petrol-claculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("ev-vs-petrol-claculator.html", form={}, result=None)

@calc_bp.route("/ev-vs-petrol-claculator/api", methods=["POST"])
def ev_vs_petrol_claculator_api():
    """API endpoint for Ev vs Petrol Claculator.xlsx."""
    data = request.get_json() or {}
    try:
        ev_cost = safe_float(data.get("ev_per_km") or data.get("input_0") or 0)
        petrol_cost = safe_float(data.get("petrol_per_km") or data.get("input_1") or 0)
        cheaper = None
        if ev_cost and petrol_cost:
            cheaper = "ev" if ev_cost < petrol_cost else "petrol"
        return jsonify({"success": True, "file": "Ev vs Petrol Claculator.xlsx", "result": {"ev_per_km": ev_cost, "petrol_per_km": petrol_cost, "cheaper": cheaper}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/financial-planning", methods=["GET", "POST"])
def financial_planning():
    """Calculator page for FINANCIAL PLANNING.xls."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "financial-planning.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("financial-planning.html", form={}, result=None)

@calc_bp.route("/financial-planning/api", methods=["POST"])
def financial_planning_api():
    """API endpoint for FINANCIAL PLANNING.xls."""
    data = request.get_json() or {}
    try:
        # If user provides monthly_income and monthly_expenses, compute surplus
        income = safe_float(data.get("monthly_income") or data.get("income") or 0)
        expenses = safe_float(data.get("monthly_expenses") or data.get("expenses") or 0)
        surplus = round(income - expenses, 2)
        return jsonify({"success": True, "file": "FINANCIAL PLANNING.xls", "result": {"monthly_income": income, "monthly_expenses": expenses, "surplus": surplus}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/financial-safety-number-calculator", methods=["GET", "POST"])
def financial_safety_number_calculator():
    """Calculator page for FINANCIAL SAFETY NUMBER CALCULATOR.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "financial-safety-number-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("financial-safety-number-calculator.html", form={}, result=None)

@calc_bp.route("/financial-safety-number-calculator/api", methods=["POST"])
def financial_safety_number_calculator_api():
    """API endpoint for FINANCIAL SAFETY NUMBER CALCULATOR.xlsx."""
    data = request.get_json() or {}
    try:
        # Prefer the field mapped by the improved UI: `input_6` is PRESENT EXPENSES
        # Keep backwards compatibility by falling back to `monthly_expense` or `input_0`.
        monthly_expense = safe_float(
            data.get("monthly_expense") or data.get("input_6") or data.get("input_0") or 0
        )
        # safety number as 25x annual expense
        safety = round(monthly_expense * 12 * 25, 2)
        return jsonify({"success": True, "file": "FINANCIAL SAFETY NUMBER CALCULATOR.xlsx", "result": {"safety_number": safety}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/fire", methods=["GET", "POST"])
def fire():
    """Calculator page for FIRE.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "fire.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("fire.html", form={}, result=None)

@calc_bp.route("/fire/api", methods=["POST"])
def fire_api():
    """API endpoint for FIRE.xlsx."""
    data = request.get_json() or {}
    try:
        annual_expense = safe_float(data.get("annual_expense") or data.get("input_0") or 0)
        corpus = round(annual_expense * 25, 2)  # 25x rule
        return jsonify({"success": True, "file": "FIRE.xlsx", "result": {"required_corpus": corpus}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/fp-of-23rd-nov-2025", methods=["GET", "POST"])
def fp_of_23rd_nov_2025():
    """Calculator page for FP of 23rd Nov 2025.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "fp-of-23rd-nov-2025.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("fp-of-23rd-nov-2025.html", form={}, result=None)

@calc_bp.route("/fp-of-23rd-nov-2025/api", methods=["POST"])
def fp_of_23rd_nov_2025_api():
    """API endpoint for FP of 23rd Nov 2025.xlsx."""
    data = request.get_json() or {}
    try:
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        return jsonify({"success": True, "file": "FP of 23rd Nov 2025.xlsx", "result": {"count": len(nums), "sum": round(sum(nums),2) if nums else 0}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/fp-to-buy-house-2", methods=["GET", "POST"])
def fp_to_buy_house_2():
    """Calculator page for FP to buy House (2).xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "fp-to-buy-house-2.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("fp-to-buy-house-2.html", form={}, result=None)

@calc_bp.route("/fp-to-buy-house-2/api", methods=["POST"])
def fp_to_buy_house_2_api():
    """API endpoint for FP to buy House (2).xlsx."""
    data = request.get_json() or {}
    try:
        price = safe_float(data.get("house_price") or data.get("input_0") or 0)
        down_pct = safe_float(data.get("downpayment_pct") or data.get("input_1") or 20) / 100
        down = round(price * down_pct, 2)
        loan = round(price - down, 2)
        return jsonify({"success": True, "file": "FP to buy House (2).xlsx", "result": {"downpayment": down, "loan": loan}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/fp-to-buy-house", methods=["GET", "POST"])
def fp_to_buy_house():
    """Calculator page for FP to buy House.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "fp-to-buy-house.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("fp-to-buy-house.html", form={}, result=None)

@calc_bp.route("/fp-to-buy-house/api", methods=["POST"])
def fp_to_buy_house_api():
    """API endpoint for FP to buy House.xlsx."""
    data = request.get_json() or {}
    try:
        price = safe_float(data.get("house_price") or data.get("input_0") or 0)
        down_pct = safe_float(data.get("downpayment_pct") or data.get("input_1") or 20) / 100
        down = round(price * down_pct, 2)
        loan = round(price - down, 2)
        return jsonify({"success": True, "file": "FP to buy House.xlsx", "result": {"downpayment": down, "loan": loan}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/fixed-returncalc", methods=["GET", "POST"])
def fixed_returncalc():
    """Calculator page for Fixed ReturnCALC.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "fixed-returncalc.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("fixed-returncalc.html", form={}, result=None)

@calc_bp.route("/fixed-returncalc/api", methods=["POST"])
def fixed_returncalc_api():
    """API endpoint for Fixed ReturnCALC.xlsx."""
    data = request.get_json() or {}
    return jsonify({
        "file": "Fixed ReturnCALC.xlsx",
        "slug": "fixed-returncalc",
        "title": "Fixed Returncalc",
        "status": "placeholder",
        "message": "Calculator API not yet implemented",
        "input_data": data
    })

@calc_bp.route("/home-loan-repayment-final", methods=["GET", "POST"])
def home_loan_repayment_final():
    """Calculator page for HOME LOAN REPAYMENT FINAL.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "home-loan-repayment-final.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("home-loan-repayment-final.html", form={}, result=None)

@calc_bp.route("/home-loan-repayment-final/api", methods=["POST"])
def home_loan_repayment_final_api():
    """API endpoint for HOME LOAN REPAYMENT FINAL.xlsx."""
    data = request.get_json() or {}
    try:
        principal = safe_float(data.get("principal") or data.get("input_0") or 0)
        annual_rate = safe_float(data.get("annual_rate") or data.get("input_1") or 7) / 100
        years = safe_int(data.get("years") or data.get("input_2") or 20)
        n = years * 12
        r = annual_rate / 12
        if r > 0 and n > 0:
            emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        else:
            emi = principal / n if n > 0 else 0
        total_payment = emi * n
        return jsonify({"success": True, "file": "HOME LOAN REPAYMENT FINAL.xlsx", "result": {"emi": round(emi, 2), "total_payment": round(total_payment, 2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/health-insurance-edited-aa-1", methods=["GET", "POST"])
def health_insurance_edited_aa_1():
    """Calculator page for Health Insurance edited aa  (1).xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "health-insurance-edited-aa-1.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("health-insurance-edited-aa-1.html", form={}, result=None)

@calc_bp.route("/health-insurance-edited-aa-1/api", methods=["POST"])
def health_insurance_edited_aa_1_api():
    """API endpoint for Health Insurance edited aa  (1).xlsx."""
    data = request.get_json() or {}
    try:
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        summary = {"count": len(nums), "sum": round(sum(nums), 2) if nums else 0}
        return jsonify({"success": True, "file": "Health Insurance edited aa  (1).xlsx", "result": summary, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/home-loan-calculator", methods=["GET", "POST"])
def home_loan_calculator():
    """Calculator page for Home Loan Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "home-loan-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("home-loan-calculator.html", form={}, result=None)

@calc_bp.route("/home-loan-calculator/api", methods=["POST"])
def home_loan_calculator_api():
    """API endpoint for Home Loan Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        principal = safe_float(data.get("principal") or data.get("loan_amount") or data.get("input_0") or 0)
        annual_rate = safe_float(data.get("annual_rate") or data.get("interest_rate") or data.get("input_1") or 7) / 100
        years = safe_int(data.get("tenure_years") or data.get("input_2") or 20)
        n = years * 12
        r = annual_rate / 12
        if r > 0 and n > 0:
            emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        else:
            emi = principal / n if n > 0 else 0
        total_payment = emi * n
        return jsonify({"success": True, "file": "Home Loan Calculator.xlsx", "result": {"emi": round(emi, 2), "total_payment": round(total_payment, 2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/home-loan-emi", methods=["GET", "POST"])
def home_loan_emi():
    """Calculator page for Home Loan EMI.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "home-loan-emi.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("home-loan-emi.html", form={}, result=None)

@calc_bp.route("/home-loan-emi/api", methods=["POST"])
def home_loan_emi_api():
    """API endpoint for Home Loan EMI.xlsx."""
    data = request.get_json() or {}
    try:
        principal = safe_float(data.get("principal") or data.get("input_0") or 0)
        annual_rate = safe_float(data.get("annual_rate") or data.get("input_1") or 7) / 100
        years = safe_int(data.get("years") or data.get("input_2") or 20)
        n = years * 12
        r = annual_rate / 12
        if r > 0 and n > 0:
            emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
        else:
            emi = principal / n if n > 0 else 0
        return jsonify({"success": True, "file": "Home Loan EMI.xlsx", "result": {"emi": round(emi, 2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/home-loan-transfer-calculator-2", methods=["GET", "POST"])
def home_loan_transfer_calculator_2():
    """Calculator page for Home Loan Transfer Calculator (2).xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "home-loan-transfer-calculator-2.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("home-loan-transfer-calculator-2.html", form={}, result=None)

@calc_bp.route("/home-loan-transfer-calculator-2/api", methods=["POST"])
def home_loan_transfer_calculator_2_api():
    """API endpoint for Home Loan Transfer Calculator (2).xlsx."""
    data = request.get_json() or {}
    try:
        # Provide simple comparison between current emi and new emi given new rate
        principal = safe_float(data.get("principal") or data.get("input_0") or 0)
        current_rate = safe_float(data.get("current_rate") or data.get("input_1") or 7) / 100
        new_rate = safe_float(data.get("new_rate") or data.get("input_2") or 6) / 100
        years_remaining = safe_int(data.get("years_remaining") or data.get("input_3") or 10)
        def calc_emi(p, annual_r, yrs):
            rn = annual_r / 12
            nn = yrs * 12
            return p * rn * (1 + rn) ** nn / ((1 + rn) ** nn - 1) if rn > 0 and nn>0 else p/nn if nn>0 else 0
        current_emi = calc_emi(principal, current_rate, years_remaining)
        new_emi = calc_emi(principal, new_rate, years_remaining)
        return jsonify({"success": True, "file": "Home Loan Transfer Calculator (2).xlsx", "result": {"current_emi": round(current_emi,2), "new_emi": round(new_emi,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/home-loan-transfer-calculator", methods=["GET", "POST"])
def home_loan_transfer_calculator():
    """Calculator page for Home Loan Transfer Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "home-loan-transfer-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("home-loan-transfer-calculator.html", form={}, result=None)

@calc_bp.route("/home-loan-transfer-calculator/api", methods=["POST"])
def home_loan_transfer_calculator_api():
    """API endpoint for Home Loan Transfer Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        principal = safe_float(data.get("principal") or data.get("input_0") or 0)
        current_rate = safe_float(data.get("current_rate") or data.get("input_1") or 7) / 100
        new_rate = safe_float(data.get("new_rate") or data.get("input_2") or 6) / 100
        years_remaining = safe_int(data.get("years_remaining") or data.get("input_3") or 10)
        def calc_emi(p, annual_r, yrs):
            rn = annual_r / 12
            nn = yrs * 12
            return p * rn * (1 + rn) ** nn / ((1 + rn) ** nn - 1) if rn > 0 and nn>0 else p/nn if nn>0 else 0
        current_emi = calc_emi(principal, current_rate, years_remaining)
        new_emi = calc_emi(principal, new_rate, years_remaining)
        return jsonify({"success": True, "file": "Home Loan Transfer Calculator.xlsx", "result": {"current_emi": round(current_emi,2), "new_emi": round(new_emi,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/house-flat-purchase-eligibility-calculator", methods=["GET", "POST"])
def house_flat_purchase_eligibility_calculator():
    """Calculator page for House_Flat Purchase Eligibility Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "house-flat-purchase-eligibility-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("house-flat-purchase-eligibility-calculator.html", form={}, result=None)

@calc_bp.route("/house-flat-purchase-eligibility-calculator/api", methods=["POST"])
def house_flat_purchase_eligibility_calculator_api():
    """API endpoint for House_Flat Purchase Eligibility Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        salary = safe_float(data.get("salary") or data.get("input_0") or 0)
        # simple rule: eligibility = annual_salary * 5
        eligibility = round(salary * 12 * 5, 2)
        return jsonify({"success": True, "file": "House_Flat Purchase Eligibility Calculator.xlsx", "result": {"eligibility": eligibility}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/income-tax-calculator-2023", methods=["GET", "POST"])
def income_tax_calculator_2023():
    """Calculator page for Income Tax Calculator 2023.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "income-tax-calculator-2023.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("income-tax-calculator-2023.html", form={}, result=None)

@calc_bp.route("/income-tax-calculator-2023/api", methods=["POST"])
def income_tax_calculator_2023_api():
    """API endpoint for Income Tax Calculator 2023.xlsx."""
    data = request.get_json() or {}
    try:
        income = safe_float(data.get("annual_income") or data.get("income") or 0)
        # simplified tax estimate: 10% of income
        tax = round(income * 0.10, 2)
        return jsonify({"success": True, "file": "Income Tax Calculator 2023.xlsx", "result": {"annual_income": income, "tax_estimate": tax}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/incremental-investment-calculator", methods=["GET", "POST"])
def incremental_investment_calculator():
    """Calculator page for Incremental Investment Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "incremental-investment-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("incremental-investment-calculator.html", form={}, result=None)

@calc_bp.route("/incremental-investment-calculator/api", methods=["POST"])
def incremental_investment_calculator_api():
    """API endpoint for Incremental Investment Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        monthly = safe_float(data.get("monthly") or data.get("input_0") or 0)
        years = safe_int(data.get("years") or data.get("input_1") or 0)
        annual_return = safe_float(data.get("annual_return") or data.get("input_2") or 8) / 100
        n = years * 12
        r = annual_return / 12
        fv = 0
        if r > 0 and n > 0:
            fv = monthly * (((1 + r) ** n - 1) / r) * (1 + r)
        else:
            fv = monthly * n
        return jsonify({"success": True, "file": "Incremental Investment Calculator.xlsx", "result": {"future_value": round(fv,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/incremental-sip-calculator", methods=["GET", "POST"])
def incremental_sip_calculator():
    """Calculator page for Incremental SIP Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "incremental-sip-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("incremental-sip-calculator.html", form={}, result=None)

@calc_bp.route("/incremental-sip-calculator/api", methods=["POST"])
def incremental_sip_calculator_api():
    """API endpoint for Incremental SIP Calculator.xlsx.

    This endpoint accepts both JSON (application/json) and form-encoded POSTs.
    - For JSON requests it returns a JSON response with calculation results.
    - For regular form POSTs it renders the page with results (backwards compatible).
    The actual calculation is delegated to the stepup_sip_schedule helper in
    `app.routes.spi` (reused to avoid duplicating logic).
    """
    # import locally to avoid circular imports at module load time
    from app.routes.spi import stepup_sip_schedule

    # Accept JSON or form data
    try:
        if request.is_json:
            data = request.get_json() or {}
            # map incoming names to same variables used by stepup_sip_schedule
            planned_monthly_investment = safe_float(data.get("input_2") or data.get("plannedMonthlyInvestment") or 0)
            years_of_investment = int(data.get("input_3") or data.get("yearsOfInvestment") or 0)
            annual_return = safe_float(data.get("input_4") or data.get("annualReturn") or 0) / 100.0
            mode = data.get("mode") or "percent"
            increment_raw = safe_float(data.get("input_5") or data.get("incrementValue") or 0)
            # when mode is percent the client typically sends a percentage (e.g. 10 for 10%)
            increment_value = (increment_raw / 100.0) if mode == "percent" else increment_raw
            holding_years = int(data.get("holdingYears") or 0)

            # basic validations
            if planned_monthly_investment < 0 or years_of_investment < 0 or annual_return < 0:
                return jsonify({"success": False, "error": "Inputs must be non-negative"}), 400
            if mode == "percent" and increment_value < -1:
                return jsonify({"success": False, "error": "Percent increment cannot be less than -100%"}), 400

            result = stepup_sip_schedule(
                planned_monthly_investment=planned_monthly_investment,
                years_of_investment=years_of_investment,
                annual_return=annual_return,
                increment_value=increment_value,
                mode=mode,
                holding_years=holding_years,
            )

            # format summary numbers for JSON response
            summary = result.get("summary", {})
            formatted_summary = {
                "final_value": f"₹{summary.get('final_value', 0):,.2f}",
                "total_invested": f"₹{summary.get('total_invested', 0):,.2f}",
                "gain": f"₹{summary.get('gain', 0):,.2f}",
            }

            return jsonify({"success": True, "summary": formatted_summary, "schedule": result.get("schedule", [])})

        # Fallback: handle traditional form POST (render page)
        form_data = dict(request.form)
        planned_monthly_investment = safe_float(request.form.get("plannedMonthlyInvestment") or request.form.get("input_2") or 0)
        years_of_investment = int(request.form.get("yearsOfInvestment") or request.form.get("input_3") or 0)
        annual_return = safe_float(request.form.get("annualReturn") or request.form.get("input_4") or 0) / 100.0
        mode = request.form.get("mode") or "percent"
        increment_value = safe_float(request.form.get("incrementValue") or request.form.get("input_5") or 0) / 100.0 if mode == "percent" else safe_float(request.form.get("incrementValue") or request.form.get("input_5") or 0)
        holding_years = int(request.form.get("holdingYears") or 0)

        # basic validations
        if planned_monthly_investment < 0 or years_of_investment < 0 or annual_return < 0:
            return render_template("incremental-sip-calculator.html", form=form_data, result=None, error="Inputs must be non-negative")

        result = stepup_sip_schedule(
            planned_monthly_investment=planned_monthly_investment,
            years_of_investment=years_of_investment,
            annual_return=annual_return,
            increment_value=increment_value,
            mode=mode,
            holding_years=holding_years,
        )

        # prepare display-friendly form
        display_form = {
            "input_2": planned_monthly_investment,
            "input_3": years_of_investment,
            "input_4": annual_return * 100,
            "input_5": (increment_value * 100) if mode == "percent" else increment_value,
            "mode": mode,
            "holdingYears": holding_years,
        }

        return render_template("incremental-sip-calculator.html", form=display_form, result=result)

    except (TypeError, ValueError) as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/kids-investment-calculator", methods=["GET", "POST"])
def kids_investment_calculator():
    """Calculator page for Kids Investment Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "kids-investment-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("kids-investment-calculator.html", form={}, result=None)

@calc_bp.route("/kids-investment-calculator/api", methods=["POST"])
def kids_investment_calculator_api():
    """API endpoint for Kids Investment Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        monthly = safe_float(data.get("monthly") or data.get("input_0") or 0)
        years = safe_int(data.get("years") or data.get("input_1") or 10)
        annual_return = safe_float(data.get("annual_return") or data.get("input_2") or 8) / 100
        n = years * 12
        r = annual_return / 12
        fv = monthly * (((1 + r) ** n - 1) / r) * (1 + r) if r > 0 and n > 0 else monthly * n
        return jsonify({"success": True, "file": "Kids Investment Calculator.xlsx", "result": {"future_value": round(fv,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/monthly-budget-planning-3", methods=["GET", "POST"])
def monthly_budget_planning_3():
    """Calculator page for Monthly Budget Planning (3).xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "monthly-budget-planning-3.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("monthly-budget-planning-3.html", form={}, result=None)

@calc_bp.route("/monthly-budget-planning-3/api", methods=["POST"])
def monthly_budget_planning_3_api():
    """API endpoint for Monthly Budget Planning (3).xlsx."""
    data = request.get_json() or {}
    try:
        income = safe_float(data.get("income") or data.get("monthly_income") or 0)
        essentials = safe_float(data.get("essentials") or data.get("input_0") or 0)
        savings = round(income - essentials, 2)
        return jsonify({"success": True, "file": "Monthly Budget Planning (3).xlsx", "result": {"savings": savings}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/monthly-budget-planning", methods=["GET", "POST"])
def monthly_budget_planning():
    """Calculator page for Monthly Budget Planning.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "monthly-budget-planning.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("monthly-budget-planning.html", form={}, result=None)

@calc_bp.route("/monthly-budget-planning/api", methods=["POST"])
def monthly_budget_planning_api():
    """API endpoint for Monthly Budget Planning.xlsx."""
    data = request.get_json() or {}
    try:
        income = safe_float(data.get("income") or data.get("monthly_income") or 0)
        total_expenses = sum([safe_float(v) for k, v in data.items() if k.startswith("expense_")])
        savings = round(income - total_expenses, 2)
        return jsonify({"success": True, "file": "Monthly Budget Planning.xlsx", "result": {"savings": savings, "total_expenses": round(total_expenses,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/my-family-financial-tracker", methods=["GET", "POST"])
def my_family_financial_tracker():
    """Calculator page for My Family Financial Tracker.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "my-family-financial-tracker.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("my-family-financial-tracker.html", form={}, result=None)

@calc_bp.route("/my-family-financial-tracker/api", methods=["POST"])
def my_family_financial_tracker_api():
    """API endpoint for My Family Financial Tracker.xlsx."""
    data = request.get_json() or {}
    try:
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        return jsonify({"success": True, "file": "My Family Financial Tracker.xlsx", "result": {"count": len(nums), "sum": round(sum(nums),2) if nums else 0}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/networth", methods=["GET", "POST"])
def networth():
    """Calculator page for NETWORTH.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "networth.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("networth.html", form={}, result=None)

@calc_bp.route("/networth/api", methods=["POST"])
def networth_api():
    """API endpoint for NETWORTH.xlsx."""
    data = request.get_json() or {}
    try:
        assets = sum([safe_float(v) for k, v in data.items() if k.startswith("asset_")])
        liabilities = sum([safe_float(v) for k, v in data.items() if k.startswith("liability_")])
        net = round(assets - liabilities, 2)
        return jsonify({"success": True, "file": "NETWORTH.xlsx", "result": {"assets": round(assets,2), "liabilities": round(liabilities,2), "networth": net}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/new-home-loan-repayment-final", methods=["GET", "POST"])
def new_home_loan_repayment_final():
    """Calculator page for NEW HOME LOAN REPAYMENT FINAL.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "new-home-loan-repayment-final.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("new-home-loan-repayment-final.html", form={}, result=None)

@calc_bp.route("/new-home-loan-repayment-final/api", methods=["POST"])
def new_home_loan_repayment_final_api():
    """API endpoint for NEW HOME LOAN REPAYMENT FINAL.xlsx."""
    data = request.get_json() or {}
    try:
        principal = safe_float(data.get("principal") or data.get("input_0") or 0)
        rate = safe_float(data.get("annual_rate") or data.get("input_1") or 7) / 100
        years = safe_int(data.get("years") or data.get("input_2") or 20)
        n = years * 12
        r = rate / 12
        emi = principal * r * (1 + r) ** n / ((1 + r) ** n - 1) if r > 0 and n>0 else principal / n if n>0 else 0
        return jsonify({"success": True, "file": "NEW HOME LOAN REPAYMENT FINAL.xlsx", "result": {"emi": round(emi,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/nps-vatsalya", methods=["GET", "POST"])
def nps_vatsalya():
    """Calculator page for NPS VATSALYA.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "nps-vatsalya.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("nps-vatsalya.html", form={}, result=None)

@calc_bp.route("/nps-vatsalya/api", methods=["POST"])
def nps_vatsalya_api():
    """API endpoint for NPS VATSALYA.xlsx."""
    data = request.get_json() or {}
    try:
        nums = [safe_float(v) for v in data.values() if str(v).strip() != ""]
        return jsonify({"success": True, "file": "NPS VATSALYA.xlsx", "result": {"count": len(nums), "sum": round(sum(nums),2) if nums else 0}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/property-tax-calculator", methods=["GET", "POST"])
def property_tax_calculator():
    """Calculator page for PROPERTY TAX CALCULATOR.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "property-tax-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("property-tax-calculator.html", form={}, result=None)

@calc_bp.route("/property-tax-calculator/api", methods=["POST"])
def property_tax_calculator_api():
    """API endpoint for PROPERTY TAX CALCULATOR.xlsx."""
    data = request.get_json() or {}
    try:
        property_value = safe_float(data.get("property_value") or data.get("input_0") or 0)
        tax_rate = safe_float(data.get("tax_rate") or data.get("input_1") or 0.2) / 100
        tax = round(property_value * tax_rate, 2)
        return jsonify({"success": True, "file": "PROPERTY TAX CALCULATOR.xlsx", "result": {"tax": tax}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/rental-yield-calculator", methods=["GET", "POST"])
def rental_yield_calculator():
    """Calculator page for Rental Yield Calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "rental-yield-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("rental-yield-calculator.html", form={}, result=None)

@calc_bp.route("/rental-yield-calculator/api", methods=["POST"])
def rental_yield_calculator_api():
    """API endpoint for Rental Yield Calculator.xlsx."""
    data = request.get_json() or {}
    try:
        annual_rent = safe_float(data.get("annual_rent") or data.get("input_0") or 0)
        property_value = safe_float(data.get("property_value") or data.get("input_1") or 0)
        yield_pct = round((annual_rent / property_value) * 100, 2) if property_value else 0
        return jsonify({"success": True, "file": "Rental Yield Calculator.xlsx", "result": {"rental_yield_pct": yield_pct}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/tax-saver-work-sheet", methods=["GET", "POST"])
def tax_saver_work_sheet():
    """Calculator page for TAX SAVER Work Sheet.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "tax-saver-work-sheet.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("tax-saver-work-sheet.html", form={}, result=None)

@calc_bp.route("/tax-saver-work-sheet/api", methods=["POST"])
def tax_saver_work_sheet_api():
    """API endpoint for TAX SAVER Work Sheet.xlsx."""
    data = request.get_json() or {}
    try:
        investments = sum([safe_float(v) for k, v in data.items() if k.startswith("inv_")])
        return jsonify({"success": True, "file": "TAX SAVER Work Sheet.xlsx", "result": {"total_investments": round(investments,2)}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/tax-cal-with-new-income-tax-act-2025", methods=["GET", "POST"])
def tax_cal_with_new_income_tax_act_2025():
    """Calculator page for Tax Cal with New Income Tax Act 2025.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "tax-cal-with-new-income-tax-act-2025.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("tax-cal-with-new-income-tax-act-2025.html", form={}, result=None)

@calc_bp.route("/tax-cal-with-new-income-tax-act-2025/api", methods=["POST"])
def tax_cal_with_new_income_tax_act_2025_api():
    """API endpoint for Tax Cal with New Income Tax Act 2025.xlsx."""
    data = request.get_json() or {}
    try:
        income = safe_float(data.get("annual_income") or data.get("income") or 0)
        tax = round(income * 0.10, 2)
        return jsonify({"success": True, "file": "Tax Cal with New Income Tax Act 2025.xlsx", "result": {"tax_estimate": tax}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/tax-calculator", methods=["GET", "POST"])
def tax_calculator():
    """Calculator page for Tax calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "tax-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("tax-calculator.html", form={}, result=None)

@calc_bp.route("/tax-calculator/api", methods=["POST"])
def tax_calculator_api():
    """API endpoint for Tax calculator.xlsx."""
    data = request.get_json() or {}
    try:
        income = safe_float(data.get("annual_income") or data.get("income") or 0)
        tax = round(income * 0.10, 2)
        return jsonify({"success": True, "file": "Tax calculator.xlsx", "result": {"tax_estimate": tax}, "input_data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@calc_bp.route("/retire-calculator", methods=["GET", "POST"])
def retire_calculator():
    """Calculator page for retire calculator.xlsx."""
    if request.method == "POST":
        # Placeholder for form data processing
        form_data = dict(request.form)
        return render_template(
            "retire-calculator.html",
            form=form_data,
            result=None,
            error="Calculator logic not yet implemented"
        )
    
    return render_template("retire-calculator.html", form={}, result=None)

@calc_bp.route("/retire-calculator/api", methods=["POST"])
def retire_calculator_api():
    """API endpoint for retire calculator.xlsx."""
    data = request.get_json() or {}
    try:
        # Parse inputs
        current_age = safe_int(data.get("input_0") or 0)
        retirement_age = safe_int(data.get("input_1") or 0)
        current_expense = safe_float(data.get("input_2") or 0)
        inflation = safe_float(data.get("input_3") or 0)
        # Remove input_4 (monthly expense at age 55) as input
        # Remove input_5, input_6 as user inputs
        # Use fixed values for returns (or set defaults)
        return_on_corpus = 12.0
        return_on_investment = 12.0

        # Calculate years to retirement
        years_to_retirement = retirement_age - current_age
        if years_to_retirement < 0:
            return jsonify({"success": False, "error": "Retirement age must be greater than current age."}), 400

        # Calculate monthly expense at retirement age
        expense_at_retirement = current_expense * ((1 + inflation / 100) ** years_to_retirement)

        # Calculate corpus required (simple rule: 25x annual expense at retirement)
        annual_expense = expense_at_retirement * 12
        corpus_required = annual_expense * 25

        # Calculate SIP needed (using future value of SIP formula, simplified)
        n = years_to_retirement * 12
        r = return_on_investment / 100 / 12
        if r > 0 and n > 0:
            sip = corpus_required * r / (((1 + r) ** n - 1) * (1 + r))
        else:
            sip = corpus_required / n if n > 0 else 0

        result = {
            "expense_at_retirement": f"₹{expense_at_retirement:,.0f}",
            "return_on_corpus": f"{return_on_corpus:.1f}",
            "return_on_investment": f"{return_on_investment:.1f}",
            "corpus_required": f"₹{corpus_required:,.0f}",
            "sip": f"₹{sip:,.0f}"
        }
        return jsonify({"success": True, "result": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
