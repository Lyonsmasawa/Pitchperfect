from distutils.command.config import config
from flask import Flask 
from config import config_options

def create_app(config_name):

    #create app instance
    app = Flask(__name__)

    #configuration
    app.config.from_object(config_options[config_name])


    return app