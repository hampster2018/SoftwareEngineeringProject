from flask import Blueprint
from flask import current_app as app
from flask import render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user

from .roles import roles_required
from .db import *

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/")
def home():
    return render_template("mainMenu.html")

@main_bp.route("/Map")
def googleMaps():
    return render_template("map.html")

@main_bp.route("/AccountPreferences")
def accPreference():
    user = GetUserById()
    email = user['email']
    name = user['name']
    return render_template("accountPreferences.html", email=email, name=name)

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

## The report issue page takes in a issue type by selection and renders issue submission
@main_bp.route("/ReportAnIssue")
def reportIssue():
    return render_template("reportAnIssue.html")    

## Renders issue submission by taking in the issue number given and puts out the 
## appropriate issue type. Will then take in a description and route to handle
## Issue Submission to process that data
@main_bp.route("/issueSubmission/<issueNum>")
def issueSubmission(issueNum):
    switch={
        1: 'GPS and Network',
        2: 'Routes',
        3: 'Map',
        4: 'Voice and Sound',
        5: 'My Account',
        6: 'Feedback and suggestions'
    }
    issue = switch.get(int(issueNum), "nothing")
    return render_template("issueSubmission.html", issue=issue, issueNum=issueNum)

## Takes in Data Here from the previous form and saves it using MakeIssue DB call
## Redirects to home page
@main_bp.route("/handleIssueSubmission", methods=['POST', 'GET'])
def handleIssueSubmission():
    formdata = request.form['issue']
    MakeAppIssue([formdata])
    return redirect(url_for('main_bp.home'))

@main_bp.route("/ContactEmergency")
def contactEmergency():
    return render_template("contactEmergency.html")

@main_bp.route("/PublicTransport")
def transportation():
    return render_template("publicTransport.html")

@main_bp.route("/Settings")
def settings():
    return render_template("settings.html")

@main_bp.route("/TollFeeAdmin")
def toll_fees():
    tolls = GetTolls()
    return render_template("tollFees.html", tolls=tolls)

@main_bp.route("/test")
def test():
    print("Car Crash number 2 is: " + GetIssue('Car Crash', 2)['name'])
    return render_template("publicTransport.html")
