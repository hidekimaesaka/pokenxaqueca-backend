from flask import Flask

from app.routes import health, apod


def create_app():
    app = Flask(__name__)

    # routes
    health.init(app)
    apod.init(app)

    return app
