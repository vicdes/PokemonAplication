
'''from controladores.controladorPokedex import *
from controladores.controladorTime import *'''
from controladores.controladorPokemon import *

'''controlador_pokedex = ControladorPokedex()

controlador_pokedex.abre_tela()'''

'''controlador_time = ControladorTime()

controlador_time.abre_tela()'''

# define a list of dictionaries with the Pokemon attributes
pokemon_testes = [
    {"nome": "Bulbasaur", "num": 1, "hp": 45, "ataque": 49},
    {"nome": "Charmander", "num": 4, "hp": 39, "ataque": 52},
    {"nome": "Squirtle", "num": 7, "hp": 44, "ataque": 48},
    {"nome": "Pidgey", "num": 16, "hp": 40, "ataque": 45},
    {"nome": "Jigglypuff", "num": 39, "hp": 115, "ataque": 45},
    {"nome": "Pikachu", "num": 25, "hp": 35, "ataque": 55},
    {"nome": "Geodude", "num": 74, "hp": 40, "ataque": 80},
    {"nome": "Abra", "num": 63, "hp": 25, "ataque": 20},
    {"nome": "Magikarp", "num": 129, "hp": 20, "ataque": 10},
    {"nome": "Diglett", "num": 50, "hp": 10, "ataque": 55},
]

# instantiate the ControladorPokemon class
controlador_pokemon = ControladorPokemon()

# use a loop to create Pokemon instances and add them to the lista_pokemons list
for pokemon in pokemon_testes:
    pokemon = Pokemon(**pokemon)
    controlador_pokemon.add_pokemon(pokemon)

# print the updated lista_pokemons list
#print(ControladorPokemon.lista_pokemons)



controlador_pokemon = ControladorPokemon()

controlador_pokemon.abre_tela()

