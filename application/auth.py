"""Routes for user authentication."""
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, confirm_login, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from . import login_manager, mongo, sesh
from .forms import LoginForm, SignupForm
from .db import MakeUser, GetUserByEmail, GetUserById
from .models import User

from . import db

# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Sign-up form to create new user accounts.
    GET: Serve sign-up page.
    POST: Validate form, create account, redirect user to dashboard.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = GetUserByEmail(form.email.data)
        print("Existing Users:", existing_user)
        if len(existing_user) == 0:
            MakeUser({'name': form.name.data, 'email': form.email.data, 'password': generate_password_hash(form.password.data, method="sha256"), 'roles': ["User"]})
            user = GetUserByEmail(form.email.data)
            user = User(_id=user['_id'], name=user['name'], email=user['email'], password=user['password'], roles=user['roles'])
            login_user(user, force=True)
            return redirect(url_for("main_bp.home"))
        flash("A user already exists with that email address.")
    return render_template(
        "signup.jinja2",
        title="Create an Account.",
        form=form,
        template="signup-page",
        body="Sign up for a user account.",
    )


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main_bp.home"))  # Bypass if user is logged in

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = GetUserByEmail(email)
        if check_password_hash(pwhash=user['password'], password=form.password.data):
            user = User(_id=user['_id'], name=user['name'], email=user['email'], password=user['password'])
            login_user(user, force=True)
            return redirect(url_for("main_bp.home"))
        flash("Invalid username/password combination")
        return redirect(url_for("auth_bp.login"))
    return render_template(
        "login.jinja2",
        form=form,
        title="Log in.",
        template="login-page",
        body="Log in with your User account.",
    )


@auth_bp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():

    logout_user()
    return redirect(url_for("auth_bp.login"))



@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        user = GetUserById(user_id)
        if user is not None:
            userObject = User(str(user['_id']))
            return userObject
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth_bp.login"))