from flask import Blueprint
from flask_mako import render_template

from blog.models import Post
from .. import app

mod = Blueprint('main', __name__,
                static_folder='./static',
                template_folder='./templates'
                )


@app.route("/")
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def connect():
    return render_template('contact.html')
