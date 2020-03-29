from ma import ma
from models.user import UserModel
from models.todo import TodoModel
from schemas.todo import TodoSchema
from schemas.group import GroupSchema

class UserSchema(ma.ModelSchema):
    todos = ma.Nested(TodoSchema, many=True, exclude=('user',))
    groups = ma.Nested("GroupSchema", many=True, exclude=('todos', ))
    class Meta:
        model = UserModel
        load_only=('password',)
