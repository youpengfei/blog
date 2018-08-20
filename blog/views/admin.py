from flask import Blueprint
from flask_login import login_required
from flask_mako import render_template

from blog.models import Post

mod = Blueprint('admin', __name__,
                static_folder='./frontend/dist/static',
                template_folder='./frontend/dist')


@mod.route("/", methods=['GET'])
# @login_required
def post_edit():
    return render_template('index.html')
