class TipoRepetidoExcpetion(Exception):
    def __init__(self, nome):
        self.mensagem = "\n[!] Já existe um tipo com o nome {}"
        super().__init__(self.mensagem.format(nome))
