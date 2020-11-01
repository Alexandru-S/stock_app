from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

from .index.views import index_blueprint


def create_app(debug=True):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'secret'
    app.register_blueprint(index_blueprint)
    socketio.init_app(app)
    return app
