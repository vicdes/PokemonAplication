from telas.tela_tipos_pokemons import TelaTiposPokemons


class ControladorTiposPokemons:
    def __init__(self, controlador_sistema):
        self.__tipos = []
        self.__tela_tipo_pokemon = TelaTiposPokemons()
        self.__controlador_sistema = controlador_sistema

    def add_tipo(self):
        pass

    def del_tipo(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    def abre_tela(self):
        lista_opcoes = {1: self.add_tipo, 2: self.del_tipo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_treinador.tela_opcoes()]