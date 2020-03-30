from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from models.todo import TodoModel
from models.user import UserModel
from models.group import GroupModel
from models.user_groups import UserGroupsModel
from schemas.todo import TodoSchema

todo_schema = TodoSchema()
todo_list_schema = TodoSchema(many=True)

NOT_FOUND = "Todo '{}' not found."
TODO_EXISTS = "Todo '{}' already exists."
NOT_AUTH = "You are not authorized."
DELETED = "Todo '{}' deleted."

class Todo(Resource):
    @jwt_required
    def get(self, name):
        user_id = get_jwt_identity()
        todo = TodoModel.find_by_name(name)
        if todo.user_id == user_id:
            return todo_schema.dump(todo), 200
        else:
            return {'message': NOT_AUTH}, 401
        return {'message': NOT_FOUND.format(name)}, 404
    
    @jwt_required
    def post(self, name):
        if TodoModel.find_by_name(name):
            return {'message': TODO_EXISTS.format(name)}, 400
        
        user_id = get_jwt_identity()
        todo_json = request.get_json()
        todo_json["name"] = name
        todo_json["user_id"] = user_id
        # todo_json["user"] = UserModel.find_by_id(user_id)
        todo = todo_schema.load(todo_json)
        todo.save_to_db()
        return todo_schema.dump(todo), 201

    @jwt_required
    def delete(self, name):
        todo = TodoModel.find_by_name(name)
        if not todo:
            return {'message': NOT_FOUND.format(name)}, 404
        
        todo.delete_from_db()
        return {'message': DELETED.format(name)}, 200

class TodoList(Resource):
    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        return todo_list_schema.dump(TodoModel.find_by_user_id(user_id)), 200

class GroupTodo(Resource):
    @jwt_required
    def post(self, group_name, todo_name):
        group = GroupModel.find_by_name(group_name)
        user_id = get_jwt_identity()
        if not group:
            return {'message': "Group '{}' not found.".format(group_name)}, 404
        user_group = UserGroupsModel.find_by_uid_and_gid(user_id, group.id)
        if not user_group:
            return {'message': NOT_AUTH}, 401
        todo_json = request.get_json()
        todo_json["name"] = todo_name
        todo_json["user_id"] = user_id
        todo_json["group_id"] = group.id
        todo = todo_schema.load(todo_json)
        todo.save_to_db()
        return todo_schema.dump(todo), 201

    @jwt_required
    def delete(self, group_name, todo_name):
        group = GroupModel.find_by_name(group_name)
        user_id = get_jwt_identity()
        if not group:
            return {'message': "Group '{}' not found.".format(group_name)}, 404
        user_group = UserGroupsModel.find_by_uid_and_gid(user_id, group.id)
        if not user_group:
            return {'message': NOT_AUTH}, 401
        todo = TodoModel.find_by_name(todo_name)
        todo.delete_from_db()
        return {'message': DELETED.format(todo_name)}, 200

