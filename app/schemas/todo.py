from ..ma import ma
from ..models.todo import TodoModel
from ..models.user import UserModel

class TodoSchema(ma.ModelSchema):
    user = ma.Nested("UserSchema", only=('id', 'username'))
    class Meta:
        model = TodoModel
        include_fk=True
