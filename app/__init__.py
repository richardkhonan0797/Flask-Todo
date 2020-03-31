import os

from flask import Flask, request
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from dotenv import load_dotenv
from .config import app_config

from .db import db
from .ma import ma

def create_app(config_name):
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config.from_object(app_config["development"])
    app.config.from_pyfile("config.py")
    db.init_app(app)

    @app.errorhandler
    def handle_marshmallow_validation(err):
        return jsonify(error=err)

    @app.before_first_request
    def create_tables():
        db.create_all()

    ma.init_app(app)
    jwt.init_app(app)


    from .users import usersApp
    from .groups import groupsApp
    from .todos import todosApp
    from .user_groups import userGroupsApp

    app.register_blueprint(usersApp)
    app.register_blueprint(todosApp)
    app.register_blueprint(groupsApp)
    app.register_blueprint(userGroupsApp)

    return app