import os
from flask import Flask, render_template, redirect, url_for
from app.routes.user_routes import user_bp
from app.routes.spi import sip_bp
from app.routes.home_loan import home_bp
from app.routes.retire import retire_bp
from app.routes.tax_full import tax_full_bp

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates")
    # static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")

    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object("app.config.Config")

    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(sip_bp, url_prefix="/sip")
    app.register_blueprint(home_bp, url_prefix="/home")
    app.register_blueprint(retire_bp, url_prefix="/retire")
    app.register_blueprint(tax_full_bp, url_prefix="/tax")

    @app.route("/home")
    def home():
        form_data = {}
        result = None
        return render_template("home.html", form=form_data, result=result)
    
    @app.route("/")
    def default_page():
        # Redirect to the SIP step-up route
        return redirect(url_for("user.tax_compare"))        
    return app
