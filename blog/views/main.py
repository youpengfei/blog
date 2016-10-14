from flask import Blueprint
from flask_mako import render_template

from .. import app

mod = Blueprint('main', __name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def connect():
    return render_template('contact.html')
