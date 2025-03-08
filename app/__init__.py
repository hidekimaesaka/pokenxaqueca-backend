from flask import Flask

from flask_cors import CORS

from app.routes import pokemon


def create_app():
    app = Flask(__name__)
    CORS(app)

    # routes
    pokemon.init(app)

    return app
