from ..ma import ma
# from models import UserModel
from ..models import UserModel
# from models.todo import TodoModel
from ..models import TodoModel
# from schemas.todo import TodoSchema
from ..schemas import TodoSchema
from ..schemas import GroupSchema

class UserSchema(ma.ModelSchema):
    todos = ma.Nested(TodoSchema, many=True, exclude=('user',))
    groups = ma.Nested("GroupSchema", many=True, exclude=('todos', ))
    class Meta:
        model = UserModel
        load_only=('password',)
