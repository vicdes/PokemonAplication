class CapturaPokemon:
    def __init__(self, id, treinador, pokemons_time, pokemon_oponente, resultado_batalha, resultado_captura):
        self.__id = id
        self.__treinador = treinador
        self.__pokemons_time = pokemons_time
        self.__pokemon_oponente = pokemon_oponente
        self.__resultado_batalha = resultado_batalha
        self.__resultado_captura = resultado_captura

    @property
    def id(self):
        return self.__id

    @property
    def treinador(self):
        return self.__treinador

    @property
    def pokemons_time(self):
        return self.__pokemons_time

    @property
    def pokemon_oponente(self):
        return self.__pokemon_oponente

    @property
    def resultado_batalha(self):
        return self.__resultado_batalha

    @property
    def resultado_captura(self):
        return self.__resultado_captura

    @id.setter
    def id(self, id):
        self.__id = id

    @treinador.setter
    def treinador(self, treinador):
        self.__treinador = treinador

    @pokemons_time.setter
    def pokemons_time(self, pokemons_time):
        self.__pokemons_time = pokemons_time

    @pokemon_oponente.setter
    def pokemon_oponente(self, pokemon_oponente):
        self.__pokemon_oponente = pokemon_oponente

    @resultado_batalha.setter
    def resultado_batalha(self, resultado_batalha):
        self.__resultado_batalha = resultado_batalha

    @resultado_captura.setter
    def resultado_captura(self, resultado_captura):
        self.__resultado_captura = resultado_captura


#talvez isso abaixo fosse uma melhor representação da classe capturaPokemon, mas não sobra tempo
#consigo alterar no trabalho 2. acredito que ficaria até melhor assim.
'''class CapturaPokemon:
    def __init__(self, treinador, pokemons_time, pokemon_oponente, resultado_batalha, resultado_captura):
        self.treinador = treinador
        self.pokemons_time = pokemons_time
        self.pokemon_oponente = pokemon_oponente
        self.resultado_batalha = resultado_batalha
        self.resultado_captura = resultado_captura'''

