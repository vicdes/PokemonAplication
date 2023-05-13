from exceptions.nickname_repetido_exception import NicknameRepetidoExcpetion
from telas.tela_treinador import TelaTreinador
from entidades.treinador import Treinador
from exceptions.pokemon_ja_cadastrado_exception import PokemonJaCadastradoException
from exceptions.pokemon_inexistente_exception import PokemonInexistenteException
from exceptions.nickname_nao_encontrado_exception import NicknameNaoEncontradoException


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
            self.__tela_treinador.mostra_treinador({"nickname": treinador.nickname, "porcentagem_pokedex": treinador.porcentagem_pokedex})

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
        nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        try:
            if treinador is not None:
                pass
            else:
                raise NicknameNaoEncontradoException(nickname)
        except NicknameNaoEncontradoException as e:
            self.__tela_treinador.mostra_mensagem(e)
        if len(treinador.time.lista_pokemon) == 0:
            pokemon_novo = None
            while True:
                codigo_pokemon = self.__tela_treinador.seleciona_pokemon_capturado()
                for pokemon in treinador.pokemons_capturados:
                    if codigo_pokemon == pokemon.codigo:
                        pokemon_novo = pokemon
                try:
                    if pokemon_novo is not None:
                        for pokemon_cadastrado in treinador.time.lista_pokemon:
                            try:
                                if pokemon_cadastrado.codigo != pokemon_novo.codigo:
                                    pass
                                else:
                                    raise PokemonJaCadastradoException(pokemon_novo.codigo)
                            except PokemonJaCadastradoException as e:
                                self.__tela_treinador.mostra_mensagem(e)
                    else:
                        raise PokemonInexistenteException(codigo_pokemon)
                except PokemonInexistenteException as e:
                    self.__tela_treinador.mostra_mensagem(e)
                if len(treinador.time.lista_pokemon) == 3:
                    break
                self.__tela_treinador.cadastrar_outro_pokemon()

    def del_time(self):
        nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        try:
            if treinador is not None:
                if treinador.time is not None:
                    treinador.time(None)
                else:
                    self.__tela_treinador.mostra_mensagem("O treinador selecionado não tem nenhum time castrado!")
            else:
                raise NicknameNaoEncontradoException(nickname)
        except NicknameNaoEncontradoException as e:
            self.__tela_treinador.mostra_mensagem(e)

    def alterar_time(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_treinador, 2: self.del_treinador, 3: self.lista_treinadores, 4: self.add_time, 5: self.del_time, 6: self.alterar_time, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_treinador.tela_opcoes()]()
