class PokemonJaCadastradoException(Exception):
    def __init__(self, codigo):
        self.mensagem = "\n[!] Já existe um pokémon cadastrado com o código {}"
        super().__init__(self.mensagem.format(codigo))
