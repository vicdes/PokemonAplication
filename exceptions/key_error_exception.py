class NicknameNaoEncontradoException(Exception):
    def __init__(self, nickname):
        self.mensagem = "\n[!] Valor inválido"
        super().__init__(self.mensagem)