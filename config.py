from dotenv import load_dotenv
from typing import TypedDict, Type
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config(object):
    ENV = "production"
    DEBUG = False
    TESTING = False
    STD_ERROR_MSG = os.environ.get(
        "STD_ERROR_MSG", "Internal server error. Please contact support."
    )

    # SQLAlchemy:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URI", "sqlite:///" + os.path.join(BASEDIR, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True


class TestingConfig(Config):
    ENV = "development"
    TESTING = True


class EnvConfigs(TypedDict):
    development: Type[Config]
    test: Type[Config]
    production: Type[Config]


ENV_CONFIGS: EnvConfigs = {
    "development": DevelopmentConfig,
    "test": TestingConfig,
    "production": Config,
}
