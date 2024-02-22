from dotenv import load_dotenv
from typing import TypedDict, Type
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

class Config(object):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    STD_ERROR_MSG = os.environ.get('STD_ERROR_MSG', 'Internal server error. Please contact support.')

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class TestingConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True

class EnvConfigs(TypedDict):
    development: Type[Config]
    testing: Type[Config]
    production: Type[Config]

ENV_CONFIGS: EnvConfigs = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": Config
}