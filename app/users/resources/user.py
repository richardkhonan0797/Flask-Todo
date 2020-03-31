from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required
)
from ...models import UserModel
from ...schemas import UserSchema

user_schema = UserSchema()

INVALID_CRED = 'Invalid credentials.'

class User(Resource):
    def get(self, name):
        user = UserModel.find_by_name(name)
        return user_schema.dump(user)

class UserRegister(Resource):
    def post(self):
        user_json = request.get_json()
        user = user_schema.load(user_json)
        user.save_to_db()
        return user_schema.dump(user), 201

class UserLogin(Resource):
    def post(self):
        user_json = request.get_json()
        user = UserModel.find_by_name(user_json["username"])
        if user and user.password == user_json["password"]:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(identity=user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        return {'message': INVALID_CRED}, 401

class Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        user_id = get_jwt_identity()
        new_token = create_access_token(identity=user_id, fresh=False)
        return {'access_token': new_token}, 200
