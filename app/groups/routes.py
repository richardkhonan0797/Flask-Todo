from .resources.group import Group

def initialize_routes(api):
    api.add_resource(Group, '/group/<string:name>')
