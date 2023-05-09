#DELETAR POSTERIORMENTE, ARQUIVO TEMPORÁRIO

import json

import sys
sys.path.append('C:\\Users\\Jose Eduardo\\Desktop\\Pokémon')
sys.path.append('C:\\Users\\Jose Eduardo\\Desktop\\Pokémon\\PokemonAplication\\pokemons.json')

class Tipo:
    def __init__(self, nome, fraquezas, vantagens):
        self.nome = nome
        self.fraquezas = fraquezas
        self.vantagens = vantagens

class Pokemon:
    lista_pokemons = []
    lista_pokemons_capturados = []

    def __init__(self, nome, numero, hp, ataque, tipo):
        self.nome = nome
        self.numero = numero
        self.hp = hp
        self.ataque = ataque
        self.tipo = tipo
        #self.lista_pokemons = Pokemon.lista_pokemons
    
    @property
    def nome(self):
        return self.__nome

    @property
    def num(self):
        return self.__num

    @property
    def hp(self):
        return self.__hp

    @property
    def ataque(self):
        return self.__ataque

    @property
    def tipos(self):
        return self.__tipos

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @num.setter
    def num(self, num: int):
        if isinstance(num, int):
            self.__num = num

    @hp.setter
    def hp(self, hp: int):
        if isinstance(hp, int):
            self.__hp = hp

    @ataque.setter
    def ataque(self, ataque: int):
        if isinstance(ataque, int):
            self.__ataque = ataque
    
    
    def add_pokemon(self, pokemon):
        self.lista_pokemons.append(pokemon)

    def capturar_pokemon(self, numero):
        for pokemon in self.lista_pokemons:
            if pokemon.numero == numero:
                self.lista_pokemons_capturados.append(pokemon)
                #print(f"O pokemon {pokemon.nome} foi capturado!")
                return
        #print("Não foi possível capturar o pokemon. Ele não existe na lista de pokemons.")
    
    def dados_pokemon_por_numero(self, numero):
        for pokemon in self.lista_pokemons:
            if pokemon.numero == numero:
                print(f"Nome: {pokemon.nome}")
                print(f"Número: {pokemon.numero}")
                #print(f"HP: {pokemon.hp}")
                #print(f"Ataque: {pokemon.ataque}")
                #print(f"Tipo: {pokemon.tipo.nome}")
                #print(f"Fraquezas: {pokemon.tipo.fraquezas}")
                #print(f"Vantagens: {pokemon.tipo.vantagens}")


with open('pokemons.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# acessa a lista de pokémons do JSON
pokemons_json = dados['pokemons']

# instancia propriamente o pokemon com as informações do JSON e o objeto da classe Tipo
for pokemon_json in pokemons_json:
    tipo_json = pokemon_json['tipo']
    tipo = Tipo(tipo_json['nome'], tipo_json['fraquezas'], tipo_json['vantagens'])
    pokemon = Pokemon(pokemon_json['nome'], pokemon_json['numero'], pokemon_json['hp'], pokemon_json['ataque'], tipo)
    Pokemon.lista_pokemons.append(pokemon)

# printa tudo
'''for pokemon in Pokemon.lista_pokemons:
    print()
    print(f"Nome: {pokemon.nome}")
    print(f"Número: {pokemon.numero}")
    print(f"HP: {pokemon.hp}")
    print(f"Ataque: {pokemon.ataque}")
    print(f"Tipo: {pokemon.tipo.nome}")
    print(f"Fraquezas: {pokemon.tipo.fraquezas}")
    print(f"Vantagens: {pokemon.tipo.vantagens}")'''

def pokemons_existentes(): 
    print('\nPokemons Existentes')
    for i, pokemon in enumerate(Pokemon.lista_pokemons):
        if i == len(Pokemon.lista_pokemons) - 1:
            print(pokemon.nome)
        else:
            print(f"{pokemon.nome}  /  ", end="")

#pokemons_existentes()

def pokemons_capturados():
    print("\nLista de Pokemons Capturados:")
    for i, pokemon in enumerate(Pokemon.lista_pokemons_capturados):
        if i == len(Pokemon.lista_pokemons_capturados) - 1:
            print(pokemon.nome)
        else:
            print(f"{pokemon.nome}  /  ", end="")


pokemon.capturar_pokemon(25)  # O pokemon Pikachu foi capturado!
pokemon.capturar_pokemon(1) 
pokemon.capturar_pokemon(441) # Não foi possível capturar o pokemon. Ele não existe na lista de pokemons.

#pokemons_capturados()'''

class Treinador():
    def __init__(self, nome):
        self.__nome = nome
