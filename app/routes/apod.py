from flask import Flask, Blueprint, redirect

from app.interfaces.nasa import NasaInterface


apod = Blueprint('apod', __name__)


nasa_interface = NasaInterface()


@apod.get('/nasa')
def get_apod():
    apod = nasa_interface.get_apod()
    return redirect(apod)


def init(app: Flask):
    return app.register_blueprint(apod)
