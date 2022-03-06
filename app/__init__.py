from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import config_options

#create instance
db = SQLAlchemy()

def create_app(config_name):

    #create app instance
    app = Flask(__name__)

    #configuration
    app.config.from_object(config_options[config_name])

    #blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #initialize extensions
    db.init_app(app)

    return app