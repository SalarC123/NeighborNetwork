import os
import firebase_admin
from flask import Flask
from . import settings, controllers, routes
from .database import db

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, static_folder='static', static_url_path='')
    app.config.from_object(config_object)

    register_database(app)
    register_firebase(app)
    register_blueprints(app)
    return app

def register_database(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()

def register_firebase(app):
    creds = firebase_admin.credentials.Certificate(settings.FIREBASE_ADMIN_CONFIG)
    firebase_admin.initialize_app(creds)

def register_blueprints(app):
    app.register_blueprint(controllers.home.blueprint)
    app.register_blueprint(routes.api.blueprint)
