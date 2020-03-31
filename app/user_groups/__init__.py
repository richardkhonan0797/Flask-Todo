from flask import Blueprint, request
from flask_restful import Api
from .routes import initialize_routes

userGroupsApp = Blueprint("user_groups", __name__)
user_groups_api = Api(userGroupsApp)
initialize_routes(user_groups_api)
