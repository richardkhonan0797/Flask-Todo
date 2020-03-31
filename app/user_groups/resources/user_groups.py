from flask_restful import Resource
from flask import request
from ...models import UserModel
# from models.group import GroupModel
from ...models import GroupModel
# from schemas.user_group import UserGroupsSchema
from ...schemas import UserGroupsSchema
from ...db import db

USER_NOT_FOUND = "User '{}' not found."
GROUP_NOT_FOUND = "Group '{}' not found."

user_groups_schema = UserGroupsSchema()

class AddUser(Resource):
    def post(self, name):
        request_json = request.get_json()
        user = UserModel.find_by_name(request_json["username"])
        if not user:
            return {'message': USER_NOT_FOUND}, 404
        group = GroupModel.find_by_name(name)
        if not group:
            return {'message': GROUP_NOT_FOUND}, 404
        new_user_groups = {
            "user_id": user.id,
            "group_id": group.id
        }
        print(type(new_user_groups),"INI NEW USE")
        user_groups = user_groups_schema.load(new_user_groups, session=db.session)
        user_groups.save_to_db()
        return user_groups_schema.dump(user_groups)
