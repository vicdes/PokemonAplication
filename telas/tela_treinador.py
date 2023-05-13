class TelaTreinador:
    def tela_opcoes(self):
        print("-------- TREINADORES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Treinador")
        print("2 - Excluir Treinador")
        print("3 - Listar Treinadores")
        print("4 - Excluir Treinador")
        print("0 - Retornar")

    def pega_dados_treinador(self):
        print("-------- CADASTRAR TREINADOR ---------")
        nickname = input("Nickname: ")
        return {"Nickname": nickname}


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

    def mostra_mensagem(self, msg):
        print(msg)



