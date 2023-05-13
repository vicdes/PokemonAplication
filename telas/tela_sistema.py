
from telas.tela_abstract import AbstractTela

class TelaSistema(AbstractTela):
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Pokemon Application ---------")
        print("Escolha sua opcao")
        print("1 - Treinadores")
        print("2 - Tipos de Pokemons")
        print("3 - Batalha Pokémon")
        print("4 - Pokémons")
        
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("\nEscolha a opcao:",[0,1,2,3,4])
        return opcao