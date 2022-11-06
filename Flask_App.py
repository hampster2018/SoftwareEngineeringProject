import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/Payment")
def payment():
    fees = [(49, "chicken"), (31, "soup"), (100, "Awesome")]
    total = sum(row[0] for row in fees)
    return render_template('payment.html', name="Eric Shields", fees=fees, total=total)

@app.route("/ReportIncidents")
def report_incidents():
    return render_template('reportIncidents.html')

if __name__ == "__main__":
    app.run()