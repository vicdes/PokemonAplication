class TelaTreinador:
    def tela_opcoes(self):
        print("-------- TREINADORES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Treinador")
        print("2 - Excluir Treinador")
        print("3 - Listar Treinadores")
        print("4 - Cadastrar time")
        print("5 - Deletar time")
        print("6 - Alterar time")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_treinador(self):
        print("-------- CADASTRAR TREINADOR ---------")
        nickname = input("Nickname: ")
        return {"nickname": nickname, "porcentagem_pokedex": 0.0}

    def mostra_treinador(self, dados_treinador):
        print("Nickname: ", dados_treinador["nickname"])
        print("Porcentagem da pokedéx completa: ", dados_treinador["porcentagem_pokedex"], "%")
        print("\n")

    def seleciona_treinador(self):
        nickname = input("Nickname do treinador que deseja selecionar: ")
        return nickname

    def seleciona_pokemon_capturado(self):
        codigo = input("Código do pokémon que deseja selecionar: ")
        return codigo

    def cadastrar_outro_pokemon(self):

        continuar = input("Deseja inserir outro pokémon? \n1- sim \n2- não ")
        self.seleciona_pokemon_capturado()

    def mostra_mensagem(self, msg):
        print(msg)



