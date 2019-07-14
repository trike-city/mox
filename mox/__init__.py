import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    __configure_app(app, test_config)
    __register_routes(app)
    __create_app_folder(app)
    return app


def __configure_app(app, test_config):
    app.config['SECRET_KEY'] = 'dev'
    app.config['DATABASE'] = os.path.join(app.instance_path, 'flask.sqlite')

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


def __register_routes(app):
    from mox.controllers import players_controller
    app.register_blueprint(players_controller.blueprint)


def __create_app_folder(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
