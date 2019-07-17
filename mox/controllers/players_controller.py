from mox.models import Player
from flask import Blueprint, request, make_response, jsonify

blueprint = Blueprint('players', __name__)


@blueprint.route('/players', methods=('POST',))
def create():
    player = Player.create(request.json)
    return make_response(jsonify(player.serialize()), 201)
