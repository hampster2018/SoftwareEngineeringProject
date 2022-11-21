from flask import Blueprint
from flask import current_app as app
from flask import render_template, redirect, url_for
from flask_login import login_required, logout_user, current_user

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))

@main_bp.route("/")
def home():
    return render_template("mainMenu.html")

@main_bp.route("/Login")
def signIn():
    return redirect(url_for("auth_bp.login"))

@main_bp.route("/Map")
def googleMaps():
    return render_template("map.html")

@main_bp.route("/AccountPreferences")
def accPreference():
    return render_template("accountPreferences.html")

@main_bp.route("/ReportIncidents")
def reportIncidents():
    return render_template("reportIncidents.html")

@main_bp.route("/ReportConditions")
def reportConditions():
    return render_template("reportConditions.html")

@main_bp.route("/VehicleResearch")
def vehicleResearch():
    return render_template("vehicleResearch.html")

@main_bp.route("/ViolationMonitor")
def violationMonitor():
    return render_template("violationMonitor.html")

@main_bp.route("/AccidentMonitor")
def accidentMonitor():
    return render_template("accidentMonitor.html")

@main_bp.route("/ReportAnIssue")
def reportIssue():
    return render_template("reportAnIssue.html")

@main_bp.route("/ContactEmergency")
def contactEmergency():
    return render_template("contactEmergency.html")

@main_bp.route("/PublicTransport")
def transportation():
    return render_template("publicTransport.html")

@main_bp.route("/Settings")
def settings():
    return render_template("settings.html")

