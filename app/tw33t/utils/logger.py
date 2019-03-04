import logging


logger_twitter_handle = logging.getLogger(__name__)
logger_twitter_handle.setLevel(logging.DEBUG)
f_handler = logging.FileHandler('twitter_handle.log')
logger_twitter_handle.addHandler(f_handler)
