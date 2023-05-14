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

    def get_pokemons_capturados(self):
        return self.__pokemons_capturados
    
    def captura_pokemon(self, pokemon):
        if pokemon in self.__pokemons_capturados:
            print(f"Você já capturou o {pokemon.nome} antes!")
        else:
            self.__pokemons_capturados.append(pokemon)
            print(f"\nParabéns, você capturou o {pokemon.nome}!")

    def mostrar_pokemons_capturados(self):
        if self.__pokemons_capturados:
            print("Pokémons capturados:")
            for pokemon in self.__pokemons_capturados:
                print(pokemon.nome)
        else:
            print("Nenhum Pokémon foi capturado ainda.")

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

    def calcular_hp_time(self):
        hp_time = 0
        for pokemon in self.__time.lista_pokemon:
            hp_time += pokemon.hp
        return hp_time

    def calcular_ataque_time(self):
        ataque_time = 0
        for pokemon in self.__time.lista_pokemon:
            ataque_time += pokemon.ataque
        return ataque_time

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

    def restaurar_hp_time(self):
        self.__hp_time = self.calcular_hp_time()

    @porcentagem_pokedex.setter
    def porcentagem_pokedex(self, porcentagem_pokedex: float):
        self.__porcentagem_pokedex = porcentagem_pokedex

    @time.setter
    def time(self, time: Time):
        if isinstance(time, Time):
            self.__time = time

    def add_pokemon_capturado(self, pokemon_capturado):
        self.__pokemons_capturados.append(pokemon_capturado)