import datetime
from flask import Flask, render_template
import configparser

config = configparser.ConfigParser()
config.read('.env')
API_Key = config['APIKey']['GOOGLE_MAP_KEY']

app = Flask(__name__)

#@app.route("/")  
#def home():
#    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/AccidentMonitor")
def user():
    return render_template('accidentMonitor.html')

@app.route("/Payment")
def payment():
    fees = [(49, "chicken"), (31, "soup"), (100, "Awesome")]
    total = sum(row[0] for row in fees)
    return render_template('payment.html', name="Eric Shields", fees=fees, total=total)

@app.route("/accountPreferences")
def accountPreferences():
    return render_template('accountPreferences.html')

@app.route("/Emergency")
def contact_emergency():
    return render_template('contactEmergency.html')

@app.route("/ReportIncidents")
def report_incidents():
    return render_template('reportIncidents.html')

@app.route("/Map")
def map():
    return render_template('map.html', mapLink="https://maps.googleapis.com/maps/api/js?key=" + API_Key + "&callback=initMap&v=weekly")

@app.route("/Vehicle_Research")
def vehicleResearch():
    return render_template("vehicleResearch.html")

@app.route("/License_Link")
def licenseLink():
    return render_template("licenseLink.html")

@app.route("/Report_Conditions")
def reportConditions():
    return render_template("reportConditions.html")

@app.route("/Submitted_Conditions")
def submittedConditions():
    return render_template("submittedConditions.html")
    
@app.route("/reportAnIssue")
def reportAnIssue():
    return render_template('reportAnIssue.html')


if __name__ == "__main__":
    app.run()