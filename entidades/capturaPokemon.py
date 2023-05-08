import sys
sys.path.append('C:\\Users\\Jose Eduardo\\Desktop\\Pokémon\\PokemonAplication')

from random import *
from PokémonOLD import *
from entidades.time import Time

class CapturaPokemon():
    def __init__(self, time_treinador, oponente):
        self.__time_treinador = time_treinador
        self.__oponente = oponente
        self.__pokemon_atual = None
        self.__turno = 1
        self.__fim_batalha = False

    def aleatoriza_pokemon_oponente(self):
        #random_pokemon = choice(Pokemon.lista_pokemons)
        print('\n[TESTE] - Seu oponente será: ')
        print()

        random_pokemon = choice(Pokemon.lista_pokemons)
        numero_pokemon = random_pokemon.numero
        #print(numero_pokemon)
        random_pokemon.dados_pokemon_por_numero(numero_pokemon)

    def inicializa_batalha(self, time, oponente):
        self.aleatoriza_pokemon_oponente()
        self.selecionar_pokemon()
        #self.trocar_pokemon()
        #self.fugir()
        self.atacar()
        

    def fugir(self):
        # ! É necessário implementar a classe Treinador e vincular ela. Aguardar Vic.
        print(f"{self.__time_treinador.nome} fugiu da batalha!")
        self.__fim_batalha = True
    

    def selecionar_pokemon(self):
        self.__time_treinador.mostrar_time()
        escolha = int(input("Escolha o número do pokemon que deseja iniciar a batalha: "))
        self.__pokemon_atual = self.__time_treinador.get_pokemon_por_numero(escolha)
        if self.__pokemon_atual:
            print(f"Você selecionou {self.__pokemon_atual.nome} ({self.__pokemon_atual.hp} HP).")
        else:
            print(f"Não foi encontrado nenhum pokemon com o número {escolha} no seu time.")
            self.selecionar_pokemon()


    def trocar_pokemon(self):
        self.__time_treinador.mostrar_time()
        print(f'\n[!] Seu pokémon atual é {self.__pokemon_atual.nome}')
        numero_pokemon = int(input(f"\nEscolha um pokémon para substituir o {self.__pokemon_atual.nome}: "))
        pokemon = self.__time_treinador.get_pokemon_por_numero(numero_pokemon)

        while pokemon is None:
            print("Número de pokémon inválido!")
            numero_pokemon = int(input("Escolha outro pokémon: "))
            pokemon = self.__time_treinador.get_pokemon_por_numero(numero_pokemon)

        while pokemon.numero == self.__pokemon_atual.numero:
            print("Você não pode selecionar o mesmo pokémon que já está em batalha!")
            numero_pokemon = int(input("Escolha outro pokémon: "))
            pokemon = self.__time_treinador.get_pokemon_por_numero(numero_pokemon)

        self.__pokemon_atual = pokemon
        print(f"Você selecionou {self.__pokemon_atual.nome} ({self.__pokemon_atual.hp} HP).")





'''captura = CapturaPokemon()

captura.aleatoriza_pokemon_oponente()'''
time = Time()
time.add_pokemon_time(25)
time.add_pokemon_time(1)
#time_treinador = Time(...)

oponente = Pokemon.lista_pokemons[0]
time.mostrar_time()
batalha = CapturaPokemon(time, oponente)
batalha.inicializa_batalha(time, oponente)