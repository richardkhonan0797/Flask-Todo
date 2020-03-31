from .resources.todo import Todo, TodoList, GroupTodo

def initialize_routes(api):
    api.add_resource(Todo, '/todo/<string:name>')
    api.add_resource(TodoList, '/todos')
    api.add_resource(GroupTodo, '/group/<string:group_name>/todo/<string:todo_name>')
