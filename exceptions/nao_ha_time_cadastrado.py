class NaoHaTimeCadastradoException(Exception):
    def __init__(self):
        self.mensagem = "\n[!] Não existe time cadastrado para esse treinador!"
        super().__init__(self.mensagem)
