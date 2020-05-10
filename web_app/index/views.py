from flask import session, redirect, url_for, render_template, request
from . import index_blueprint
# generate random integer values
from random import seed
from random import randint
from .forms import LoginForm
import yfinance as yf


@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    print('---------')
    room = randint(0, 10)
    return render_template('index.html', room=room)



@index_blueprint.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)

