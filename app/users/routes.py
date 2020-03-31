from .resources.user import UserRegister, UserLogin, Refresh, User

def initialize_routes(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(Refresh, '/refresh')
    api.add_resource(User, '/user/<string:name>')
