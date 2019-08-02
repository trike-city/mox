from flask import Blueprint, request, make_response, jsonify


class Controller:
    def register(self, app):
        bp = Blueprint(self.resource, __name__)

        if hasattr(self, 'create'):
            @bp.route(f'/{self.resource}', methods=('POST',))
            def create():
                return self.create(request)

        app.register_blueprint(bp)

    def response(self, body, status):
        return make_response(jsonify(body), status)
