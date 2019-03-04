
from flask import Flask
import sys
from flask_cors import CORS

app = Flask(__name__,
            static_folder=".././dist/static",
            template_folder=".././dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

application = app

# Setup the app with the config.py file
app.config.from_object('config')

from tw33t.views import main
