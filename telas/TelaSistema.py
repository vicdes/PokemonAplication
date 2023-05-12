class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Pokemon Application ---------")
        print("Escolha sua opcao")
        print("1 - Treinadores")
        print("2 - Tipos de Pokemons")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao