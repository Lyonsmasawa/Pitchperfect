from flask import Flask 

def create_app(config_options):

    app = Flask(__name__)

    return app