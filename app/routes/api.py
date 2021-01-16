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


@blueprint.route('/user', methods=['POST'])
def user():
    pass