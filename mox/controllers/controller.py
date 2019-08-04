from flask import Blueprint, request, make_response, jsonify


class Controller:
    @property
    def resource_name(self):
        class_name = self.__class__.__name__
        return class_name[:-len('Controller')].lower()

    def register(self, app):
        bp = Blueprint(self.resource_name, __name__)

        if hasattr(self, 'create'):
            @bp.route(f'/{self.resource_name}', methods=('POST',))
            def create():
                return self.create(request)

        app.register_blueprint(bp)

    def response(self, body, status):
        return make_response(jsonify(body), status)
