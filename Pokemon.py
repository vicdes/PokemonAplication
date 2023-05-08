'''class Pokemon:
    def __init__(self, nome: str, num: int, hp: int, ataque: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(num, int):
            self.__num = num
        if isinstance(hp, int):
            self.__hp = hp
        if isinstance(ataque, int):
            self.__ataque = ataque
        self.__tipos = []

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

    def add_tipo(self, tipo: TipoPokemon):
        if isinstance(tipo, TipoPokemon):
            self.__tipos.append(tipo)

class TipoPokemon:
    def __init__(self, nome, descricao):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(descricao, str):
            self.__descricao = descricao
        self.__fraquezas = []
        self.__vantagens = []

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def fraquezas(self):
        return self.__fraquezas

    @property
    def vantagens(self):
        return self.__vantagens

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao

    def add_fraqueza(self, tipo: TipoPokemon):
        if isinstance(tipo, TipoPokemon):
            self.__fraquezas.append(tipo)

    def add_vantagem(self, tipo: TipoPokemon):
        if isinstance(tipo, TipoPokemon):
            self.__fraquezas.append(tipo)

from Pokemon import *

class PokemonCapturado(Pokemon):
    def __int__(self, nome: str, num: int, hp: int, ataque: int, tipos:[], peso: int, altura: float):
        super().__init__(nome, num, hp, ataque, tipos)
        if isinstance(peso, int):
            self.__peso = peso
        if isinstance(altura, float):
            self.__altura = altura

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @peso.setter
    def peso(self, peso: int):
        if isinstance(peso, int):
            self.__peso = peso

    @altura.setter
    def altura(self, altura: float):
        if isinstance(altura, float):
            self.__altura = altura'''

class Treinador:
    pass

class Pokemon:
    #pokemons = []
    pass

class PokemonsCapturados:
    pass

class Time:
    pass

class Pokedex:
    pass