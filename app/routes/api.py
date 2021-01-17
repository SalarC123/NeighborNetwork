import datetime
from flask import Blueprint, request, abort
from app import settings
from firebase_admin import auth
from app.models.user import User
from app.models.post import Post
from app.models.reply import Reply
from app.models.event import Event
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

@blueprint.route('/post', methods=['GET', 'POST'])
def post():

    if request.method == 'GET':
        all_posts = Post.query.all()
        return {
            'posts': [post.to_dict() for post in all_posts]
        }, 200

    try:
        id_token = request.cookies.get('id_token')
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    user = User.query.get(decoded_token['uid'])
    payload = request.json
    payload['poster'] = user.id
    payload['datetime'] = datetime.datetime.utcnow()
    try:
        post = Post(payload)
        db.session.add(post)
        db.session.commit()
    except Exception as e:
        print(e)

    return post.to_dict(), 200

@blueprint.route('/post/<int:post_id>', methods=['GET', 'POST'])
def reply(post_id):
    if request.method == 'GET':
        all_replies_for_post = Reply.query.filter_by(post_id=post_id)
        return {
            'replies': [reply.to_dict() for reply in all_replies_for_post]
        }, 200

    try:
        id_token = request.cookies.get('id_token')
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    user = User.query.get(decoded_token['uid'])
    post = Post.query.get(post_id)
    payload = request.json
    payload['post_id'] = post.id
    payload['poster'] = user.id
    payload['datetime'] = datetime.datetime.utcnow()
    try:
        reply = Reply(payload)
        db.session.add(reply)
        db.session.commit()
    except Exception as e:
        print(e)

    return reply.to_dict(), 200

@blueprint.route('/event', methods=['GET', 'POST'])
def event():

    if request.method == 'GET':
        all_events = Event.query.all()
        return {
            'events': [event.to_dict() for event in all_events]
        }, 200

    try:
        id_token = request.cookies.get('id_token')
        decoded_token = auth.verify_id_token(id_token)
    except:
        abort(401)

    user = User.query.get(decoded_token['uid'])
    payload = request.json
    payload['poster'] = user.id
    payload['datetime'] = datetime.datetime.utcnow()
    try:
        event = Event(payload)
        db.session.add(event)
        db.session.commit()
    except Exception as e:
        print(e)

    return event.to_dict(), 200