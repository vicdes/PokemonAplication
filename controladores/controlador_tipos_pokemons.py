from telas.tela_tipos_pokemons import TelaTiposPokemons
from entidades.tipo_pokemon import TipoPokemon
from exceptions.tipo_inexistente_exception import TipoInexistenteException

class ControladorTiposPokemons:
    def __init__(self, controlador_sistema):
        self.__tipos = []
        self.__tela_tipo_pokemon = TelaTiposPokemons()
        self.__controlador_sistema = controlador_sistema

    def add_tipo(self):
        dados_tipo = self.__tela_tipo_pokemon.pega_dados_tipo_pokemon()
        tipo_pokemon = TipoPokemon(dados_tipo["nome"], dados_tipo["vantagens"], dados_tipo["fraquezas"])
        self.__tipos.append(tipo_pokemon)

    def lista_tipos(self):
        if len(self.__tipos) > 0:
            for tipo in self.__tipos:

                if len(tipo.vantagens) > 0:
                    vantagens_str = ", ".join(tipo.vantagens)
                else:
                    vantagens_str = "nenhuma"

                if len(tipo.fraquezas) > 0:
                    fraquezas_str = ", ".join(tipo.fraquezas)
                else:
                    fraquezas_str = "nenhuma"

                self.__tela_tipo_pokemon.mostra_tipo_pokemon({"nome": tipo.nome, "vantagens": vantagens_str, "fraquezas": fraquezas_str,})
        else:
            self.__tela_tipo_pokemon.mostra_mensagem("\nNão há tipos cadastrados.")

    def pega_tipo_por_nome(self):
        self.__tela_tipo_pokemon.seleciona_tipo_pokemon()
        
        while True:
            try:
                nome = input("Digite o nome do tipo de pokémon: ")
                if nome in self.__tipos:
                    break
                else:
                    print("Tipo não encontrado. Digite novamente.")
            except Exception:
                print("Entrada inválida. Digite novamente.")
        
        return nome

    def del_tipo(self):
        self.lista_tipos()
        nome_tipo = self.__tela_tipo_pokemon.seleciona_tipo_pokemon()

        tipos_encontrados = []
        for tipo in self.__tipos:
            if tipo.nome == nome_tipo:
                tipos_encontrados.append(tipo)
        
        try:
            if tipos_encontrados:
                for tipo in tipos_encontrados:
                    self.__tela_tipo_pokemon.mostra_mensagem(f'\n[!] {tipo.nome} removido da lista de Tipos.')
                    self.__tipos.remove(tipo)

                #self.lista_tipos()
                
            else:
                raise TipoInexistenteException(nome_tipo)
            
        except TipoInexistenteException as e:
            self.__tela_tipo_pokemon.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.add_tipo, 2: self.del_tipo, 3: self.lista_tipos, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_tipo_pokemon.tela_opcoes()]()