


class TelaPokemon():
    def tela_opcoes(self):
        print("\n--------- TESTE TELA POKEMON ---------")
        print("1 - Adicionar Pokémons")
        print("2 - Deletar Pokémon")
        print("3 - Mostrar Pokémons existentes")
        print("0 - Retornar")

        opcao = int(input("\nEscolha a opcao: "))
        return opcao
    # ! talvez falta adicionar o método adicionar pokémon. 
    
    def deletar_pokemon(self):
        numero_pokemon = int(input('Digite o número do Pokémon que deseja deletar: '))
        return numero_pokemon
    
    def mostrar_pokemons(self, nomes):
        if len(nomes) == 0:
            print("Você não tem nenhum pokémon no seu time.")
        else:
            print(f"\nAo todo, existem {len(nomes)} pokémons! \nSão eles: ", end="")
            for i, nome in enumerate(nomes):
                if i == len(nomes) - 1:
                    print(nome)
                else:
                    print(f"{nome} / ", end="")

    def mostra_mensagem(self, msg):
        print(msg)
