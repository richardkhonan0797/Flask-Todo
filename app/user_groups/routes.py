from .resources.user_groups import AddUser

def initialize_routes(api):
    api.add_resource(AddUser, '/group/<string:name>/add-user')
