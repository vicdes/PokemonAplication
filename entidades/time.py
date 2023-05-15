class Time:
    def __init__(self, lista_pokemons=None):
        self.__lista_pokemons = lista_pokemons or []

    @property
    def lista_pokemons(self):
        return self.__lista_pokemons

    @lista_pokemons.setter
    def lista_pokemons(self, pokemon):
        self.__lista_pokemons.append(pokemon)


