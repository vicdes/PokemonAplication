
from telas.tela_abstract import AbstractTela

class TelaPokemon(AbstractTela):
    def tela_opcoes(self):
        self.titulo("Tela Pokémon")
        print("\nEscolha sua opcao")
        print("  1 - Deletar Pokémon OK")                    
        print("  2 - Mostrar Pokémons existentes OK")
        print("  3 - Alterar HP ou Ataque de Pokémon OK")
        print("  0 - Retornar")
        print('[OBS.] Essas alterações causam impacto em todo o jogo. Faça com moderação.')
        opcao = self.le_num_inteiro("\nEscolha a opção: ", [1, 2, 3, 0]) #* tratamento de exceção FEITO
        return opcao

    # * talvez isso possa se tornar um método abstrato pra ser usado no time?
    def seleciona_pokemon_numero(self):
        print("\nDigite o número do pokémon: ")
        num_pokemon = self.le_num_inteiro() #* tratamento de exceção FEITO
        return num_pokemon

    def mostrar_pokemons(self, lista): #recebe a lista nomes e nums vindas do controlador de pokemons
        if len(lista) == 0:
            print("Algo está errado... não existem pokémons registrados no jogo.")
        else:
            print(f"\nOs pokémons disponíveis são: ")
            for i, (nome, num) in enumerate(lista):
                print(f"- {nome} #{num}")
            print(f'\nTotal -> {len(lista)} pokémons.')
    
    def mostra_mensagem(self, msg):
        print(msg)
