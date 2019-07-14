from flask import Blueprint, request, make_response, jsonify

blueprint = Blueprint('players', __name__)


@blueprint.route('/players', methods=('POST',))
def create():
    data = request.form
    return make_response(jsonify(data), 201)
