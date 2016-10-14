from flask import Blueprint
from flask_mako import render_template
from .. import app

mod = Blueprint('post', __name__)


@mod.route("/<id>")
def get(id):
    app.logger.warning(id)

    return render_template('post.html', biaoti='标题')
