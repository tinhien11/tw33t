from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from flask.views import MethodView
from tw33t.utils.twitter_client import twitter11


@app.route("/", methods=['GET'])
def index():

    return render_template('index.html')


class UserAPI(MethodView):
    def get(self, twitter_handle=None):
        twitters = twitter11.statuses.user_timeline(screen_name=twitter_handle)
        return jsonify(twitters)


app.add_url_rule('/users/<string:twitter_handle>', view_func=UserAPI.as_view('users'))
