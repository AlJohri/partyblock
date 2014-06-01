from . import db

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self,id,username,pw_hash):
        self.id = id
        self.username = username