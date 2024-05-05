from config import ENV_CONFIGS
from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    # If you don't set the ENVIRONMENT env variable, or if you set it to an invalid
    # value,the app is going to run in production environment.
    environment = os.environ.get("ENVIRONMENT", default="production")
    config_obj = ENV_CONFIGS.get(environment) or ENV_CONFIGS["production"]
    app.config.from_object(config_obj)

    from app.domains.posts import bp as posts_bp

    app.register_blueprint(posts_bp)

    return app
