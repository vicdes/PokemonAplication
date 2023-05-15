class PokemonInexistenteException(Exception):
    def __init__(self, num_pokemon):
        self.mensagem = "\n[!] Não existe um pokémon com o código {}!"
        super().__init__(self.mensagem.format(num_pokemon))