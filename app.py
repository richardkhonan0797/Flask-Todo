import os

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError
from dotenv import load_dotenv
from db import db
from ma import ma

from resources.user import UserRegister, UserLogin, User, Refresh
from resources.todo import Todo, TodoList, GroupTodo
from resources.group import Group
from resources.user_groups import AddUser

from schemas.todo import TodoSchema
from schemas.user import UserSchema

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY']=os.environ.get("SECRET")
app.config['PROPAGATE_EXCEPTION']=True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get("DB_URI", 'sqlite:///todo.db')
print(os.environ.get("SECRET"))

@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler
def handle_marshmallow_validation(err):
    return jsonify(error=err)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Refresh, '/refresh')
api.add_resource(User, '/user/<string:name>')
api.add_resource(Todo, '/todo/<string:name>')
api.add_resource(TodoList, '/todos')
api.add_resource(Group, '/group/<string:name>')
api.add_resource(AddUser, '/group/<string:name>/add-user')
api.add_resource(GroupTodo, '/group/<string:group_name>/todo/<string:todo_name>')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)