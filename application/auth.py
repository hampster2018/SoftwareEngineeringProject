"""Routes for user authentication."""
from flask import Blueprint
from flask import current_app as app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import login_manager
from .forms import LoginForm, SignupForm
from .db import Signup, MakeUser, CheckAuth, GetUserById


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
        existing_user = Signup(form.email.data)
        if existing_user is None:
            user = {
                "firstName": form.firstName.data,
                "lastName": form.lastName.data,
                "email": form.email.data,
                "password": generate_password_hash(form.password.data, method="sha256")
            }
            MakeUser(user)
            login_user(user)  # Log in as newly created user
            print(user)
            return redirect(url_for("main_bp.dashboard"))
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
    """
    Log-in page for registered users.
    GET: Serve Log-in page.
    POST: Validate form and redirect user to dashboard.
    """
    if current_user.is_authenticated:
        return redirect(url_for("main_bp.dashboard"))  # Bypass if user is logged in

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = CheckAuth(email)
        if check_password_hash(generate_password_hash(pwhash=form.password.data, password=user['password'])):
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page or url_for("main_bp.dashboard"))
        flash("Invalid username/password combination")
        return redirect(url_for("auth_bp.login"))
    return render_template(
        "login.jinja2",
        form=form,
        title="Log in.",
        template="login-page",
        body="Log in with your User account.",
    )


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return GetUserById(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect(url_for("auth_bp.login"))