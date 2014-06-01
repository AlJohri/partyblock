# -*- coding: utf-8 -*-

from . import app
from .tasks import celery
from flask import render_template, request, redirect

from flask.ext.login import login_required

# from flask.ext.cors import cross_origin
# @app.after_request 
# @cross_origin() #allow all origins all methods everywhere in the app
# def after(response): return response

@app.route('/map')
def map():
	return render_template(
		'map.html',
		content='Map Page'
		)

# @app.route('/login')
# def login():
# 	return render_template(
# 		'login.html',
# 		content='Login Page'
# 		)

# @app.route('/profile')
# @login_required
# def profile():
#     return render_template(
#         'profile.html',
#         content='Profile Page',
#         facebook_conn=social.facebook.get_connection())

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print path
    return render_template('index.html')