import os

from flask import Flask


def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    __register_routes(app)
    __create_app_folder(app)
    return app


def __register_routes(app):
    from mox.controllers import players_controller, tournaments_controller
    app.register_blueprint(players_controller.blueprint)
    app.register_blueprint(tournaments_controller.blueprint)


def __create_app_folder(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
