from flask import Blueprint, send_from_directory, current_app

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def root():
    return current_app.send_static_file('index.html')

@blueprint.route('/<path:filepath>')
def serve(filepath):
    return send_from_directory('./app/static', filename=filepath)
