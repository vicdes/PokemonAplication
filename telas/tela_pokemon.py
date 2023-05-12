
from telas.tela_abstract import AbstractTela



class TelaPokemon(AbstractTela):

    def tela_opcoes(self):
        print("\n--------- TESTE TELA POKEMON ---------")
        print("1 - Adicionar Pokémons") #! isso tbm acho meio estranho
        print("2 - Deletar Pokémon")
        print("3 - Mostrar Pokémons existentes")
        print("4 - Alterar HP ou Ataque de Pokémon") #! sou meio contra isso
        #! se tivermos algum crude de alteração prefiro excluir isso
        #! podemos ver com a patrícia se trocar um pokémon do time é válido
        #! talvez até possa ter um método q faça um swap de pokémons baseado no num
        #! seleciona o pokemon do time, seleciona o pokemon pra substituir e ta feito
        print("0 - Retornar")
        opcao = self.le_num_inteiro("\nEscolha a opção: ", [1, 2, 3, 4,0])
        return opcao
    # ! talvez falta adicionar o método adicionar pokémon. 
    
    def add_pokemon(): #! se não tiver a opção 1 da tela pokemon, isso deve ser excluido
        pass

    # * talvez isso possa se tornar um método abstrato pra ser usado no time?
    def seleciona_pokemon_numero(self):
        print("\nDigite o número do pokémon: ")
        num_pokemon = self.le_num_inteiro()
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
