# -*- coding: utf-8 -*-

from .. import app
from flask import make_response
from flask.ext.restful import Api

api = Api(app)

#http://www.wiredmonk.me/customizing-flask-restful.html
import json, datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(obj.strftime('%s'))
        return json.JSONEncoder.default(self, obj)

def custom_json_output(data, code, headers=None):
    dumped = json.dumps(data, cls=CustomEncoder)
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp

api.representations.update({
    'application/json': custom_json_output
})

from app.controllers import issue