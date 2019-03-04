
from flask import Flask
import sys

app = Flask(__name__,
            static_folder=".././dist/static",
            template_folder=".././dist")
application = app

# Setup the app with the config.py file
app.config.from_object('config')

from tw33t.views import main
