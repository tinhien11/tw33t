from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
import json, requests, datetime, sys, os, uuid, re, time
from flask.views import MethodView


@app.route("/", methods=['GET'])
def index():

    return render_template('index.html')


class UserAPI(MethodView):
    def get(self, twitter_handle=None):
        return jsonify()


app.add_url_rule('/users/<string:twitter_handle>', view_func=UserAPI.as_view('users'))
