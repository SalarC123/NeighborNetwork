from flask import Blueprint, request, abort
from app import settings
from firebase_admin import auth
from app.models.user import User
from app.database import db

blueprint = Blueprint('api', __name__, url_prefix='/api')

@blueprint.route('/register', methods=['POST'])
def register():
    payload = request.json
    user = None
    db_user = None
    try:
        user = auth.create_user(**{
            'email': payload['email'],
            'password': payload['password']
        })
        db_user = User(user.uid, user.email, payload['zip_code'])
        db.session.add(db_user)
        db.session.commit()
    except Exception as e:
        print(e)
        if user and not User.query.get(user.uid):
            auth.delete_user(user.uid)
        abort(400)
    return db_user.to_dict(), 200


@blueprint.route('/user')
def user():
    try:
        id_token = request.cookies.get('id_token')
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    user = User.query.get(decoded_token['uid'])
    
    return user.to_dict(), 200