from flask import Blueprint

index_blueprint = Blueprint('index', __name__, template_folder='templates', static_folder='static')

from . import views, events