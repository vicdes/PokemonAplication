from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise ValueError ("Não é um objeto da classe Livro.")
        
        if livro in self.livros:
            raise ValueError ("Livro duplicado.")
        
        self.livros.append(livro)

        # Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        # Nao permitir insercao de Livros duplicados!
        

    def excluir_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            raise ValueError ("Não é um objeto da classe Livro.")
        
        self.livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
    
    