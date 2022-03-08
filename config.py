import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:passdb@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com' #smtp server
    MAIL_PORT = 587 #gmail smtp server port
    MAIL_USE_TLS = True #enables a transport layer security to secure emails when sending
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") #these are yours
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations im
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:passdb@localhost/pitches-test'

class TestConfig(Config):
    pass

config_options = {
    'production': ProdConfig,
    'development': DevConfig,
    'tests': TestConfig
}