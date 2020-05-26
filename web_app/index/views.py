from flask import session, redirect, url_for, render_template, request
from . import index_blueprint
# generate random integer values
from random import seed
from random import randint
from .forms import LoginForm
import yfinance as yf


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    room = randint(0, 10)
    return render_template('index.html', room=room)
