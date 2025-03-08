from app.interfaces.pokeapi import PokeApiInterface


class PokemonInfoService:
    def __init__(self):
        self.pokeapi_interface = PokeApiInterface()

    def get_pokemon_info(self, pokemon_name):
        pokemon_info = {}

        pokemon_info_response = self.pokeapi_interface.get_pokemon_general_info_by_name( # noqa
            pokemon_name)

        if not pokemon_info_response:
            return False

        pokemon_info['abilities'] = self.get_abilities(pokemon_info_response)
        pokemon_info['base_experience'] = self.get_base_experience(
            pokemon_info_response)
        pokemon_info['cries'] = self.get_cries(pokemon_info_response)
        pokemon_info['height'] = self.get_height(pokemon_info_response)
        pokemon_info['name'] = self.get_name(pokemon_info_response)
        pokemon_info['sprites'] = self.get_sprites(pokemon_info_response)
        pokemon_info['stats'] = self.get_stats(pokemon_info_response)
        pokemon_info['types'] = self.get_types(pokemon_info_response)
        pokemon_info['weight'] = self.get_weight(pokemon_info_response)

        return pokemon_info

    def get_abilities(self, pokemon_info_response):
        abilities = pokemon_info_response.get('abilities')
        abilities_names = []

        [abilities_names.append(a.get('ability').get('name')) for a in abilities] # noqa5    

        return abilities_names

    def get_base_experience(self, pokemon_info_response):
        return str(pokemon_info_response.get('base_experience'))

    def get_cries(self, pokemon_info_response):
        return pokemon_info_response.get('cries').get('latest')

    def get_height(self, pokemon_info_response):
        return str(pokemon_info_response.get('height'))

    def get_name(self, pokemon_info_response):
        return pokemon_info_response.get('name')

    def get_sprites(self, pokemon_info_response):
        sprites = []
        for _, value in pokemon_info_response.get('sprites').items():
            if value and type(value) is str:
                sprites.append(value)
        return sprites

    def get_stats(self, pokemon_info_response):
        stats_dict = {}
        stats = pokemon_info_response.get('stats')
        for stat in stats:
            stats_dict[stat.get('stat').get('name')] = str(
                stat.get('base_stat'))

        return stats_dict

    def get_types(self, pokemon_info_response):
        types = []
        for type_ in pokemon_info_response.get('types'):
            types.append(type_.get('type').get('name'))

        return types

    def get_weight(self, pokemon_info_response):
        return str(pokemon_info_response.get('weight'))
