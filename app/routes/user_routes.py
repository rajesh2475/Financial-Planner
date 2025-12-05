from flask import Blueprint, request, render_template
from app.services.tax_service import calculate_tax
from app.utils.helpers import safe_float

user_bp = Blueprint("user", __name__)


@user_bp.route("/tax", methods=["GET", "POST"])
def tax_compare():
    if request.method == "POST":
        form_data = {
            "salary": safe_float(request.form.get("salary")),
            "hra": safe_float(request.form.get("hra")),
            "sec80c": safe_float(request.form.get("sec80c")),
            "nps": safe_float(request.form.get("nps")),
            "sec80d": safe_float(request.form.get("sec80d")),
            "home_loan": safe_float(request.form.get("home_loan")),
            "other": safe_float(request.form.get("other")),
            "standard": safe_float(request.form.get("standard"), 50000),
        }
        result = calculate_tax(form_data["salary"], form_data)
        return render_template("tax_compare.html", form=form_data, result=result)

    return render_template("tax_compare.html", form={}, result=None)