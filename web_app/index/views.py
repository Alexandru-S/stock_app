from flask import Blueprint, render_template
from . import index_blueprint

@index_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")
