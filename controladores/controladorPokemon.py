
from exceptions.pokemon_inexistente import PokemonInexistente
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
        try:
            pokemon = self.selecionar_pokemon()
            ControladorPokemon.lista_pokemons.remove(pokemon)
            self.__tela_pokemon.mostra_mensagem(f"O pokemon {pokemon.nome} foi removido do jogo com sucesso.")
        
        except PokemonInexistente as e:
            self.__tela_pokemon.mostra_mensagem(e)
            #print deu ruim
        
    def selecionar_pokemon(self):
        #implementar -> chamar tela Pokemon pedindo para usuario digitar num pokemon
        #tratar num pokemon
        #retornar pokemon
        num_pokemon = self.__tela_pokemon.seleciona_pokemon_numero()
        for pokemon in self.lista_pokemons:
            if pokemon.num == num_pokemon:
                return pokemon
        
        raise PokemonInexistente(num_pokemon)
        #self.__tela_pokemon.mostra_mensagem("Código de pokémon inválido!")
        #return None

    def altera_status(self):
            #num_pokemon = self.__tela_pokemon.seleciona_pokemon_numero()
        try:
            pokemon = self.selecionar_pokemon()
            #pokemon = self.selecionar_pokemon(num_pokemon)
            self.__tela_pokemon.mostra_mensagem(f'\nPokemon selecionado:\n     {pokemon.nome} #{pokemon.num}, {pokemon.hp}HP, {pokemon.ataque} Ataque')
            novo_hp = self.__tela_pokemon.le_num_inteiro("\nDigite o novo valor de HP: ")
            novo_ataque = self.__tela_pokemon.le_num_inteiro("Digite o novo valor de ataque: ")
            
            
            pokemon.hp = novo_hp
            pokemon.ataque = novo_ataque
            self.__tela_pokemon.mostra_mensagem(f'\nPokemon selecionado com seus atributos alterados:\n     {pokemon.nome} #{pokemon.num}, {pokemon.hp}HP, {pokemon.ataque} Ataque')
        
        except PokemonInexistente as e:
            self.__tela_pokemon.mostra_mensagem(e)
            
    def mostra_pokemons(self):
        pokemons = ControladorPokemon.lista_pokemons
        nomes_e_nums = []
        for pokemon in pokemons:
            nomes_e_nums.append((pokemon.nome, pokemon.num))
        self.__tela_pokemon.mostrar_pokemons(nomes_e_nums)


    #def mostra_tudo(self):          #* TESTANDO LOCAL DE MEMÓRIA DA LISTA
    #    print(self.lista_pokemons)
    #    '''for i in self.lista_pokemons:
    #        print(i['nome'], i['num'], i['hp'], i['ataque'])'''

    def retornar(self):
        exit() # ! - Temporário, alterar para retornar ao controladorSistema depois.

    def abre_tela(self):
        lista_opcoes = {1: self.add_pokemon, 2: self.del_pokemon, 3: self.mostra_pokemons, 4:self.altera_status, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pokemon.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()