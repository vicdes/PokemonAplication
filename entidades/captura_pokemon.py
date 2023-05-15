class CapturaPokemon:
    def __init__(self, treinador):
        self.__treinador = treinador
        self.__oponente = None

    @property
    def treinador(self):
        return self.__treinador

    @property
    def oponente(self):
        return self.__oponente

    @treinador.setter
    def treinador(self, treinador):
        self.__treinador = treinador

    @oponente.setter
    def oponente(self, oponente):
        self.__oponente = oponente

#talvez isso abaixo fosse uma melhor representação da classe capturaPokemon, mas não sobra tempo
#consigo alterar no trabalho 2. acredito que ficaria até melhor assim.
'''class CapturaPokemon:
    def __init__(self, treinador, pokemons_time, pokemon_oponente, resultado_batalha, resultado_captura):
        self.treinador = treinador
        self.pokemons_time = pokemons_time
        self.pokemon_oponente = pokemon_oponente
        self.resultado_batalha = resultado_batalha
        self.resultado_captura = resultado_captura'''

