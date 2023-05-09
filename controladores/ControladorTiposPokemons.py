class ControladorTiposPokemons:
    def __init__(self, tela_tipo_pokemon: TelaTipoPokemon, controlador_sistema: ControladorSistema):
        self.__tipos = []
        if isinstance(tela_tipo_pokemon, TelaTipoPokemon):
            self.__tela_tipo_pokemon = tela_tipo_pokemon
        if isinstance(controlador_sistema, ControladorSistema):
            self.__controlador_sistema = controlador_sistema

    def add_tipo(self):
        while True:
            nome_fraq = self.__tela_tipo_pokemon.seleciona_fraquezas()
            fraq = pega_tipo_nome(nome_fraq)
            tipo.add_fraqueza(fraq)

