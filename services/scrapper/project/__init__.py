import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_debugtoolbar import DebugToolbarExtension


# instantiate extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()



def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)


    

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    # register blueprints
    from project.api.scrapper import scrapper_blueprint
    app.register_blueprint(scrapper_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
