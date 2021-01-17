from app.database import db

cols = ('id', 'email', 'zip_code')

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    zip_code = db.Column(db.String(80), nullable=False)

    def __init__(self, firebase_id, email, zip_code):
        self.id = firebase_id
        self.email = email
        self.zip_code = zip_code

    def __repr__(self):
        return "<User: {}>".format(self.email)

    def to_dict(self):
        d = {}
        for k in cols:
            val = getattr(self, k)
            if val:
                d[k] = val
        return d
