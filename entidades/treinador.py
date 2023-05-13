from entidades.time import Time

class Treinador:
    def __init__(self, nickname: str, porcentagem_pokedex: float):
        self.__nickname = nickname
        self.__porcentagem_pokedex = porcentagem_pokedex
        self.__time = Time()
        self.__pokemons_capturados = []

        self.__ataque_equipe = 0
        self.__hp_equipe = 0
        
    def verifica_numero_pokemon_capturado(self, numero_pokemon):
        capturados = [p.num for p in self.__pokemons_capturados]
        return numero_pokemon in capturados

    @property
    def hp_equipe(self):
        return self.__hp_equipe

    @hp_equipe.setter
    def hp_equipe(self, valor):
        self.__hp_equipe = valor
   
    @property
    def ataque_equipe(self):
        return self.__ataque_equipe
    
    
    @ataque_equipe.setter
    def ataque_equipe(self, valor):
        self.__ataque_equipe = valor

    def calcular_ataque_equipe(self):
        ataque_equipe = 0
        for pokemon in self.__equipe:
            ataque_equipe += pokemon.ataque
        return ataque_equipe
    
    
    def calcular_hp_equipe(self):
        hp_equipe = 0
        for pokemon in self.__equipe:
            hp_equipe += pokemon.hp
        return hp_equipe

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
