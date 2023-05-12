from controladores.ControladorTreinadores import ControladorTreinadores
from controladores.ControladorTiposPokemons import ControladorTiposPokemons
from controladores.ControladorPokemons import ControladorPokemons
from telas.TelaSistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__controlador_treinadores = ControladorTreinadores(self)
        self.__controlador_tipos_pokemons = ControladorTiposPokemons(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_treinadores(self):
        return self.__controlador_treinadores

    @property
    def controlador_tipos_pokemons(self):
        return self.__controlador_tipos_pokemons

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_treinadores(self):
        self.__controlador_treinadores.abre_tela()

    def cadastra_tipos_pokemons(self):
        self.__controlador_tipos_pokemons.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_treinadores, 2: self.cadastra_tipos_pokemons,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()