
class TelaTiposPokemons:
    def tela_opcoes(self):
        pass

    def pega_dados_tipo_pokemon(self):
        print("-------- CADASTRAR TIPO DE POKÉMON ---------")
        nome = input("Nome: ")
        #tirar:
        fraquezas = []
        while True:
            fraqueza = input("Fraqueza: ")
            continuar = input("Deseja digitar outra? \n1- sim \n2- não ")
            if continuar != 1:
                break
        return {"Nome": nome}
