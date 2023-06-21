class TipoRepetidoExcpetion(Exception):
    def __init__(self, nome):
        self.mensagem = "Já existe um tipo com o nome {}"
        super().__init__(self.mensagem.format(nome))
