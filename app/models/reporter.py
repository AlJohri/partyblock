from . import db, BaseModel

from sqlalchemy.orm import relationship

class Reporter(BaseModel, db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    witty_title = db.Column(db.String)
    civic_points = db.Column(db.BigInteger)
    name = db.Column(db.String)
    issues = relationship("Issue")

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.witty_title = kwargs.get('witty_title')
        self.civic_points = kwargs.get('civic_points')
        self.name = kwargs.get('name')
