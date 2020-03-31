from flask import Blueprint, request
from flask_restful import Api
from .routes import initialize_routes

usersApp = Blueprint("users", __name__)
api_user_app = Api(usersApp)
initialize_routes(api_user_app)