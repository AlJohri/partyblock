from . import db, BaseModel

class Connection(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.user_id = kwargs.get('user_id')
        self.provider_id = kwargs.get('provider_id')
        self.provider_user_id = kwargs.get('provider_user_id')
        self.access_token = kwargs.get('access_token')
        self.secret = kwargs.get('secret')
        self.display_name = kwargs.get('display_name')
        self.profile_url = kwargs.get('profile_url')
        self.image_url = kwargs.get('image_url')
        self.rank = kwargs.get('rank')