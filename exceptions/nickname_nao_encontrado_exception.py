class NicknameNaoEncontradoException(Exception):
    def __init__(self, nickname):
        self.mensagem = "Não existe treinador com o nickname {}"
        super().__init__(self.mensagem.format(nickname))
