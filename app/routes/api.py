from flask import Blueprint, request, abort
from app import settings
from firebase_admin import auth
from app.database import db

blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/register')
@blueprint.route('/user')
def user():
    try:
        id_token = request.headers.get('Authorization', '').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    uid = decoded_token['uid']
    email = decoded_token['email']
    return {'debug': decoded_token}, 200