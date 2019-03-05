
import os
# DEBUG has to be to False in a production enrironment for security reasons
DEBUG = True


TWITTER_TOKEN = os.environ['TWITTER_TOKEN']
TWITTER_TOKEN_SECRET = os.environ['TWITTER_TOKEN_SECRET']
TWITTER_HANDLE_FILENAME_LOG = 'twitter_handle.log'
