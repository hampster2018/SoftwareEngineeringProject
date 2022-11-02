import datetime
from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")  
#def home():
#    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/") # TO DO: Change to "/Accident-Monitor"
def user():
    return render_template('accidentMonitor.html')


if __name__ == "__main__":
    app.run()