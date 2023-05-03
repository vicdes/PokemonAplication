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
