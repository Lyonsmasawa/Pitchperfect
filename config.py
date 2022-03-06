class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:passdb@localhost/pitches'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    pass

config_options = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'tests': TestConfig
}