
import json
from controladores.controlador_pokemon import *

with open('populacao_pokemons.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# acessa a lista de pokémons do JSON
pokemons_json = dados['pokemons']

# instancia propriamente o pokemon com as informações do JSON e o objeto da classe Tipo
for pokemon_json in pokemons_json:
    #tipo_json = pokemon_json['tipo']
    #tipo = Tipo(tipo_json['nome'], tipo_json['fraquezas'], tipo_json['vantagens'])
    pokemon = Pokemon(pokemon_json['nome'], pokemon_json['num'], pokemon_json['hp'], pokemon_json['ataque'])
    ControladorPokemon.add_lista(pokemon)


#testando tela pokemon
controlador_pokemon = ControladorPokemon()

controlador_pokemon.abre_tela()

