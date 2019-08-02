import os

from flask import Flask
from mox.data import Database
from mox.controllers import PlayersController, tournaments_controller


class Dependencies:
    def __init__(self, config):
        self.config = config
        self.database = Database(config)


def create_app(deps):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(deps.config)
    __register_routes(app, deps)
    __create_app_folder(app)
    return app


def __register_routes(app, deps):
    PlayersController(deps.database).register(app)
    app.register_blueprint(tournaments_controller.blueprint)


def __create_app_folder(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
