from flask import Blueprint, jsonify
from flask_mako import render_template

from blog.models import Post

mod = Blueprint('post', __name__)


@mod.route("/<id>")
def get(id):
    post = Post.query.filter(Post.id.__eq__(id)).one_or_none()
    if (not post):
        return render_template('error/404.html')

    return render_template('post.html', post=post)
