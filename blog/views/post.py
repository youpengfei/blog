from flask import Blueprint
from flask_mako import render_template

from blog.models import Post

mod = Blueprint('post', __name__)


@mod.route("/<id>")
def get(id):
    post = Post.query.filter(Post.id.__eq__(id)).one()
    return render_template('post.html', post=post)
