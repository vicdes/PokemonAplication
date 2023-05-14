
from telas.tela_abstract import AbstractTela

class TelaCaptura(AbstractTela):
    def tela_opcoes(self):
        print("\n--------- TESTE TELA CAPTURA ---------")
        print("1 - Procurar Pokémons nas redondezas")
        print("2 - Log?")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("\nEscolha a opção: ", [1, 2, 0])
        return opcao
    
    def pega_dados_captura(self):
        print("-------- DADOS CAPTURA ----------")
        nickname = input("Nickname do treinador: ")

        return nickname

    def seleciona_pokemon_inicial(self):
        codigo_inicial = int(input("Digite o código do inicial que deseja capturar:\n#1 Bulbasaur\n#4 Charmander\n#7 Squirtle"))
        return codigo_inicial
    
    def mostra_mensagem(self, msg):
        print(msg)