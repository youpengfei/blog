from flask import Blueprint
from flask_login import login_required
from blog.models import Post

mod = Blueprint('admin', __name__)


@mod.route("/", methods=['GET'])
@login_required
def post_edit():
    return render_template('admin/index.html')
