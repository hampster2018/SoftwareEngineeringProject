from flask import Flask
from werkzeug.local import LocalProxy
from flask_login import LoginManager
from flask_session import Session
from .db import get_db


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        from . import routes
        
        app.register_blueprint(routes.main_bp)

        return app