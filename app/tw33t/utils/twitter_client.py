import os
from twitter import Twitter, OAuth, TwitterHTTPError
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET

oauth = OAuth(os.environ['TWITTER_TOKEN'], os.environ['TWITTER_TOKEN_SECRET'], CONSUMER_KEY, CONSUMER_SECRET)

twitter11 = Twitter(domain='api.twitter.com',
                    auth=oauth,
                    api_version='1.1')
