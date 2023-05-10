
# ! DESCONTINUADO
class TelaTime():
    def tela_opcoes(self):
        print("\n--------- TESTE TELA TIME ---------")
        print("1 - Mostrar time atual")
        print("2 - Adicionar pokémon ao time") 
        #mostrar pokémons disponíveis na hora de adicionar
        print("3 - Remover pokémon do time")
        print("0 - Retornar")

        opcao = int(input("\nEscolha a opcao: "))
        return opcao
    
    def add_pokemon(self):
        numero_pokemon = int(input('Digite o número do Pokémon que quer adicionar ao time: '))
        return numero_pokemon
    
    def deletar_pokemon(self):
        numero_pokemon = int(input('Digite o número do Pokémon que quer retirar do time: '))
        return numero_pokemon
    
    def mostra_mensagem(self, msg):
        print(msg)