from flask import Blueprint, request, render_template, jsonify

home_bp = Blueprint("home", __name__)

def calculate_home_loan(loan_amount, annual_rate, tenure_years):
    """
    Calculate EMI and total repayment for a home loan.
    loan_amount: principal
    annual_rate: interest rate in percentage (e.g., 8.5 means 8.5%)
    tenure_years: loan tenure in years
    """
    monthly_rate = (annual_rate / 100) / 12
    months = tenure_years * 12

    emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    total_payment = emi * months

    return {
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "interest_paid": round(total_payment - loan_amount, 2)
    }

@home_bp.route("/loan", methods=["GET", "POST"])
def loan_calculator():
    if request.method == "GET":
        form_data = {
            "loanAmount": "",
            "annualRate": "",
            "tenureYears": "",
            "rateChange": "",
            "emisPaid": ""
        }
        return render_template("home_loan.html", form=form_data, result=None)

    if request.method == "POST":
        try:
            loan_amount = float(request.form.get("loanAmount", 0))
            annual_rate = float(request.form.get("annualRate", 0))
            tenure_years = int(request.form.get("tenureYears", 0))

            base_result = calculate_home_loan(loan_amount, annual_rate, tenure_years)

            # Scenario only if rateChange is provided
            rate_change = request.form.get("rateChange")
            scenario = None
         
            if rate_change:
                rate_change = float(rate_change)
                emis_paid = int(request.form.get("emisPaid", 0))

                months = tenure_years * 12
                monthly_rate = (annual_rate / 100) / 12
                emi = base_result["emi"]

                # Remaining balance formula
                outstanding = loan_amount * ((1 + monthly_rate) ** months - (1 + monthly_rate) ** emis_paid) / ((1 + monthly_rate) ** months - 1)

                # New rate and tenure
                new_rate = annual_rate + rate_change
                new_months_left = months - emis_paid

                new_result = calculate_home_loan(outstanding, new_rate, new_months_left / 12)

                scenario = {
                    "emis_paid": emis_paid,
                    "rate_change": rate_change,
                    "new_rate": new_rate,
                    "outstanding": round(outstanding, 2),
                    "new_emi": new_result["emi"],
                    "new_total_payment": new_result["total_payment"],
                    "new_tenure_months": round(new_months_left, 2),
                    "change_in_total": round(new_result["total_payment"] - base_result["total_payment"], 2),
                    "change_in_amount": round(new_result["total_payment"] - (emi * months), 2)
                }

            form_data = {
                "loanAmount": loan_amount,
                "annualRate": annual_rate,
                "tenureYears": tenure_years,
                "rateChange": rate_change,
                "emisPaid": emis_paid
            }

            return render_template("home_loan.html", form=form_data, result=base_result, scenario=scenario)

        except (TypeError, ValueError):
            return jsonify({"error": "Invalid input"}), 400
