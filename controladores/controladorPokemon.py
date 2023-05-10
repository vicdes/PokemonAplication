

from telas.tela_pokemon import TelaPokemon
from entidades.pokemon import *
import json

class ControladorSistema():
    #temporário
    pass


class ControladorPokemon():
    
    lista_pokemons = [] #! TENHO QUE DEIXAR FIXA ESSA LISTA

    def __init__(self):
        self.__tela_pokemon = TelaPokemon()
        '''if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema'''
        #self.__controlador_sistema = controlador_sistema
        # * adicionar controlador_sistema: ControladorSistema no init depois
    
    
    def add_pokemon(self, pokemon): # adiciona um pokémon novo a lista de pokémons
        self.lista_pokemons.append(pokemon)

    def add_lista(dict):
        ControladorPokemon.lista_pokemons = dict

    def del_pokemon(self): # ! Fazer LOOP de "deseja remover outro pokemon? " + loop q faça o else ir direto para a função de novo.
        numero_pokemon = self.__tela_pokemon.deletar_pokemon()
        for pokemon in ControladorPokemon.lista_pokemons:
            if pokemon.num == numero_pokemon:
                ControladorPokemon.lista_pokemons.remove(pokemon)
                self.__tela_pokemon.mostra_mensagem(f"O pokemon {pokemon.nome} foi removido do jogo com sucesso.")
                break
        else:
            self.__tela_pokemon.mostra_mensagem("Nenhum pokémon encontrado com esse número. Tente novamente.")
    

    def mostra_pokemons(self):
        nomes_pokemons = [pokemon.nome for pokemon in self.lista_pokemons]
        self.__tela_pokemon.mostrar_pokemons(nomes_pokemons)

    def mostra_tudo(self):
        print(self.lista_pokemons)
        '''for i in self.lista_pokemons:
            print(i['nome'], i['num'], i['hp'], i['ataque'])'''

    def seleciona_pokemon(self):
        pass

    def retornar(self):
        exit() # ! - Temporário, alterar para retornar ao controladorSistema depois.

    def abre_tela(self):
        lista_opcoes = {1: self.add_pokemon, 2: self.del_pokemon, 3: self.mostra_pokemons, 0: self.retornar}

        continua = True
        while continua:
         lista_opcoes[self.__tela_pokemon.tela_opcoes()]()