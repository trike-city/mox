from mox.models import Tournament
from flask import Blueprint, request, make_response, jsonify

blueprint = Blueprint('tournaments', __name__)


@blueprint.route('/tournaments', methods=('POST',))
def create():
    tournament = Tournament.create(request.json)
    return make_response(jsonify(tournament.serialize()), 201)
