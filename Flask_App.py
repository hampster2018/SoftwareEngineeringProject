import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run()