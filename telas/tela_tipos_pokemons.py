
class TelaTiposPokemons:
    def tela_opcoes(self):
        print("--------- TIPOS DE POKÉMON ----------")
        print("Escolha a opcao")
        print("1 - Incluir tipo de pokémon")
        print("2 - Excluir tipo de pokémon")
        print("3 - Listar tipos de pokémon")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_tipo_pokemon(self):
        print("-------- CADASTRAR TIPO DE POKÉMON ---------")
        nome = input("Nome: ")
        #tirar:
        fraquezas = []
        while True:
            fraqueza = input("Fraqueza: ")
            fraquezas.append(fraqueza)
            continuar = input("Deseja digitar outra? \n1- sim \n2- não ")
            if continuar != 1:
                break
        vantagens = []
        while True:
            vantagem = input("Vantagem: ")
            vantagens.append(vantagem)
            continuar = input("Deseja digitar outra? \n1- sim \n2- não ")
            if continuar != 1:
                break
        return {"nome": nome, "fraquezas": fraquezas, "vantagens": vantagens}

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")


    def seleciona_tipo_pokemon(self):
        nome = input("Nome do tipo de pokémon que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)