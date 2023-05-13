class TipoPokemon:
    def __init__(self, nome, fraquezas, vantagens):
        self.__nome = nome
        self.__fraquezas = fraquezas
        self.__vantagens = vantagens

    @property
    def nome(self):
        return self.__nome

    @property
    def fraquezas(self):
        return self.__fraquezas

    @property
    def vantagens(self):
        return self.__vantagens

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def add_fraqueza(self, tipo: str):
        self.__fraquezas.append(tipo)

    def add_vantagem(self, tipo: str):
        self.__fraquezas.append(tipo)
