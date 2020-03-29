from flask_restful import Resource
from models.group import GroupModel
from schemas.group import GroupSchema

group_schema = GroupSchema()

NOT_FOUND = "Group '{}' doesn't exists."
EXISTS = "Group '{}' already exists."

class Group(Resource):
    def get(self, name):
        group = GroupModel.find_by_name(name)
        if group:
            return group_schema.dump(group), 200
        return {'message': NOT_FOUND.format(name)}, 404

    def post(self, name):
        if GroupModel.find_by_name(name):
            return {'message': EXISTS.format(name)}, 400
        group = group_schema.load({'name': name})
        group.save_to_db()
        return group_schema.dump(group), 201

    def delete(self, name):
        group = GroupModel.find_by_name(name)
        if group:
            return {'message': NOT_FOUND.format(name)}, 404
        group.delete_from_db()
        return {'message': "Group '{}' deleted.".format(name)}, 200

