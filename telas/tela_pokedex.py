
# ! DESCONTINUADO
class TelaPokedex():

    def tela_opcoes(self):
        print("\n--------- TESTE TELA ---------")
        print("1 - Mostrar porcentagem pokedex")
        print("2 - Exibir nomes de pokemons capturados")
        print("0 - Retornar")

        opcao = int(input("\nEscolha a opcao: "))
        return opcao

    def mostrar_porcentagem_capturados(self, porcentagem):
        print(f'\n[!] Você capturou {porcentagem:.1f}% dos pokémons existentes na pokedex.')

    def mostrar_nome_pokemons_capturados(self, nomes):
        print(f'\nVocê já capturou {len(nomes)} pokémons! São eles:')
        for i, nome in enumerate(nomes):
            print(f"- {nome}")
