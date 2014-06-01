# -*- coding: utf-8 -*-

from .. import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class BaseModel(object):

    def to_dict(self):
        d = {}
        for column in self.__table__.columns:
            val = getattr(self, column.name)
            d[column.name] = val
        return d

from app.models.user import User
from app.models.issue import Issue
from app.models.reporter import Reporter
from app.models.connection import Connection
