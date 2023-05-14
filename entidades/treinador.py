from entidades.time import Time

class Treinador:
    def __init__(self, nickname: str, porcentagem_pokedex: float, pokemons_capturados=None, time=None):
        self.__nickname = nickname
        self.__porcentagem_pokedex = porcentagem_pokedex
        self.__time = time or Time()
        self.__pokemons_capturados = pokemons_capturados or []

        self.__ataque_time = 0
        self.__hp_time = 0
        
    def verifica_numero_pokemon_capturado(self, numero_pokemon):
        capturados = [p.num for p in self.__pokemons_capturados]
        return numero_pokemon in capturados

    @property
    def hp_time(self):
        return self.__hp_time

    @hp_time.setter
    def hp_time(self, valor):
        self.__hp_time = valor
   
    @property
    def ataque_time(self):
        return self.__ataque_time
    
    
    @ataque_time.setter
    def ataque_time(self, valor):
        self.__ataque_time = valor

    def calcular_ataque_time(self):
        ataque_time = 0
        for pokemon in self.__time:
            ataque_time += pokemon.ataque
        return ataque_time

    def calcular_hp_time(self):
        hp_time = 0
        for pokemon in self.__time:
            hp_time += pokemon.hp
        return hp_time

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
        self.__porcentagem_pokedex = porcentagem_pokedex

    @time.setter
    def time(self, time: Time):
        if isinstance(time, Time):
            self.__time = time

    def add_pokemon_capturado(self, pokemon_capturado):
        self.__pokemons_capturados.append(pokemon_capturado)
