from exceptions.nickname_repetido_exception import NicknameRepetidoException
from telas.tela_treinador import TelaTreinador
from entidades.treinador import Treinador
from exceptions.pokemon_ja_cadastrado_exception import PokemonJaCadastradoException
from exceptions.pokemon_inexistente_exception import PokemonInexistenteException
from exceptions.nickname_nao_encontrado_exception import NicknameNaoEncontradoException
from exceptions.nao_ha_time_cadastrado import NaoHaTimeCadastradoException
from entidades.pokemon import Pokemon
from entidades.tipo_pokemon import TipoPokemon
from entidades.time import Time


class ControladorTreinadores:
    def __init__(self, controlador_sistema):
        #deixamos o treinador Ash temporário pra fazer testes mais rapidamente.
        self.__treinadores = [Treinador(
            "Ash",
            6.98,
            [
                Pokemon("Pikachu", 25, 35, 55, [TipoPokemon("Elétrico")]),
                Pokemon("Charmander", 4, 39, 52, [TipoPokemon("Fogo")]),
                Pokemon("Pidgey", 16, 40, 45, [TipoPokemon("Normal"), TipoPokemon("Voador")]),
                Pokemon("Caterpie", 10, 45, 3, [TipoPokemon("Inseto")])
            ],
            Time([
                Pokemon("Pikachu", 25, 35, 55, [TipoPokemon("Elétrico")]),
                Pokemon("Charmander", 4, 39, 52, [TipoPokemon("Fogo")]),
                Pokemon("Pidgey", 16, 40, 45, [TipoPokemon("Normal"), TipoPokemon("Voador")]),
            ])
        )
    ]
            #(Treinador("Ash", 0.0, [Pokemon("Pikachu", 25, 35, 55), Pokemon("Charmander", 4, 39, 52), Pokemon("Pidgey", 16, 40, 45)], Time([Pokemon("Pikachu", 25, 35, 55), Pokemon("Charmander", 4, 39, 52), Pokemon("Pidgey", 16, 40, 45)])))]
        self.__tela_treinador = TelaTreinador()
        self.__controlador_sistema = controlador_sistema
    
    def verifica_treinador(self): #vê se o nome do treinador é existente na lista de treinadores
        while True:
            try: #checa se o nome do treinador digitado existe na lista de treinadores
                nickname = self.__tela_treinador.seleciona_treinador()
                if nickname == '0':
                    break
                treinador = self.pega_treinador_por_nickname(nickname)
                if treinador is not None:
                    return treinador
                else:
                    raise NicknameNaoEncontradoException(nickname)
            except NicknameNaoEncontradoException as e:
                self.__tela_treinador.mostra_mensagem(e)
                self.__tela_treinador.mostra_mensagem('Tente novamente ou digite 0 para sair')

    def pega_treinador_por_nickname(self, nickname: str):
        for treinador in self.__treinadores:
            if treinador.nickname == nickname:
                return treinador
        return None

    def pega_porcentagem(self, treinador):
        if treinador is not None:
            total_pokemons_capturados = len(treinador.pokemons_capturados)
            total_pokemons = len(self.__controlador_sistema.controlador_pokemon.lista_pokemons)
            porcentagem = total_pokemons_capturados*100/total_pokemons
            treinador.porcentagem_pokedex = porcentagem
        else:
            return

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
                raise NicknameRepetidoException(nickname)
        except NicknameRepetidoException as e:
            self.__tela_treinador.mostra_mensagem(e)
            return
        self.__controlador_sistema.controlador_captura.captura_pokemon_inicial(nickname)
        self.__tela_treinador.cadastrado_com_sucesso()

    def del_treinador(self):
        self.lista_treinadores()

        treinador = self.verifica_treinador()

        if treinador is not None:
            self.__treinadores.remove(treinador)
            self.lista_treinadores()
            self.__tela_treinador.mostra_mensagem("\n[!] Treinador deletado!")
        '''else:
            self.__tela_treinador.mostra_mensagem("ATENÇÃO: Treinador inexistente!")
            return'''

    def listar_pokemons_capturados(self, nickname=None):
        if nickname is None:
            nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        pokemons_str = ""
        self.__tela_treinador.mostra_mensagem("\nSeus pokémons capturados: ")
        for pokemon in treinador.pokemons_capturados:
            pokemons_str += "#" + str(pokemon.num) + " " + pokemon.nome + "\n"
        self.__tela_treinador.mostra_mensagem(pokemons_str)

    def mostrar_time(self, nickname=None):
        if nickname is None:
            nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        pokemons_str = ""
        try:
            if treinador.time is not None:
                try:
                    if len(treinador.time.lista_pokemons) > 0:
                        self.__tela_treinador.mostra_mensagem("\nSeu time: ")
                        for pokemon in treinador.time.lista_pokemons:
                            pokemons_str += pokemon.nome + " "
                        self.__tela_treinador.mostra_mensagem(pokemons_str)
                    else:
                        raise NaoHaTimeCadastradoException()
                except NaoHaTimeCadastradoException as e:
                    self.__tela_treinador.mostra_mensagem(e)
            else:
                raise NaoHaTimeCadastradoException()
        except NaoHaTimeCadastradoException as e:
            self.__tela_treinador.mostra_mensagem(e)

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
            return
        if len(treinador.time.lista_pokemons) == 0:
            pokemon_novo = None
            continuar = True
            while continuar == True:
                codigo_pokemon = self.__tela_treinador.seleciona_pokemon_capturado()
                codigo = self.existe_na_pokedex(codigo_pokemon)
                if codigo_pokemon != codigo:
                    return
                for pokemon in treinador.pokemons_capturados:
                    if codigo_pokemon == pokemon.num:
                        pokemon_novo = pokemon
                try:
                    if pokemon_novo is not None and len(treinador.time.lista_pokemons) > 0:
                        for pokemon_cadastrado in treinador.time.lista_pokemons:
                            try:
                                if pokemon_cadastrado.num != pokemon_novo.num:
                                    pass
                                else:
                                    raise PokemonJaCadastradoException(pokemon_novo.num)
                            except PokemonJaCadastradoException as e:
                                self.__tela_treinador.mostra_mensagem(e)
                    elif pokemon_novo is None:
                        raise PokemonInexistenteException(codigo_pokemon)
                except PokemonInexistenteException as e:
                    self.__tela_treinador.mostra_mensagem(e)
                treinador.time.lista_pokemons.append(pokemon_novo)
                if len(treinador.time.lista_pokemons) == 3:
                    break
                continuar = self.__tela_treinador.cadastrar_outro_pokemon()
        else:
            self.__tela_treinador.mostra_mensagem("Já existe um time cadastrado para esse treinador!")

    def existe_na_pokedex(self, codigo):
        flag = False
        for pokemon in self.__controlador_sistema.controlador_pokemon.lista_pokemons:
            if pokemon.num == codigo:
                flag = True
        try:
            if flag == True:
                return codigo
            else:
                raise PokemonInexistenteException(codigo)
        except PokemonInexistenteException as e:
            self.__tela_treinador.mostra_mensagem(e)

    def del_time(self):
        nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        try:
            if treinador is not None:
                try:
                    if treinador.time is not None:
                        treinador.del_time()
                        self.__tela_treinador.mostra_mensagem("Time deletado!")
                        return
                    else:
                        raise NaoHaTimeCadastradoException()
                except NaoHaTimeCadastradoException as e:
                    self.__tela_treinador.mostra_mensagem(e)
            else:
                raise NicknameNaoEncontradoException(nickname)
        except NicknameNaoEncontradoException as e:
            self.__tela_treinador.mostra_mensagem(e)
            return

    def alterar_time(self):
        nickname = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_nickname(nickname)
        try:
            if treinador is not None:
                self.listar_pokemons_capturados(nickname)
                self.mostrar_time(nickname)
            else:
                raise NicknameNaoEncontradoException(nickname)
        except NicknameNaoEncontradoException as e:
            self.__tela_treinador.mostra_mensagem(e)
            return
        try:
            if treinador.time is not None:
                try:
                    if len(treinador.time.lista_pokemons) > 0:
                        opcao = self.__tela_treinador.seleciona_funcao_alterar_time()
                        if opcao == 1:
                            pokemon_novo = None
                            continuar = True
                            while continuar == True:
                                codigo_pokemon_novo = self.__tela_treinador.seleciona_pokemon_capturado()
                                for pokemon in treinador.pokemons_capturados:
                                    if codigo_pokemon_novo == pokemon.num:
                                        pokemon_novo = pokemon
                                try:
                                    if pokemon_novo is not None:
                                        if len(treinador.time.lista_pokemons) > 0 and len(treinador.time.lista_pokemons) < 3:
                                            for pokemon_cadastrado in treinador.time.lista_pokemons:
                                                try:
                                                    if pokemon_cadastrado.num != pokemon_novo.num:
                                                        pass
                                                    else:
                                                        raise PokemonJaCadastradoException(pokemon_novo.num)
                                                except PokemonJaCadastradoException as e:
                                                    self.__tela_treinador.mostra_mensagem(e)
                                                    return
                                            treinador.time.lista_pokemons.append(pokemon_novo)
                                            self.mostrar_time(nickname)
                                        elif len(treinador.time.lista_pokemons) < 3:
                                            treinador.time.lista_pokemons.append(pokemon_novo)
                                            self.mostrar_time(nickname)
                                        else:
                                            self.__tela_treinador.mostra_mensagem("O time já está cheio!")
                                            return
                                    else:
                                        raise PokemonInexistenteException(codigo_pokemon_novo)
                                except PokemonInexistenteException as e:
                                    self.__tela_treinador.mostra_mensagem(e)
                                    return
                                continuar = self.__tela_treinador.cadastrar_outro_pokemon()
                        elif opcao == 2:
                            continuar = True
                            while continuar == True:
                                codigo_pokemon_antigo = self.__tela_treinador.seleciona_pokemon_capturado()
                                flag = False
                                if len(treinador.time.lista_pokemons) > 0:
                                    for pokemon in treinador.time.lista_pokemons:
                                        if codigo_pokemon_antigo == pokemon.num:
                                            treinador.time.lista_pokemons.remove(pokemon)
                                            flag = True
                                    try:
                                        if flag == True:
                                            self.mostrar_time(nickname)
                                        else:
                                            raise PokemonInexistenteException(codigo_pokemon_antigo)

                                    except PokemonInexistenteException as e:
                                        self.__tela_treinador.mostra_mensagem(e)
                                        return
                                else:
                                    self.__tela_treinador.mostra_mensagem("O time está vazio!")
                                    return
                                continuar = self.__tela_treinador.cadastrar_outro_pokemon()
                        else:
                            try:
                                if treinador.time.lista_pokemons is not None:
                                    self.mostrar_time(nickname)
                                    pokemon_antigo = None
                                    pokemon_novo = None
                                    continuar = True
                                    while continuar == True:
                                        codigo_pokemon_antigo = self.__tela_treinador.seleciona_pokemon_do_time()
                                        codigo_pokemon_novo = self.__tela_treinador.seleciona_pokemon_capturado()
                                        for pokemon in treinador.time.lista_pokemons:
                                            if codigo_pokemon_antigo == pokemon.num:
                                                pokemon_antigo = pokemon
                                        try:
                                            if pokemon_antigo is not None:
                                                pass
                                            else:
                                                raise PokemonInexistenteException(codigo_pokemon_antigo)
                                        except PokemonInexistenteException as e:
                                            self.__tela_treinador.mostra_mensagem(e)
                                            return
                                        for pokemon in treinador.pokemons_capturados:
                                            if codigo_pokemon_novo == pokemon.num:
                                                pokemon_novo = pokemon
                                        try:
                                            if pokemon_novo is not None:
                                                for pokemon_cadastrado in treinador.time.lista_pokemons:
                                                    try:
                                                        if pokemon_cadastrado.num != pokemon_novo.num:
                                                            pass
                                                        else:
                                                            raise PokemonJaCadastradoException(pokemon_novo.num)
                                                    except PokemonJaCadastradoException as e:
                                                        self.__tela_treinador.mostra_mensagem(e)
                                                for pokemon in treinador.time.lista_pokemons:
                                                    if pokemon.num == pokemon_antigo.num:
                                                        treinador.time.lista_pokemons.remove(pokemon)
                                                        treinador.time.lista_pokemons.append(pokemon_novo)
                                                        self.mostrar_time(nickname)
                                                        break

                                            else:
                                                raise PokemonInexistenteException(codigo_pokemon_novo)
                                        except PokemonInexistenteException as e:
                                            self.__tela_treinador.mostra_mensagem(e)
                                            return
                                        continuar = self.__tela_treinador.cadastrar_outro_pokemon()
                                else:
                                    raise NaoHaTimeCadastradoException()
                            except NaoHaTimeCadastradoException as e:
                                self.__tela_treinador.mostra_mensagem(e)
                    else:
                        raise NaoHaTimeCadastradoException()
                except NaoHaTimeCadastradoException as e:
                    self.__tela_treinador.mostra_mensagem(e)
            else:
                raise NaoHaTimeCadastradoException()
        except NaoHaTimeCadastradoException as e:
            self.__tela_treinador.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_treinador, 2: self.del_treinador, 3: self.lista_treinadores, 4: self.add_time, 5: self.del_time, 6: self.alterar_time, 7: self.listar_pokemons_capturados, 8: self.mostrar_time, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_treinador.tela_opcoes()]()