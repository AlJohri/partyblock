# -*- coding: utf-8 -*-

import os

from flask import Flask
from . import settings
from . import environment

app = Flask(__name__)
app.config.from_object(settings.config)

# app.config['SOCIAL_FACEBOOK'] = {
#     'consumer_key': os.getenv('FLASK_APP_ID'),
#     'consumer_secret': os.getenv('FLASK_APP_SECRET')
# }

# from flask.ext.social import Social
# from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

from . import models
from . import controllers
from . import routes

# app.config['SECURITY_POST_LOGIN'] = '/profile'

# from .models import db, User, Role, Connection

# Security(app, SQLAlchemyUserDatastore(db, User, Role))
# Social(app, SQLAlchemyConnectionDatastore(db, Connection))

# Set up logging

import logging

if not app.debug:
    app.logger.setLevel(logging.INFO)
    settings.log_handler.setLevel(logging.INFO)
else:
    app.logger.setLevel(logging.DEBUG)
    settings.log_handler.setLevel(logging.DEBUG)

app.logger.addHandler(settings.log_handler)