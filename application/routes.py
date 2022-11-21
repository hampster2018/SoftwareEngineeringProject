from flask import Blueprint
from flask import current_app as app
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/")
def home():
        print(current_user)
        return render_template("login.html")

@main_bp.route("/session")
@login_required
def session_view():
    return render_template("accidentMonitor.html")

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))