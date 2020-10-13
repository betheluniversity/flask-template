# python
import os
import sentry_sdk

# flask packages
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

# extensions
from .extensions import db


def create_app():

    _basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize Plugins
    db.init_app(app)

    # sentry
    sentry_sdk.init(
        dsn=app.config.get('SENTRY_URL'),
        integrations=[FlaskIntegration(), SqlalchemyIntegration()]
    )

    # routes
    with app.app_context():
        from .views import bp
        from .views import subfolder_bp
        app.register_blueprint(bp)
        app.register_blueprint(subfolder_bp)

    return app
