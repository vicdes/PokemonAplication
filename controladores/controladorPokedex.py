import sys
sys.path.append('C:\\Users\\Jose\\Desktop\\Pokémon\\PokemonAplication')

from telas.tela_pokedex import TelaPokedex
from entidades.pokedex import *



class ControladorPokedex:
    def __init__(self):   #posteriomente recebe controlador_sistema
        self.__tela_pokedex = TelaPokedex()
        #self.__controlador_sistema = controlador_sistema

    #? Acho que não será necessária essa parte mais.
    '''def calcular_porcentagem_capturados(self):
        porcentagem_capturados = Pokedex.calcular_porcentagem_capturados()
        self.__tela_pokedex.mostrar_porcentagem_capturados(porcentagem_capturados)'''
    
    def calcular_porcentagem_capturados(self):
        total_pokemons = len(Pokemon.lista_pokemons)
        total_capturados = len(Pokemon.lista_pokemons_capturados)

        porcentagem_capturados = (total_capturados / total_pokemons) * 100
        
        self.__tela_pokedex.mostrar_porcentagem_capturados(porcentagem_capturados)

    def nome_pokemons_capturados(self):
        nomes = []

        for pokemon in Pokemon.lista_pokemons_capturados:
            nomes.append(pokemon.nome)

        self.__tela_pokedex.mostrar_nome_pokemons_capturados(nomes)


    def retornar(self):
        exit() # ! - Temporário, alterar para retornar ao controladorSistema depois.

    def abre_tela(self):
        lista_opcoes = {1: self.calcular_porcentagem_capturados, 2: self.nome_pokemons_capturados, 0: self.retornar}

        continua = True
        while continua:
         lista_opcoes[self.__tela_pokedex.tela_opcoes()]()