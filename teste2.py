import json

from entidades.pokemon import Pokemon
from entidades.tipo_pokemon import TipoPokemon

## Abrir o arquivo JSON e ler o conteúdo
with open("teste_pokemons_com_tipos.json", encoding="utf-8") as arquivo:
    dados_json = arquivo.read()

# Converter JSON para dicionário Python
dados = json.loads(dados_json)

# Criar objetos Pokemon e TipoPokemon
pokemons = []
tipos_pokemon = {}

for pokemon_data in dados["pokemons"]:
    nome = pokemon_data["nome"]
    num = pokemon_data["num"]
    hp = pokemon_data["hp"]
    ataque = pokemon_data["ataque"]
    tipos_data = pokemon_data["tipo"]

    tipos_nome = tipos_data["nome"]
    vantagens = tipos_data["vantagens"]
    fraquezas = tipos_data["fraquezas"]

    tipos = []
    for tipo_nome in tipos_nome:
        tipo = TipoPokemon(tipo_nome, vantagens, fraquezas)
        tipos.append(tipo)
        if tipo_nome not in tipos_pokemon:
            tipos_pokemon[tipo_nome] = tipo

    pokemon = Pokemon(nome, num, hp, ataque, tipos)
    pokemons.append(pokemon)

for pokemon in pokemons:
    print("Nome:", pokemon.nome)
    print("Número:", pokemon.num)
    print("HP:", pokemon.hp)
    print("Ataque:", pokemon.ataque)
    print("Tipos:")
    for tipo in pokemon.tipos:
        print(f"  - {tipo.nome}")
        print("    Vantagens:", tipo.vantagens)
        print("    Fraquezas:", tipo.fraquezas)
    print()

import random
def verificar_vantagem(pokemon1, pokemon2):
    for tipo_pokemon1 in pokemon1.tipos:
        for tipo_pokemon2 in pokemon2.tipos:
            for vantagem in tipo_pokemon1.vantagens:
                if vantagem == tipo_pokemon2.nome:
                    return pokemon1.nome + " tem vantagem sobre " + pokemon2.nome, tipo_pokemon1.vantagens
    for tipo_pokemon2 in pokemon2.tipos:
        for tipo_pokemon1 in pokemon1.tipos:
            for vantagem in tipo_pokemon2.vantagens:
                if vantagem == tipo_pokemon1.nome:
                    return pokemon2.nome + " tem vantagem sobre " + pokemon1.nome, tipo_pokemon2.vantagens
    return None, []

# Selecionar dois pokémons aleatórios
pokemon1 = random.choice(pokemons)
pokemon2 = random.choice(pokemons)

# Exibir as informações dos dois pokémons selecionados

# Exibir as informações dos dois pokémons selecionados
print("Pokémon 1:", pokemon1.nome)
print("Vantagens e Desvantagens do Pokémon 1:")
for tipo in pokemon1.tipos:
    print("  - Tipo:", tipo.nome)
    print("    Vantagens:", tipo.vantagens)
    print("    Desvantagens:", tipo.fraquezas)

print("\nPokémon 2:", pokemon2.nome)
print("Vantagens e Desvantagens do Pokémon 2:")
for tipo in pokemon2.tipos:
    print("  - Tipo:", tipo.nome)
    print("    Vantagens:", tipo.vantagens)
    print("    Desvantagens:", tipo.fraquezas)

# Realizar a comparação
resultado, vantagens = verificar_vantagem(pokemon1, pokemon2)
if resultado is not None:
    print(resultado)
    print("\nMotivo da vantagem:", ", ".join(vantagens))
else:
    print("\nNão há vantagem específica entre os pokémons.")
