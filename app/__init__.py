from config import ENV_CONFIGS
from flask import Flask
import os

from app.extensions import db


def create_app():
    app = Flask(__name__)

    # determine environment:

    # If you don't set the ENVIRONMENT env variable, or if you set it to an invalid
    # value,the app is going to run in production environment.
    environment = os.environ.get("ENVIRONMENT", default="production")
    config_obj = ENV_CONFIGS.get(environment) or ENV_CONFIGS["production"]
    app.config.from_object(config_obj)

    # initialize extensions:

    db.init_app(app)

    # register blueprints:

    from app.domains.posts import bp as posts_bp

    app.register_blueprint(posts_bp)

    from app.domains.users import bp as users_bp

    app.register_blueprint(users_bp)

    from app.domains.error import bp as error_bp

    app.register_blueprint(error_bp)

    return app
