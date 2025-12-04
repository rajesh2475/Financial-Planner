import os
from flask import Flask, render_template
from app.routes.user_routes import user_bp
from app.routes.spi import sip_bp

def create_app():
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates")
    # static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")

    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object("app.config.Config")

    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(sip_bp, url_prefix="/sip")

    @app.route("/home")
    def home():
        form_data = {}
        result = None
        return render_template("home.html", form=form_data, result=result)
        
    return app
