from ..db import db

class UserGroupsModel(db.Model):
    __tablename__ = 'user_groups'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key = True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key = True)
    # user = db.relationship('UserModel', backref = db.backref("user_groups", cascade = "all, delete-orphan"))
    # group = db.relationship('GroupModel', backref = db.backref("user_groups", cascade = "all, delete-orphan"))

    @classmethod
    def find_by_uid_and_gid(cls, uid, gid):
        return cls.query.filter_by(user_id=uid,group_id=gid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()