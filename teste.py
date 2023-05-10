
from controladores.controladorPokemon import *

# ! Ambos abaixo foram descontinuados
'''controlador_pokedex = ControladorPokedex()

controlador_pokedex.abre_tela()'''

'''controlador_time = ControladorTime()

controlador_time.abre_tela()'''

pokemon_testes = [
    {"nome": "Bulbasaur", "num": 1, "hp": 45, "ataque": 49},
    {"nome": "Charmander", "num": 4, "hp": 39, "ataque": 52},
    {"nome": "Squirtle", "num": 7, "hp": 44, "ataque": 48},
    {"nome": "Mankey", "num": 56, "hp": 40, "ataque": 80},
    {"nome": "Pidgey", "num": 16, "hp": 40, "ataque": 45},
    {"nome": "Jigglypuff", "num": 39, "hp": 115, "ataque": 45},
    {"nome": "Pikachu", "num": 25, "hp": 35, "ataque": 55},
    {"nome": "Geodude", "num": 74, "hp": 40, "ataque": 80},
    {"nome": "Abra", "num": 63, "hp": 25, "ataque": 20},
    {"nome": "Magikarp", "num": 129, "hp": 20, "ataque": 10},
    {"nome": "Diglett", "num": 50, "hp": 10, "ataque": 55},
    {"nome": "Caterpie", "num": 10, "hp": 45, "ataque": 30},
    {"nome": "Ekans", "num": 23, "hp": 35, "ataque": 60},
    {"nome": "Sandshrew", "num": 27, "hp": 50, "ataque": 75},
    {"nome": "Nidoran♀", "num": 29, "hp": 55, "ataque": 47},
    {"nome": "Nidoran♂", "num": 32, "hp": 46, "ataque": 57},
    {"nome": "Clefairy", "num": 35, "hp": 70, "ataque": 45},
    {"nome": "Vulpix", "num": 37, "hp": 38, "ataque": 41},
    {"nome": "Zubat", "num": 41, "hp": 40, "ataque": 45},
    {"nome": "Golbat", "num": 42, "hp": 75, "ataque": 80},
    {"nome": "Oddish", "num": 43, "hp": 45, "ataque": 50},
    {"nome": "Paras", "num": 46, "hp": 35, "ataque": 70},
    {"nome": "Venonat", "num": 48, "hp": 60, "ataque": 55},
    {"nome": "Diglett", "num": 50, "hp": 10, "ataque": 55},
    {"nome": "Meowth", "num": 52, "hp": 40, "ataque": 45},
    {"nome": "Psyduck", "num": 54, "hp": 50, "ataque": 52}
]

controlador_pokemon = ControladorPokemon()

for pokemon in pokemon_testes:
    pokemon = Pokemon(**pokemon)
    controlador_pokemon.add_pokemon(pokemon)

#print(ControladorPokemon.lista_pokemons)

#testando tela pokemon
controlador_pokemon = ControladorPokemon()

controlador_pokemon.abre_tela()

