import sys
sys.path.append('C:\\Users\\Jose Eduardo\\Desktop\\Pokémon\\PokemonAplication')

from telas.tela_time import TelaTime
from entidades.time import *

class ControladorTime():
    def __init__(self):
        self.__tela_time = TelaTime()
        #self.__controlador_sistema = controlador_sistema

    def mostrar_pokemons_disponiveis(self):
        #print('DENTRO DA CLASSE TIME')
        for pokemon in Pokemon.lista_pokemons_capturados:
            print()
            print(f"Nome: {pokemon.nome}")
            print(f"Número: {pokemon.numero}")
            '''
            print(f"HP: {pokemon.hp}")
            print(f"Ataque: {pokemon.ataque}")
            print(f"Tipo: {pokemon.tipo.nome}")
            print(f"Fraquezas: {pokemon.tipo.fraquezas}")
            print(f"Vantagens: {pokemon.tipo.vantagens}")
            '''
    
    def time_atual(self):
        if len(self.__time) == 0:
            self.__tela_time.mostra_mensagem('Seu time está vazio. Você deve adicionar pelo menos um (1) pokémon ao seu time.')
            #print('Seu time está vazio. Você deve adicionar pelo menos um (1) pokémon ao seu time.')
        else:
            self.__tela_time.mostra_mensagem('\nSeu time:')
            for pokemon in self.__time:
                #self.__tela_time.mostra_time(f'- {pokemon.nome} #{pokemon.numero}')
                self.__tela_time.mostra_mensagem(f'- {pokemon.nome} #{pokemon.numero}')
                
    def add_pokemon_time(self):
        numero_pokemon = self.__tela_time.add_pokemon
        for pokemon in self.__lista_pokemons_capturados:
            if pokemon.numero == numero_pokemon:
                self.__time.append(pokemon)
                print(f"O pokémon {pokemon.nome} foi adicionado ao time com sucesso.")
                break
        else:
            print("Número de pokémon inválido. Tente outro número.")

    def del_pokemon_time(self, numero_pokemon):
        numero_pokemon = self.__tela_time.deletar_pokemon
        for pokemon in self.__time:
            if pokemon.numero == numero_pokemon:
                self.__time.remove(pokemon)
                # * esse print deve ser feito na tela com a função mostrar_msg()
                # * assim como os outros prints
                #print(f"O pokemon {pokemon.nome} foi removido do seu time com sucesso.")
                self.__tela_time.mostra_mensagem("O pokemon {pokemon.nome} foi removido do seu time com sucesso.")
                break
            else:
                self.__tela_time.mostra_mensagem("Nenhum pokémon encontrado com esse número. Tente novamente.")
                #print('Nenhum pokémon encontrado com esse número. Tente novamente.')
                
    def retornar(self):
        exit() # ! - Temporário, alterar para retornar ao controladorSistema depois.

    def abre_tela(self):
        lista_opcoes = {1: self.time_atual, 2: self.add_pokemon_time, 3: self.del_pokemon_time, 0: self.retornar}

        continua = True
        while continua:
         lista_opcoes[self.__tela_time.tela_opcoes()]()