from telas.tela_abstract import AbstractTela

class TelaTiposPokemons(AbstractTela):
    def tela_opcoes(self):
        self.titulo("Tipos de Pokémon")
        print("\nEscolha a opcao")
        print("  1 - Incluir tipo de pokémon")
        print("  2 - Excluir tipo de pokémon")
        print("  3 - Listar tipos de pokémon")
        print("  0 - Retornar")
        opcao = self.le_num_inteiro("\nEscolha a opcao: ", [0, 1, 2, 3])  #* tratamento de exceção FEITO
        return opcao

    def pega_dados_tipo_pokemon(self):
        self.titulo2("Cadastrar Tipo de Pokémon")
        nome = input("Nome: ") #! tratamento de exceção
        
        fraquezas = []
        continuar = "1"
        while continuar == "1":
            fraqueza = input("Fraqueza: ") #! tratamento de exceção
            fraquezas.append(fraqueza)
            continuar = self.le_num_inteiro("Deseja digitar outra? \n1- sim \n2- não ", [1,2]) #* tratamento de exceção FEITO
        
        vantagens = []
        continuar = "1"
        while continuar == "1":
            vantagem = input("Vantagem: ") #! tratamento de exceção
            vantagens.append(vantagem)
            continuar = self.le_num_inteiro("Deseja digitar outra? \n1- sim \n2- não ", [1,2]) #* tratamento de exceção FEITO
        return {"nome": nome, "fraquezas": fraquezas, "vantagens": vantagens}

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")


    def seleciona_tipo_pokemon(self):
        nome = input("Nome do tipo de pokémon que deseja selecionar: ") #! tratamento de exceção
        return nome

    def mostra_mensagem(self, msg):
        print(msg)