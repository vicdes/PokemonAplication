class TipoPokemon:
    def __init__(self, nome, descricao):
        if isinstance(nome, str):
            self.__nome = nome
        self.__fraquezas = []
        self.__vantagens = []

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
        if isinstance(nome, str):
            self.__nome = nome

    def add_fraqueza(self, tipo: str):
        if isinstance(tipo, str):
            self.__fraquezas.append(tipo)

    def add_vantagem(self, tipo: str):
        if isinstance(tipo, str):
            self.__fraquezas.append(tipo)
q