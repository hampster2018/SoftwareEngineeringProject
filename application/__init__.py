from flask import Flask
from werkzeug.local import LocalProxy
from flask_login import LoginManager
from flask_pymongo import PyMongo

mongo = PyMongo()
login_manager = LoginManager()

def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app.secret_key=app.config['SECRET_KEY']

    mongo.init_app(app)
    login_manager.init_app(app)

    with app.app_context():

        from . import routes
        from . import auth
        from . import db
        
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        return app