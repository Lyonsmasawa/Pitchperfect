import imp
from operator import imod
from config import config_options

from flask import Flask

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])