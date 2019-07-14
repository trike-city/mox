from flask import Blueprint, request

blueprint = Blueprint('players', __name__)


@blueprint.route('/players', methods=('POST',))
def create():
    return '', 201
