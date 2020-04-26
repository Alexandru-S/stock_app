from flask import Flask
from .index.views import index_blueprint
app = Flask(__name__)
app.register_blueprint(index_blueprint)