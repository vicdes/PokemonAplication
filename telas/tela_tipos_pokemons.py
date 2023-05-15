from telas.tela_abstract import AbstractTela

#imagino que não há necessidade de tratar as exceções que recebem strings. 

class TelaTiposPokemons(AbstractTela):
    def tela_opcoes(self):
        self.titulo("Tipos de Pokémon")
        print("\nEscolha uma opção")
        print("  1 - Incluir tipo de pokémon")
        print("  2 - Excluir tipo de pokémon")
        print("  3 - Listar tipos de pokémon")
        print("\n  0 - Retornar")
        opcao = self.le_num_inteiro("\nEscolha uma opção: ", [0, 1, 2, 3])  #* tratamento de exceção FEITO
        return opcao

    def pega_dados_tipo_pokemon(self):
        self.titulo2("Cadastrar Tipo de Pokémon")
        nome = input("\nNome: ").capitalize()
        fraquezas = []
        while True:
            fraqueza = input("\nFraqueza: ").capitalize()
            fraquezas.append(fraqueza) 
            continuar = self.le_num_inteiro("\nDeseja digitar outra? \n1- Sim \n2- Não\n", [1, 2]) #* tratamento de exceção FEITO
            if continuar == 2:
                break

        vantagens = []
        while True:
            vantagem = input("\nVantagem: ").capitalize()
            vantagens.append(vantagem)
            continuar = self.le_num_inteiro("\nDeseja digitar outra? \n1- Sim \n2- Não\n", [1, 2]) #* tratamento de exceção FEITO
            if continuar == 2:
                break

        return {"nome": nome, "vantagens": vantagens, "fraquezas": fraquezas,}

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")


    def seleciona_tipo_pokemon(self):
        nome = input("Nome do tipo de pokémon que deseja selecionar: ") #não posso colocar capitalize aqui pq quebra.
        return nome

    def mostra_mensagem(self, msg):
        print(msg)