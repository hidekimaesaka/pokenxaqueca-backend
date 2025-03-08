from requests import get


class PokeApiInterface:
    def __init__(self):
        self.pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/$pokemon_name/'

    def get_pokemon_general_info_by_name(self, name):
        url = self.pokeapi_url.replace('$pokemon_name', name)

        response = get(url)

        if not response.ok:
            return False

        return response.json()
