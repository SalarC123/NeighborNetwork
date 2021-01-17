from flask import Blueprint, send_from_directory, render_template, request
from firebase_admin import auth
from app.models.user import User
from sqlalchemy import func, distinct
from app.database import db

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def root():
    user = None
    try:
        id_token = request.cookies.get('id_token')
        decoded_token = auth.verify_id_token(id_token)
        user = User.query.get(decoded_token['uid'])
    except:
        pass
        # this user is not logged in or session has expired

    content = 'null'
    if user:
        content = user.to_dict()

    community_count = 0
    try:
        community_count = db.session.query(func.count(distinct(User.zip_code)))[0][0]
    except:
        pass
    
    return render_template('index.html', **{'content':content, 'community_count': community_count})

@blueprint.route('/<path:filepath>')
def serve(filepath):
    return send_from_directory('./app/static', filename=filepath)
