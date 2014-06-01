# -*- coding: utf-8 -*-

from . import app
from .tasks import celery
from flask import render_template, request, redirect

# from flask.ext.cors import cross_origin
# @app.after_request 
# @cross_origin() #allow all origins all methods everywhere in the app
# def after(response): return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print path
    return render_template('index.html')