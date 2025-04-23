import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'defaultsecretkey')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://localhost:5432/poll_app')

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'

