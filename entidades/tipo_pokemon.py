

class TipoPokemon:
    def __init__(self, nome, vantagens=None, fraquezas=None):
        self.nome = nome
        self.vantagens = vantagens or []
        self.fraquezas = fraquezas or []

    def adicionar_vantagem(self, tipo):
        self.vantagens.append(tipo)

    def adicionar_fraqueza(self, tipo):
        self.fraquezas.append(tipo)

    def remover_vantagem(self, tipo):
        if tipo in self.vantagens:
            self.vantagens.remove(tipo)

    def remover_fraqueza(self, tipo):
        if tipo in self.fraquezas:
            self.fraquezas.remove(tipo)