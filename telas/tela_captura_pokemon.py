
from telas.tela_abstract import AbstractTela

class TelaCaptura(AbstractTela):
    def tela_opcoes(self):
        self.titulo('Tela Captura')
        print("\nEscolha sua opcao")
        print("  1 - Procurar Pokémons nas redondezas")
        print("\n  2 - Log Geral")
        print("  3 - Log Treinador")
        print("  4 - Ranking de Treinadores")
        print("\n  0 - Retornar")

        opcao = self.le_num_inteiro("\nEscolha a opção: ", [1, 2, 3, 4, 0]) #* tratamento de exceção FEITO
        return opcao
    
    def digite_para_continuar(self):
        input('\nAperte qualquer coisa para continuar...') #apenas pra dar uma pausa antes de retornar a tela

    def pega_dados_captura(self): #* tratamento de exceção FEITO
        self.titulo2("Dados Captura") 
        nickname = input("\nNickname do treinador: ")

        return nickname

    def seleciona_pokemon_inicial(self): #* tratamento de exceção FEITO
        codigo_inicial = self.le_num_inteiro("\nDigite o código do pokémon que deseja selecionar:\n#1 Bulbasaur\n#4 Charmander\n#7 Squirtle\n", [1,4,7]) 
        return codigo_inicial
    
    def log_treinador(self):
        nickname = input("\nDigite o nickname do treinador: ")
        return nickname

    def mostra_mensagem(self, msg):
        print(msg)