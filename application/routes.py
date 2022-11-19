from flask import Blueprint
from flask import current_app as app
from flask import render_template

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/AccidentMonitor")
def user():
    return render_template('accidentMonitor.html')

@main_bp.route("/Payment")
def payment():
    fees = [(49, "chicken"), (31, "soup"), (100, "Awesome")]
    total = sum(row[0] for row in fees)
    return render_template('payment.html', name="Eric Shields", fees=fees, total=total)

@main_bp.route("/accountPreferences")
def accountPreferences():
    return render_template('accountPreferences.html')

@main_bp.route("/Emergency")
def contact_emergency():
    return render_template('contactEmergency.html')

@main_bp.route("/ReportIncidents")
def report_incidents():
    return render_template('reportIncidents.html')

@main_bp.route("/Map")
def map():
    return render_template('map.html', mapLink="https://maps.googleapis.com/maps/api/js?key=" + API_Key + "&callback=initMap&v=weekly")

@main_bp.route("/Vehicle_Research")
def vehicleResearch():
    return render_template("vehicleResearch.html")

@main_bp.route("/License_Link")
def licenseLink():
    return render_template("licenseLink.html")

@main_bp.route("/Report_Conditions")
def reportConditions():
    return render_template("reportConditions.html")

@main_bp.route("/Submitted_Conditions")
def submittedConditions():
    return render_template("submittedConditions.html")
    
@main_bp.route("/reportAnIssue")
def reportAnIssue():
    return render_template('reportAnIssue.html')

@main_bp.route("/")  
def home():
    return render_template('violationMonitor.html')