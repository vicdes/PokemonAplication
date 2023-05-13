from telas.tela_tipos_pokemons import TelaTiposPokemons
#from controladores.controlador_sistema import ControladorSistema


class ControladorTiposPokemons:
    def __init__(self, tela_tipo_pokemon: TelaTiposPokemons, controlador_sistema):
        self.__tipos = []
        if isinstance(tela_tipo_pokemon, TelaTiposPokemons):
            self.__tela_tipo_pokemon = tela_tipo_pokemon
        #if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema

    def add_tipo(self):
        pass

    def del_tipo(self):
        pass
