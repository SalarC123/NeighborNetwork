import json
from app.database import db

cols = ('id', 'poster', 'description', 'datetime', 'timeframe', 'location', 'cost')

class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poster = db.Column(db.String(80))
    description = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    timeframe = db.Column(db.DateTime)
    location = db.Column(db.String(160))
    cost = db.Column(db.String(80))

    def __init__(self, payload):
      for k in cols:
        if k == 'id':
          continue

        if payload.get(k):
            setattr(self, k, payload[k])

    def __repr__(self):
        return "<Post: {}>".format(self.email)

    def to_dict(self):
        d = {}
        for k in cols:
            val = getattr(self, k)
            if val:
                d[k] = val
        return d
