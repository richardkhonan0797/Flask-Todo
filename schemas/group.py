from ma import ma
from models.group import GroupModel
from models.todo import TodoModel
from models.user import UserModel

class GroupSchema(ma.ModelSchema):
    todos = ma.Nested("TodoSchema", many=True, exclude=('group', 'group_id'))
    users = ma.Nested("UserSchema", many=True, only=('id', 'username', ))
    class Meta:
        model = GroupModel
        include_fk = True