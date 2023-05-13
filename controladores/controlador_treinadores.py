from exceptions.nickname_repetido_exception import NicknameRepetidoExcpetion
from telas.tela_treinador import TelaTreinador
from entidades.treinador import Treinador

class ControladorTreinadores:
    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaTreinador()
        self.__controlador_sistema = controlador_sistema

    def pega_treinador_por_nickname(self, nickname: str):
        for treinador in self.__treinadores:
            if treinador.nickname == nickname:
                return treinador
        return None

    def lista_treinadores(self):
        for treinador in self.__treinadores:
            self.__tela_treinador.mostra_treinador({"nickname": treinador.nickname, "pokedex": treinador.porcentagem_pokedex})

    def add_treinador(self):
        dados_treinador = self.__tela_treinador.pega_dados_treinador()
        nickname = dados_treinador["nickname"]
        treinador = self.pega_treinador_por_nickname(nickname)
        try:
            if treinador == None:
                treinador = Treinador(dados_treinador["nickname"], dados_treinador["porcentagem_pokedex"])
                self.__treinadores.append(treinador)
            else:
                raise NicknameRepetidoExcpetion(nickname)
        except NicknameRepetidoExcpetion as e:
            self.__tela_treinador.mostra_mensagem(e)

    def del_treinador(self):
        self.lista_treinadores()
        nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)

        if treinador is not None:
            self.__treinadores.remove(treinador)
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENÇÃO: Treinador inexistente!")

    def add_time(self):
        pass

    def del_time(self):
        pass

    def alterar_time(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_treinador, 2: self.del_treinador, 3: self.lista_treinadores, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_treinador.tela_opcoes()]()
