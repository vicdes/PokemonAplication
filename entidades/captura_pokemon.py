from controladores.controlador_pokemon import ControladorPokemon
#from entidades.pokemon import Pokemon
import random

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
    
    def escolher_pokemon_aleatorio(self):
        pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        return pokemon_aleatorio