from telas.tela_tipos_pokemons import TelaTiposPokemons
from entidades.tipo_pokemon import TipoPokemon

class ControladorTiposPokemons:
    def __init__(self, controlador_sistema):
        self.__tipos = []
        self.__tela_tipo_pokemon = TelaTiposPokemons()
        self.__controlador_sistema = controlador_sistema

    def add_tipo(self):
        dados_tipo = self.__tela_tipo_pokemon.pega_dados_tipo_pokemon()
        tipo_pokemon = TipoPokemon(dados_tipo["nome"], dados_tipo["fraquezas"], dados_tipo["vantagens"])
        self.__tipos.append(tipo_pokemon)

    def lista_tipos(self):
        if self.__tipos is not None:
            for tipo in self.__tipos:
                if len(tipo.fraquezas) == 0:
                    fraquezas_str = ", ".join(tipo.fraquezas)
                else:
                    fraquezas_str = "nenhuma"
                if len(tipo.vantagens) <= 0:
                    vantagens_str = "nenhuma"
                else:
                    vantagens_str = ", ".join(tipo.vantagens)
                self.__tela_tipo_pokemon.mostra_tipo_pokemon({"nome": tipo.nome, "fraquezas": fraquezas_str, "vantagens": vantagens_str})

    def del_tipo(self):
        self.lista_tipos()
        nome_tipo = self.__tela_tipo_pokemon.seleciona_tipo_pokemon()
        tipo = self.pega_tipo_por_nome(nome_tipo)

        if(tipo is not None):
          self.__tipos.remove(tipo)
          self.lista_tipos()
        else:
          self.__tela_tipo_pokemon.mostra_mensagem("ATENCAO: Tipo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_tipo, 2: self.del_tipo, 3: self.lista_tipos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_pokemon.tela_opcoes()]()