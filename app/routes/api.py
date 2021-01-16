from flask import Blueprint, request, abort
from app import settings
from firebase_admin import auth
from app.database import db

blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/register', methods=['POST'])
def register():
    payload = request.json

    user = auth.create_user(**{
        'email': payload['email'],
        'password': payload['password']
    })
    zip_code = payload['zip_code']
    return {'uid': user.uid, 'email': payload['email'], 'zip_code': zip_code}, 200


@blueprint.route('/user')
def user():
    try:
        id_token = request.headers.get('Authorization', '').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    uid = decoded_token['uid']
    email = decoded_token['email']
    
    return {'uid': uid, 'email': email}, 200