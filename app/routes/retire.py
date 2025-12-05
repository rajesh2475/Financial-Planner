from flask import Blueprint, request, render_template
import math
from app.utils.helpers import safe_float, safe_int

retire_bp = Blueprint("retire", __name__)

def calculate_retirement_corpus(data):
    current_age = safe_int(data.get("current_age", 0))
    retirement_age = safe_int(data.get("retirement_age", 0))
    life_expectancy = safe_int(data.get("life_expectancy", 0))
    monthly_expense_now = safe_float(data.get("monthly_expense_now", 0))
    inflation = safe_float(data.get("inflation", 0)) / 100
    return_on_corpus = safe_float(data.get("return_on_corpus", 0)) / 100
    return_on_investment = safe_float(data.get("return_on_investment", 0)) / 100

    years_to_retire = retirement_age - current_age
    years_in_retirement = life_expectancy - retirement_age

    monthly_expense_at_retirement = monthly_expense_now * ((1 + inflation) ** years_to_retire)

    r_corpus = return_on_corpus / 12
    n_corpus = years_in_retirement * 12
    corpus_required = monthly_expense_at_retirement * ((1 - (1 + r_corpus) ** -n_corpus) / r_corpus)

    r_invest = return_on_investment / 12
    n_invest = years_to_retire * 12
    sip_to_be_invested = corpus_required / (((1 + r_invest) ** n_invest - 1) / r_invest)

    return {
        "years_to_retire": years_to_retire,
        "monthly_expense_at_retirement": round(monthly_expense_at_retirement, 2),
        "corpus_required": round(corpus_required, 2),
        "sip_to_be_invested": round(sip_to_be_invested, 2)
    }

@retire_bp.route("/retire", methods=["GET", "POST"])
def retire_calculator():
    if request.method == "GET":
        form_data = {
            "current_age": "",
            "retirement_age": "",
            "life_expectancy": "",
            "monthly_expense_now": "",
            "inflation": "",
            "return_on_corpus": "",
            "return_on_investment": ""
        }
        return render_template("retire.html", form=form_data, result=None)

    if request.method == "POST":
        form_data = {
            "current_age": request.form.get("current_age", ""),
            "retirement_age": request.form.get("retirement_age", ""),
            "life_expectancy": request.form.get("life_expectancy", ""),
            "monthly_expense_now": request.form.get("monthly_expense_now", ""),
            "inflation": request.form.get("inflation", ""),
            "return_on_corpus": request.form.get("return_on_corpus", ""),
            "return_on_investment": request.form.get("return_on_investment", "")
        }

        try:
            result = calculate_retirement_corpus(form_data)
            return render_template("retire.html", form=form_data, result=result)
        except Exception:
            return render_template("retire.html", form=form_data, result=None, error="Invalid input")
