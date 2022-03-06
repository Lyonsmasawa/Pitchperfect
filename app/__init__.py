from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from config import config_options
from flask_login import LoginManager

#create instance
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):

    #create app instance
    app = Flask(__name__)

    #configuration
    app.config.from_object(config_options[config_name])

    #blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

    #initialize extensions
    db.init_app(app)

    return app