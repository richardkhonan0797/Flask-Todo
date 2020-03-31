from flask import Blueprint, request
from flask_restful import Api
from .routes import initialize_routes

groupsApp = Blueprint('groups', __name__)
groups_app_api = Api(groupsApp)
initialize_routes(groups_app_api)
