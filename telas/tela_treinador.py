from telas.tela_abstract import AbstractTela

class TelaTreinador(AbstractTela): 
    def tela_opcoes(self):
        self.titulo("Tela Treinadores")
        print("\nEscolha a opcao")
        print("  1 - Incluir Treinador INCLUINDO CORRETAMENTE")
        print("  2 - Excluir Treinador DELETANDO CORRETAMENTE")
        print("  3 - Listar Treinadores LISTANDO CORRETAMENTE")
        print("\n  4 - Cadastrar time")
        print("  5 - Deletar time")
        print("  6 - Alterar time")
        print("\n  7 - Listar pokemons de um treinador LISTANDO CORRETAMENTE")
        print("  8 - Mostrar time de um treinador LISTANDO CORRETAMENTE")
        print("  0 - Retornar")
        opcao = self.le_num_inteiro("\nEscolha a opcao: ", [0, 1, 2, 3, 4, 5,6, 7, 8]) #* tratamento de exceção FEITO
        return opcao

    def seleciona_funcao_alterar_time(self):
        print("\nEscolha a opcao")
        print("  1 - Incluir pokemon")
        print("  2 - Excluir pokemon")
        print("  3 - Trocar pokemon")
        opcao = self.le_num_inteiro("\nEscolha a opcao: ", [1, 2, 3])  # * tratamento de exceção FEITO
        return opcao


    def cadastrar_outro_pokemon(self):
        print("\nDeseja continuar? \n1- sim \n2- não ")
        continuar = self.le_num_inteiro() == 1 # * tratamento de exceção FEITO
        return continuar

    def pega_dados_treinador(self):
        self.titulo2("Cadastrar Treinador")
        nickname = input("Nickname: ")
        return {"nickname": nickname, "porcentagem_pokedex": 0.0}

    def mostra_treinador(self, dados_treinador):
        print("Nickname: ", dados_treinador["nickname"])
        print("Porcentagem da pokedéx completa: {:.1f}%".format(dados_treinador["porcentagem_pokedex"]))

    def seleciona_treinador(self):
        nickname = input("Nickname do treinador que deseja selecionar: ")
        return nickname

    def seleciona_pokemon_capturado(self):
        print("\nCódigo do pokémon que deseja selecionar: ")
        codigo = self.le_num_inteiro() #* tratamento de exceção FEITO
        return codigo

    def seleciona_pokemon_do_time(self):
        print("\nCódigo do pokémon que deseja substituir: ")
        codigo = self.le_num_inteiro() #* tratamento de exceção FEITO
        return codigo
    
    def cadastrar_outro_pokemon(self):
        print("\nDeseja inserir outro pokémon? \n1- sim \n2- não ")
        continuar = self.le_num_inteiro() == 1 # * tratamento de exceção FEITO
        return continuar

    def mostra_mensagem(self, msg):
        print(msg)



