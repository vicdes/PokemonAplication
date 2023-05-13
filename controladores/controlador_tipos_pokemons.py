from telas.tela_tipos_pokemons import TelaTiposPokemons
from entidades.tipo_pokemon import TipoPokemon


class ControladorTiposPokemons:
    def __init__(self, controlador_sistema):
        self.__tipos = []
        self.__tela_tipo_pokemon = TelaTiposPokemons()
        self.__controlador_sistema = controlador_sistema

    def pega_tipo_por_nome(self, nome: str):
        for tipo in self.__tipos:
            if tipo.nome == nome:
                return tipo
        return None

    def add_tipo(self):
        dados_tipo = self.__tela_tipo_pokemon.pega_dados_tipo_pokemon()
        tipo_pokemon = TipoPokemon(dados_tipo["nome"])
        self.__tipos.append(tipo_pokemon)

    def lista_tipos(self):
        for tipo in self.__tipos:
            self.__tela_tipo_pokemon.mostra_tipo_pokemon({"nome": tipo.nome, "fraquezas": tipo.fraquezas, "vantagens": tipo.vantagens})

    def del_tipo(self):
        self.lista_tipos()
        nome_tipo = self.__tela_tipo_pokemon.seleciona_tipo_pokemon()
        tipo = self.pega_tipo_por_nome(nome_tipo)

        if(tipo is not None):
          self.__tipos.remove(tipo)
          self.lista_tipos()
        else:
          self.__tela_tipo_pokemon.mostra_mensagem("ATENCAO: Amigo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_tipo, 2: self.del_tipo, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_pokemon.tela_opcoes()]()