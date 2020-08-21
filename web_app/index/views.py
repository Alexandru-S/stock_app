from flask import redirect, url_for, render_template, request
from . import index_blueprint
from random import randint
from .forms import LoginForm


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    room = randint(0, 10)
    return render_template('index.html', room=room)
