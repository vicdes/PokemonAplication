import json

class Tipo:
    def __init__(self, nome, fraquezas, vantagens):
        self.nome = nome
        self.fraquezas = fraquezas
        self.vantagens = vantagens


class Pokemon:
    def __init__(self, nome, numero, hp, ataque, tipo):
        self.nome = nome
        self.numero = numero
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo


with open('pokemons.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

#acessa a lista de pokémons do JSON
pokemons_json = dados['pokemons']
lista_pokemons = []

#inicia a instanciação do pokemon baseado nas informações do JSON um por um
for pokemon_json in pokemons_json:

    #entra na chave 'tipo' do arquivo JSON e cria uma instância da classe Tipo com base nas informações do JSON
    tipo_json = pokemon_json['tipo']
    tipo = Tipo(tipo_json['nome'], tipo_json['fraquezas'], tipo_json['vantagens'])
    
    #instancia propriamente o pokemon com as informações do JSON + e o objeto da classe Tipo
    pokemon = Pokemon(
        pokemon_json['nome'],
        pokemon_json['numero'],
        pokemon_json['hp'],
        pokemon_json['ataque'],
        tipo
    )

    lista_pokemons.append(pokemon)

#printa tudo
for pokemon in lista_pokemons:
    print(f"Nome: {pokemon.nome}")
    print(f"Número: {pokemon.numero}")
    print(f"HP: {pokemon.hp}")
    print(f"Ataque: {pokemon.ataque}")
    print(f"Tipo: {pokemon.tipo.nome}")
    print(f"Fraquezas: {pokemon.tipo.fraquezas}")
    print(f"Vantagens: {pokemon.tipo.vantagens}")
    print()


def pega_nome_pokemon(num):
    for pokemon in lista_pokemons:
        if pokemon.numero == num:
            #print(pokemon.nome)
            return pokemon.nome

