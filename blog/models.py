import hashlib
from . import db, app
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def verify_password(self, password):
        return hashlib.md5(
            str("%s-%s" % (app.config.get("PASSWORD_SALT"), password)).encode('utf-8')).hexdigest() == self.password

    def __repr__(self):
        return "<User(user='%d',name=%s email='%s',password='%s' )>" % (
            self.id, self.name, self.email, self.password)


