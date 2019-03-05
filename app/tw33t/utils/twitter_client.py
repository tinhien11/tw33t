import os
from tw33t import app
from twitter import Twitter, OAuth, TwitterHTTPError
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET

oauth = OAuth(app.config['TWITTER_TOKEN'], app.config['TWITTER_TOKEN_SECRET'], CONSUMER_KEY, CONSUMER_SECRET)

twitter11 = Twitter(domain='api.twitter.com',
                    auth=oauth,
                    api_version='1.1')
