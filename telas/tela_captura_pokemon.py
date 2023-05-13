
from telas.tela_abstract import AbstractTela

class TelaCaptura(AbstractTela):
    def tela_opcoes(self):
        print("\n--------- TESTE TELA CAPTURA ---------")
        print("1 - Procurar Pokémons nas redondezas")
        print("2 - Log?")
        print("0 - Retornar")

        opcao = int(input("\nEscolha a opcao: "))
        return opcao
    
    def pega_dados_captura(self):
        print("-------- DADOS CAPTURA ----------")
        nickname = input("Nickname do treinador: ")

        return nickname
    
    def mostra_mensagem(self, msg):
        print(msg)