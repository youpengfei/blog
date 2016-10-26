import bcrypt
from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    status = db.Column(db.String(150))

    def verify_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8')) == self.password.encode('utf-8')

        # return hashlib.md5(
        #     str("%s-%s" % (app.config.get("PASSWORD_SALT"), password)).encode('utf-8')).hexdigest() == self.password

    def __repr__(self):
        return "<User(user='%d',name=%s email='%s',password='%s' )>" % (
            self.id, self.name, self.email, self.password)


class Post(db.Model, UserMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150))
    markdown = db.Column(db.Text)
    html = db.Column(db.Text)
    status = db.Column(db.String(150))
