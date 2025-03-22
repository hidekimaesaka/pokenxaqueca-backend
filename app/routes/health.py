from flask import Flask, Blueprint, jsonify


health = Blueprint('health', __name__)


@health.get('/')
def health_check():
    return jsonify(msg='ok')


def init(app: Flask):
    return app.register_blueprint(health)
