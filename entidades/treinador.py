class Treinador:
    def __init__(self, nickname: str, porcentagem_pokedex: float, time):
        if isinstance(nickname, str):
            self.__nickname = nickname
        if isinstance(porcentagem_pokedex, float):
            self.__porcentagem_pokedex = porcentagem_pokedex
        #if isinstance(time, Time):
            self.__time = time
        self.__pokemons_capturados = []

    @property
    def nickname(self):
        return self.__nickname

    @property
    def porcentagem_pokedex(self):
        return self.__porcentagem_pokedex

    @property
    def time(self):
        return self.__time

    @property
    def pokemons_capturados(self):
        return self.__pokemons_capturados

    @nickname.setter
    def nickname(self, nickname: str):
        if isinstance(nickname, str):
            self.__nickname = nickname

    @porcentagem_pokedex.setter
    def porcentagem_pokedex(self, porcentagem_pokedex: float):
        if isinstance(porcentagem_pokedex, float):
            self.__porcentagem_pokedex

    @time.setter
    def time(self, time: Time):
        if isinstance(time, Time):
            self.__time = time

    def add_pokemon_capturado(self, pokemon_capturado: PokemonCapturado):
        if isinstance(pokemon_capturado, PokemonCapturado):
            self.__pokemons_capturados.append(pokemon_capturado)
