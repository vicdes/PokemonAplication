import random
from PokémonOLD import * 

class Treinador:
    pass

class Time:
    pass

class Pokedex:
    #TODO - CÓDIGO TEMPORÁRIO: Lembrar de adaptar ao código da Vic
    def __init__(self, lista_pokemons, lista_pokemons_capturados):
        self.lista_pokemons = lista_pokemons
        self.lista_pokemons_capturados = lista_pokemons_capturados

    def calcular_porcentagem_capturados(self):
        total_pokemons = len(self.lista_pokemons)
        total_capturados = len(self.lista_pokemons_capturados)

        porcentagem_capturados = (total_capturados / total_pokemons) * 100
        return porcentagem_capturados    



class CapturaPokemon:
    def __init__(self, treinador: Treinador, oponente: Pokemon, time_treinador: Time, pokedex: Pokedex):
        self.__treinador = treinador
        self.__oponente = None
        self.__time_treinador = time_treinador
        self.__pokedex = pokedex

    def aleatoriza_pokemon(self):
        self.oponente = random.choice(self.pokemon.pokemons)


pokedex = Pokedex(Pokemon.lista_pokemons, Pokemon.lista_pokemons_capturados)

porcentagem_capturados = pokedex.calcular_porcentagem_capturados()
print(f'Porcentagem de Pokémons capturados: {porcentagem_capturados:.2f}%')