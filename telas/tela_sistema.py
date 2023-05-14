
from telas.tela_abstract import AbstractTela

class TelaSistema(AbstractTela):
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        self.titulo_sistema("Pokemon\nApplication")
        print("\nEscolha sua opcao")
        print("  1 - Treinadores")
        print("  2 - Tipos de Pokemons")
        print("  3 - Pokémons")
        print("  4 - Captura")
        print("  0 - Finalizar sistema")
        opcao = self.le_num_inteiro("\nEscolha a opcao: ",[0,1,2,3,4]) #* tratamento de exceção FEITO
        return opcao