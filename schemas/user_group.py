from ma import ma
from models.user_groups import UserGroupsModel
from models.user import UserModel
from models.group import GroupModel
from models.todo import TodoModel

class UserGroupsSchema(ma.ModelSchema):
    user = ma.Nested("UserSchema", only=('id', 'username', ))
    group = ma.Nested("GroupSchema", only=('id', 'name', ))
    class Meta:
        model = UserGroupsModel
        include_fk=True