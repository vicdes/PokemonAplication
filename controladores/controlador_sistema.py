from controladores.controlador_treinadores import ControladorTreinadores
from controladores.controlador_pokemon import ControladorPokemon, Pokemon
from controladores.controlador_tipos_pokemons import ControladorTiposPokemons
from controladores.controlador_captura_pokemon import ControladorCaptura
from telas.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_treinadores = ControladorTreinadores(self)
        self.__controlador_tipos_pokemons = ControladorTiposPokemons(self)
        self.__controlador_pokemon = ControladorPokemon(self)
        self.__controlador_captura = ControladorCaptura(self)
        self.__tela_sistema = TelaSistema()


    #instancia os pokémons e adiciona eles na lista de pokémons que existem no jogo
    import json

    with open('populacao_pokemons.json', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    pokemons_json = dados['pokemons']

    for pokemon_json in pokemons_json:
        #tipo_json = pokemon_json['tipo']
        #tipo = Tipo(tipo_json['nome'], tipo_json['fraquezas'], tipo_json['vantagens'])
        pokemon = Pokemon(pokemon_json['nome'], pokemon_json['num'], pokemon_json['hp'], pokemon_json['ataque'])
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
