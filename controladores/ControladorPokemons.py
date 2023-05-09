from Pokemon import Pokemon
class ControladorPokemons:
    def __init__(self, tela_pokemon: TelaPokemon, controlador_sistema: ControladorSistema):
        if isinstance(tela_pokemon, TelaPokemon):
            self.__tela_pokemon = tela_pokemon
        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema

    def add_pokemon(self):
        pass

    def del_pokemon(self):
        pass

    def mostra_pokemons(self):
        pass

    def seleciona_pokemon(self):
        pass

    def abre_tela(self):
        pass