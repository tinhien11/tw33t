import logging
from tw33t import app


logger_twitter_handle = logging.getLogger(__name__)
logger_twitter_handle.setLevel(logging.DEBUG)
f_handler = logging.FileHandler(app.config['TWITTER_HANDLE_FILENAME_LOG'])
logger_twitter_handle.addHandler(f_handler)
