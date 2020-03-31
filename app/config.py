import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('...') / '.env'

load_dotenv(dotenv_path=env_path)

class DevelopmentConfiguration(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI', 'sqlite:///todo.db')
    PROPAGATE_EXCEPTION = True

class ProductionConfiguration(object):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')
    PROPAGATE_EXCEPTION = True

app_config = {
    'development': DevelopmentConfiguration,
    'production': ProductionConfiguration
}