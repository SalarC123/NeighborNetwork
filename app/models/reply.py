from app.database import db

cols = ('id', 'post_id', 'poster', 'datetime', 'message')

class Reply(db.Model):
    __tablename__ = 'reply'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.String(80))
    poster = db.Column(db.String(80))
    datetime = db.Column(db.DateTime)
    message = db.Column(db.String(80))

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
