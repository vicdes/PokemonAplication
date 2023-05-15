class TipoInexistenteException(Exception):
    def __init__(self, nome_tipo):
        self.mensagem = "\n[!] Não existe um tipo com o nome: {}"
        super().__init__(self.mensagem.format(nome_tipo))
