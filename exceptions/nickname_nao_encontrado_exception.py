class NicknameNaoEncontradoException(Exception):
    def __init__(self, nickname):
        self.mensagem = "\n[!] Não existe um treinador com o nickname: {}"
        super().__init__(self.mensagem.format(nickname))
