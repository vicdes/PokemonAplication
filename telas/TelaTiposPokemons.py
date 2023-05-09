from controladores.ControladorTiposPokemons import ControladorTiposPokemons

class TelaTiposPokemons:
    def __init__(self, controlador_tipos_pokemons: ControladorTiposPokemons):
        if isinstance(controlador_tipos_pokemons, ControladorTiposPokemons):
            self.__controlador_tipos_pokemons = controlador_tipos_pokemons

    def tela_opcoes(self):
        pass
