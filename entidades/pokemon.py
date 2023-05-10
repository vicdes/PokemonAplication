class TipoPokemon:
    def __init__(self, tipo):
        self.tipo = tipo

class Pokemon:
    
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

    def copiar_pokemon(self):
        return Pokemon(self.__nome, self.__num, self.__hp, self.__ataque)
    
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