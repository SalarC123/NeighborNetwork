from flask import Blueprint, send_from_directory, render_template

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def root():
    return render_template('index.html', **{'content': 'test test'})

@blueprint.route('/<path:filepath>')
def serve(filepath):
    return send_from_directory('./app/static', filename=filepath)
