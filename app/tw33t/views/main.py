from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from flask.views import MethodView
from tw33t.utils.twitter_client import twitter11, TwitterHTTPError
from tw33t.utils.logger import logger_twitter_handle
import requests


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


class TweetsAPI(MethodView):
    def get(self):
        twitter_handle = request.args.get('user')
        count = request.args.get('count', 10)
        try:
            logger_twitter_handle.info(twitter_handle)
            twitters = twitter11.statuses.user_timeline(screen_name=twitter_handle, count=count)
            return jsonify(twitters)
        except TwitterHTTPError as err:
            abort(err.e.code)
        except Exception as err:
            abort(500)


app.add_url_rule('/api/v1/tweets/', view_func=TweetsAPI.as_view('tweets'))
