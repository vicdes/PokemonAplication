from pokemon import *

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
            self.__altura = altura

