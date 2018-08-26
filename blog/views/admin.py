from flask import Blueprint
from flask_login import login_required
from blog.models import Post
from flask.ext.mako import render_template


mod = Blueprint('admin', __name__)


@mod.route("/", methods=['GET'])
# @login_required
def post_edit():
    return render_template('admin/index.html')


@mod.route("/new_post/", methods=['GET'])
# @login_required
def post_new():
    return render_template('admin/new_post.html')
