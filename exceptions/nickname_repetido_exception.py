class NicknameRepetidoException(Exception):
    def __init__(self, nickname):
        self.mensagem = "\n[!] Já existe um treinador com o nickname: {}"
        super().__init__(self.mensagem.format(nickname))
