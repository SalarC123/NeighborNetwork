import json
from app.database import db

cols = ('id', 'poster', 'datetime', 'droptime', 'location', 'groceries', 'cost', 'priority', 'replies')

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poster = db.Column(db.String(80))
    datetime = db.Column(db.DateTime)
    droptime = db.Column(db.DateTime)
    location = db.Column(db.String(160))
    groceries = db.Column(db.String)
    cost = db.Column(db.String(80))
    priority = db.Column(db.Integer)
    replies = db.Column(db.String)

    def __init__(self, payload):
      for k in cols:
        if k in ('id', 'replies'):
          continue

        if payload.get(k):
          if k == 'groceries':
            setattr(self, k, json.dumps(payload[k]))
          else:
            setattr(self, k, payload[k])

    def __repr__(self):
        return "<Post: {}>".format(self.email)

    def to_dict(self):
        d = {}
        for k in cols:
            val = getattr(self, k)
            if val:
              if k in ('groceries', 'replies'):
                d[k] = json.loads(val)
              else:
                d[k] = val
        return d
