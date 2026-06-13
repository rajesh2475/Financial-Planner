# app.py
from flask import Flask, request, jsonify, render_template, Blueprint
from app.utils.helpers import safe_float, safe_int
sip_bp = Blueprint("sip", __name__)



def stepup_sip_schedule(
    planned_monthly_investment: float,
    years_of_investment: int,
    annual_return: float,
    increment_value: float,
    mode: str = "percent",  # "percent" or "value"
    holding_years: int = 0
):
    """
    Calculate step-up SIP schedule.
    - planned_monthly_investment: starting monthly SIP (e.g., 1000)
    - years_of_investment: active SIP years (e.g., 5)
    - annual_return: expected annual return as decimal (e.g., 0.12)
    - increment_value: if mode='percent', use 0.10 for +10% yearly; if mode='value', use absolute e.g. 500
    - holding_years: years after investment with no contributions
    """
    m_rate = annual_return / 12.0
    months_per_year = 12

    schedule = []
    value = 0.0
    monthly_investment = planned_monthly_investment

    # Active investment years with step-up
    for year in range(1, years_of_investment + 1):
        beginning_value = value
        # 12 months compounding + monthly contributions
        for _ in range(months_per_year):
            value = value * (1 + m_rate) + monthly_investment

        schedule.append({
            "year": year,
            "beginning_value": round(beginning_value, 2),
            "monthly_investment": round(monthly_investment, 2),
            "end_value": round(value, 2)
        })

        # Step-up for next year
        if mode == "percent":
            print(f"Step-up percent: {increment_value}, before: {monthly_investment}")
            monthly_investment = monthly_investment * (1 + increment_value)
            print(f"After: {monthly_investment}")
        else:
            monthly_investment = monthly_investment + increment_value

    # Holding period: compounding only, no contributions
    if holding_years and holding_years > 0:
        total_holding_months = holding_years * months_per_year
        beginning_value = value
        for _ in range(total_holding_months):
            value = value * (1 + m_rate)
        schedule.append({
            "year": f"Holding {holding_years}y",
            "beginning_value": round(beginning_value, 2),
            "monthly_investment": 0.00,
            "end_value": round(value, 2)
        })

    # Summary
    total_invested = 0.0
    # Sum of contributions across active years (12 months each)
    monthly = planned_monthly_investment
    for _y in range(years_of_investment):
        total_invested += monthly * months_per_year
        if mode == "percent":
            monthly = monthly * (1 + increment_value)
        else:
            monthly = monthly + increment_value

    return {
        "schedule": schedule,
        "summary": {
            "final_value": round(value, 2),
            "total_invested": round(total_invested, 2),
            "gain": round(value - total_invested, 2)
        }
    }


@sip_bp.route("/stepup", methods=["GET", "POST"])
def api_stepup():
    if request.method == "GET":
        # Empty form, no results yet
        form_data = {
            "plannedMonthlyInvestment": "",
            "yearsOfInvestment": "",
            "annualReturn": "",
            "incrementValue": "",
            "mode": "percent",
            "holdingYears": ""
        }
        return render_template("incremental_sip.html", form=form_data, result=None)

    if request.method == "POST":
        # Handle both JSON and form-encoded requests
        try:
            if request.is_json:
                data = request.get_json()
                planned_monthly_investment = safe_float(data.get("plannedMonthlyInvestment", 0))
                years_of_investment = int(data.get("yearsOfInvestment", 0))
                annual_return = safe_float(data.get("annualReturn", 0)) / 100
                holding_years = safe_int(data.get("holdingYears", 0))
                mode = data.get("mode", "percent")
                increment_value = safe_float(data.get("incrementValue", 0))
                
                # For JSON, if mode is "value", don't divide by 100
                if mode == "percent":
                    increment_value = increment_value / 100
            else:
                # Form-encoded request
                planned_monthly_investment = safe_float(request.form.get("plannedMonthlyInvestment", 0))
                years_of_investment = int(request.form.get("yearsOfInvestment", 0))
                annual_return = safe_float(request.form.get("annualReturn", 0)) / 100
                holding_years = safe_int(request.form.get("holdingYears", 0))
                mode = request.form.get("mode", "percent")
                increment_value = safe_float(request.form.get("incrementValue", 0)) / 100

            if mode not in ("percent", "value"):
                return jsonify({"success": False, "error": "mode must be 'percent' or 'value'"}), 400

            # Validations
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
                holding_years=holding_years
            )

            annual_return_display = annual_return * 100  # Convert back to percentage for display
            increment_display = increment_value * 100 if mode == "percent" else increment_value

            # If JSON request, return JSON response
            if request.is_json:
                return jsonify({
                    "success": True,
                    "summary": {
                        "final_value": f"₹{result['summary']['final_value']:,.2f}",
                        "total_invested": f"₹{result['summary']['total_invested']:,.2f}",
                        "gain": f"₹{result['summary']['gain']:,.2f}"
                    },
                    "schedule": result['schedule']
                })
            
            # Otherwise render template
            form_data = {
                "plannedMonthlyInvestment": planned_monthly_investment,
                "yearsOfInvestment": years_of_investment,
                "annualReturn": annual_return_display,
                "incrementValue": increment_display,
                "mode": mode,
                "holdingYears": holding_years
            }
            return render_template("incremental_sip.html", form=form_data, result=result)
        except (TypeError, ValueError) as e:
            if request.is_json:
                return jsonify({"success": False, "error": str(e)}), 400
            return jsonify({"error": "Invalid input"}), 400

      


