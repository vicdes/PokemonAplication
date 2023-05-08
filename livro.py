from editora import Editora
from autor import Autor
from capitulo import *

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        if isinstance (editora, Editora):
            self.editora = editora
        if isinstance (autor, Autor):
            self.autor = autor
        
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.autores = []
        self.capitulos = []
        
        self.incluir_autor(autor)
        self.incluir_capitulo(numero_capitulo, titulo_capitulo)

        # Criar todos os atributos, incluindo as listas
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.autores
    
    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.autor: #verifica se é pertence a classe autor e se já está na lista de autores
            self.autores.append(autor)

        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        # Nao permitir insercao de Autores duplicados!

    def excluir_autor(self, autor: Autor):
        pass

    def incluir_capitulo(self, numero: int, titulo: str):
        self.capitulos.append(Capitulo(numero, titulo))
        
        #... Nao permitir insercao de Capitulos duplicados!

    def excluir_capitulo(self, titulo: str):
        pass

    def find_capitulo_by_titulo(self, titulo: str):
        # Procura na lista de capitulos se existe um Capitulo com este titulo 
        # Se encontrar, retorna o Capitulo encontrado
        pass
