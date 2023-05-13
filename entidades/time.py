class Time:
    def __init__(self):
        self.__lista_pokemons = []

    @property
    def lista_pokemon(self):
        return self.__lista_pokemons

    @lista_pokemon.setter
    def lista_pokemon(self, pokemon):
        self.__lista_pokemons.append(pokemon)
