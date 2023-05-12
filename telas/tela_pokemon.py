from controladores.controlador_pokemons import ControladorPokemons

class TelaPokemon:
    def __init__(self, controlador_pokemons: ControladorPokemons):
        if isinstance(controlador_pokemons, ControladorPokemons):
            self.__controlador_pokemons = controlador_pokemons

    def tela_opcoes(self):
        pass