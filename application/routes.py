from flask import Blueprint
from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from .roles import roles_required
from .db import *

import random
import string

main_bp = Blueprint(
    "main_bp", __name__, template_folder="templates", static_folder="static"
)

@main_bp.route("/")
@login_required
def home():
    roles = GetRoles()
    if "Admin" in roles:
        return render_template("mainMenu.html", Admin=True)
    return render_template("mainMenu.html", Admin=False)

@main_bp.route("/AccountPreferences")
@login_required
def accPreference():
    user = GetUserById()
    email = user['email']
    name = user['name']
    return render_template("accountPreferences.html", email=email, name=name)

@main_bp.route("/updateEmail")
@login_required
def updateEmail():
    user = GetUserById()
    email = user['email']
    return render_template("updateEmail.html", email=email)

@main_bp.route("/handleUpdateEmail", methods=['POST', 'GET'])
@login_required
def handleUpdateEmail():
    newEmail = request.form['newEmail']
    UpdateUserEmail(newEmail)
    return redirect(url_for('main_bp.accPreference'))

@main_bp.route("/ReportIncidents")
@login_required
def reportIncidents():
    return render_template("reportIncidents.html")

@main_bp.route("/ReportConditions")
@login_required
def reportConditions():
    return render_template("reportConditions.html")

@main_bp.route("/conditionSubmission/<issueNum>")
@login_required
def conditionSubmission(issueNum):
    switch={
        1: 'Heavy Rain',
        2: 'Flash Flood',
        3: 'Strong Winds',
        4: 'Heavy Snow',
        5: 'Icy Roads'
    }
    issue = switch.get(int(issueNum), "nothing")
    return render_template("conditionSubmission.html", issue=issue, issueNum=issueNum)

@main_bp.route("/handleConditionSubmission/<issue>", methods=['POST', 'GET'])
@login_required
def handleconditionSubmission(issue):
    formdata = request.form
    MakeIssue(issue, formdata['issue'])
    return redirect(url_for('main_bp.home'))

@main_bp.route("/VehicleResearch", methods=['GET', 'POST'])
@login_required
def vehicleResearch():

    if request.method == 'POST':
        print('hi')
        formdata = request.form
        car = GetLicensePlate(formdata['license'], formdata['state'])
        print(car)
        if car is None:
            return redirect(url_for('main_bp.no_license'))
        return redirect(location="/foundLicense/"  + car['Plate'] + "/" + car['State'] + "/" + car['VIN'] + "/" + car['Model'] + "/" + car['Make'] + "/" + str(car['Year']))
    return render_template("vehicleResearch.html/")

@main_bp.route("/ViolationMonitor")
@login_required
def violationMonitor():
    return render_template("violationMonitor.html")

@main_bp.route("/AccidentMonitor")
@login_required
def accidentMonitor():
    return render_template("accidentMonitor.html")

## The report issue page takes in a issue type by selection and renders issue submission
@main_bp.route("/ReportAnIssue")
@login_required
def reportIssue():
    return render_template("reportAnIssue.html")    

## Renders issue submission by taking in the issue number given and puts out the 
## appropriate issue type. Will then take in a description and route to handle
## Issue Submission to process that data
@main_bp.route("/issueSubmission/<issueNum>")
@login_required
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
@login_required
def handleIssueSubmission():
    formdata = request.form['issue']
    MakeAppIssue([formdata])
    return redirect(url_for('main_bp.home'))

## Issue Sumbission for reporting Incidents
@main_bp.route("/issueSubmission_incident/<issueNum>")
@login_required
def issueSubmission_incident(issueNum):
    switch={
        1: 'Car Crash',
        2: 'Traffic Jam',
        3: 'Speed Trap',
        4: 'Construction Zone',
        5: 'Hazard'
    }
    issue = switch.get(int(issueNum), "nothing")
    return render_template("issueSubmissionIncidents.html", issue=issue, issueNum=issueNum)

@main_bp.route("/handleIssueSubmission_incident/<issue>", methods=['POST', 'GET'])
@login_required
def handleIssueSubmission_incident(issue):
    formdata = request.form
    print(formdata)
    MakeIssue(issueType=issue, description=formdata['issue'], latitude=formdata['latitude'], longitude=formdata['longitude'])
    return redirect(url_for('main_bp.home'))

@main_bp.route("/ContactEmergency", methods=['POST', 'GET'])
@login_required
def contactEmergency():
    if request.method == 'POST':
        flash("Calling from your phone")
    return render_template("contactEmergency.html")

@main_bp.route("/PublicTransport")
@login_required
def transportation():
    return render_template("publicTransport.html")

@main_bp.route("/Settings")
@login_required
def settings():
    return render_template("settings.html")

@main_bp.route("/TollFeeAdmin")
@login_required
def toll_fees():
    tolls = GetTolls()
    return render_template("tollFees.html", tolls=tolls)

@main_bp.route("/foundLicense/<Plate>/<State>/<VIN>/<Model>/<Make>/<Year>")
@login_required
def found_license(Plate, State, VIN, Model, Make, Year):
    return render_template("FoundLicense.html", Plate=Plate, State=State, VIN=VIN, Model=Model, Make=Make, Year=Year)

@main_bp.route("/noLicense")
@login_required
def no_license():
    return render_template("licenseLink.html")
