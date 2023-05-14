from controladores.controlador_treinadores import ControladorTreinadores
from controladores.controlador_pokemon import ControladorPokemon, Pokemon
from controladores.controlador_tipos_pokemons import ControladorTiposPokemons, TipoPokemon
from controladores.controlador_captura_pokemon import ControladorCaptura
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_treinadores = ControladorTreinadores(self)
        self.__controlador_tipos_pokemons = ControladorTiposPokemons(self)
        self.__controlador_pokemon = ControladorPokemon(self)
        self.__controlador_captura = ControladorCaptura(self)
        self.__tela_sistema = TelaSistema()
  
    import json

    with open("teste_pokemons_com_tipos.json", encoding="utf-8") as arquivo:
        dados_json = arquivo.read()

    # Converte JSON para dicionário Python
    dados = json.loads(dados_json)

    # Cria objetos Pokemon e TipoPokemon
    pokemons = []
    tipos_pokemon = {}

    for pokemon_data in dados["pokemons"]:
        nome = pokemon_data["nome"]
        num = pokemon_data["num"]
        hp = pokemon_data["hp"]
        ataque = pokemon_data["ataque"]
        tipos_data = pokemon_data["tipo"]

        tipos_nome = tipos_data["nome"]
        vantagens = tipos_data["vantagens"]
        fraquezas = tipos_data["fraquezas"]

        tipos = []
        for tipo_nome in tipos_nome:
            tipo = TipoPokemon(tipo_nome, vantagens, fraquezas)
            tipos.append(tipo)
            if tipo_nome not in tipos_pokemon:
                tipos_pokemon[tipo_nome] = tipo

        pokemon = Pokemon(nome, num, hp, ataque, tipos)
        ControladorPokemon.add_lista(pokemon)

    @property
    def controlador_treinadores(self):
        return self.__controlador_treinadores

    @property
    def controlador_tipos_pokemons(self):
        return self.__controlador_tipos_pokemons

    @property
    def controlador_pokemon(self):
        return self.__controlador_pokemon
    
    @property
    def controlador_captura(self):
        return self.__controlador_captura

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_treinadores(self):
        self.__controlador_treinadores.abre_tela()

    def cadastra_tipos_pokemons(self):
        self.__controlador_tipos_pokemons.abre_tela()

    def pokemons(self): #n sei se é justo colocar cadastra_pokemons
        self.__controlador_pokemon.abre_tela()

    def captura(self):
        self.__controlador_captura.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_treinadores, 2: self.cadastra_tipos_pokemons, 3: self.pokemons, 4: self.captura,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            return funcao_escolhida()