from mox.models import Round
from flask import Blueprint, request, make_response, jsonify

blueprint = Blueprint('rounds', __name__)


@blueprint.route('/rounds', methods=('POST',))
def create():
    round = Round.create(request.json)
    return make_response(jsonify(round.serialize()), 201)
