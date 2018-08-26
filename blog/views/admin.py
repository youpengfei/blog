from flask import Blueprint
from flask_login import login_required
from flask import render_template, _request_ctx_stack

from blog.models import Post

mod = Blueprint('admin', __name__,
                static_folder='./frontend/dist',
                template_folder='./frontend')


@mod.route("/", methods=['GET'])
# @login_required
def post_edit():
    return render_template('index.html')
