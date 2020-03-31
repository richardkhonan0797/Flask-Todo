from flask import Blueprint, request
from flask_restful import Api
from .routes import initialize_routes

todosApp = Blueprint('todos', __name__)
todos_app_api = Api(todosApp)
initialize_routes(todos_app_api)
