from flask import Flask, Blueprint, jsonify, request

from app.services.pokemon_info import PokemonInfoService


pokemon = Blueprint('pokemon', __name__)

pokemon_info_service = PokemonInfoService()


@pokemon.get('/')
def get_pokemon_info():
    pokemon = request.args.get('pokemon_name')

    pokemon_info = pokemon_info_service.get_pokemon_info(pokemon)

    if not pokemon_info:
        return jsonify(msg=f'Pokemon {pokemon} not found :(')
    return pokemon_info


def init(app: Flask):
    app.register_blueprint(pokemon)
