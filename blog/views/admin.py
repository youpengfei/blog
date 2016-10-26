from flask import Blueprint
from flask_login import login_required
from flask_mako import render_template

from blog.models import Post

mod = Blueprint('admin', __name__)


@mod.route("/post_edit", methods=['GET'])
@login_required
def post_edit():
    return render_template('admin/new_post.html')


@mod.route("/post", methods=['POST'])
@login_required
def post_post():
    return render_template('admin/new_post.html')


@mod.route("/post/list", methods=['GET'])
def post_list():
    posts = Post.query.all()
    return render_template('admin/post_list.html', posts=posts)
