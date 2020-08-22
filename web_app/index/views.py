from flask import url_for, render_template, request
from . import index_blueprint
from random import randint


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    room = randint(0, 10)
    return render_template('index.html', room=room)
