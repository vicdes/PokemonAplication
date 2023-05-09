class ControladorPokemonsCapturados:
    def __init__(self, tela_pokemon_capturado: TelaPokemonCapturado, controlador_sistema: ControladorSistema):
        if isinstance(tela_pokemon_capturado, TelaPokemonCapturado):
            self.__tela_pokemon = tela_pokemon_capturado
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


        