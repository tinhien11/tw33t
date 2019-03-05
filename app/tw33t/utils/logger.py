import logging
import os
from tw33t import app


logger_twitter_handle = logging.getLogger(__name__)
logger_twitter_handle.setLevel(logging.DEBUG)

FOLDER_LOGS_PATH = app.root_path + '/logs/'
os.makedirs(FOLDER_LOGS_PATH, exist_ok=True)

f_handler = logging.FileHandler('%s%s' % (FOLDER_LOGS_PATH, app.config['TWITTER_HANDLE_FILENAME_LOG']))
logger_twitter_handle.addHandler(f_handler)
