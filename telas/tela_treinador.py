from telas.tela_abstract import AbstractTela

class TelaTreinador(AbstractTela):
    def tela_opcoes(self):
        self.titulo("Tela Treinadores")
        print("\nEscolha a opcao")
        print("  1 - Incluir Treinador")
        print("  2 - Excluir Treinador")
        print("  3 - Listar Treinadores")
        print("  4 - Cadastrar time")
        print("  5 - Deletar time")
        print("  6 - Alterar time")
        print("  7 - Listar pokemons de um treinador")
        print("  8 - Mostrar time de um treinador")
        print("  0 - Retornar")
        opcao = self.le_num_inteiro("\nEscolha a opcao: ", [0, 1, 2, 3, 4, 5,6, 7, 8])
        return opcao

    def pega_dados_treinador(self):
        self.titulo2("Cadastrar Treinador")
        nickname = input("Nickname: ")
        return {"nickname": nickname, "porcentagem_pokedex": 0.0}

    def mostra_treinador(self, dados_treinador):
        print("Nickname: ", dados_treinador["nickname"])
        print("Porcentagem da pokedéx completa: ", dados_treinador["porcentagem_pokedex"], "%")

    def seleciona_treinador(self):
        nickname = input("Nickname do treinador que deseja selecionar: ")
        return nickname

    def seleciona_pokemon_capturado(self):
        codigo = int(input("Código do pokémon que deseja selecionar: "))
        return codigo

    def seleciona_pokemon_do_time(self):
        codigo = int(input("Código do pokémon que deseja substituir: "))
        return codigo
    
    def cadastrar_outro_pokemon(self):
        continuar = input("Deseja inserir outro pokémon? \n1- sim \n2- não ") == "1"
        return continuar

    def mostra_mensagem(self, msg):
        print(msg)



