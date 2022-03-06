class Config:
    pass

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