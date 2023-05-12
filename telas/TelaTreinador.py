from controladores.ControladorTreinadores import ControladorTreinadores
class TelaTreinador:
    def __init__(self, controlador_treiandores: ControladorTreinadores):
        if isinstance(controlador_treiandores, ControladorTreinadores):
            self.__controlador_treinadores = controlador_treiandores

    def tela_opcoes(self):
        pass

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



