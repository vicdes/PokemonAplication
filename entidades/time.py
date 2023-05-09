import sys
sys.path.append('C:\\Users\\Jose Eduardo\\Desktop\\Pokémon\\PokemonAplication')

from PokémonOLD import Pokemon


class Time():
    def __init__(self):
        self.__lista_pokemons_capturados = Pokemon.lista_pokemons_capturados
        self.__time = []
    
    #@property
    def get_pokemon_por_numero(self, numero):
        for pokemon in self.__time:
            if pokemon.numero == numero:
                return pokemon
        return None
    
    def mostrar_pokemons_disponiveis(self):
        #print('DENTRO DA CLASSE TIME')
        for pokemon in Pokemon.lista_pokemons_capturados:
            print()
            print(f"Nome: {pokemon.nome}")
            print(f"Número: {pokemon.numero}")
            '''
            print(f"HP: {pokemon.hp}")
            print(f"Ataque: {pokemon.ataque}")
            print(f"Tipo: {pokemon.tipo.nome}")
            print(f"Fraquezas: {pokemon.tipo.fraquezas}")
            print(f"Vantagens: {pokemon.tipo.vantagens}")
            '''

    def mostrar_time(self):
        if len(self.__time) == 0:
            print('Seu time está vazio. Você deve adicionar pelo menos um (1) pokémon ao seu time.')
        else:
            print('\nSeu time:')
            for pokemon in self.__time:
                print(f'- {pokemon.nome} #{pokemon.numero}')
                
    def add_pokemon_time(self, numero_pokemon):
        for pokemon in self.__lista_pokemons_capturados:
            if pokemon.numero == numero_pokemon:
                self.__time.append(pokemon)
                print(f"O pokémon {pokemon.nome} foi adicionado ao time com sucesso.")
                break
        else:
            print("Número de pokémon inválido. Tente outro número.")

    def del_pokemon_time(self, numero_pokemon):
        for pokemon in self.__time:
            if pokemon.numero == numero_pokemon:
                self.__time.remove(pokemon)
                # * esse print deve ser feito na tela com a função mostrar_msg()
                # * assim como os outros prints
                print(f"O pokemon {pokemon.nome} foi removido do seu time com sucesso.")
                break
            else:
                print('Nenhum pokémon encontrado com esse número. Tente novamente.')

# Cria uma instância da classe Time
time = Time()

# Chama o método mostrar_pokemons_disponiveis() na instância da classe Time
'''time.mostrar_pokemons_disponiveis()'''

'''while True:
    numero_pokemon = int(input('Qual pokemon vc deseja adicionar ao seu time? '))
    time.add_pokemon_time(numero_pokemon)
    continuar = input('Deseja adicionar outro pokémon ao time? S/N ').upper()
    if continuar == 'N':
        break

print('[TESTE] Time antes da remoção: ')
time.mostrar_time()'''

'''while True:
    numero_pokemon = int(input('Qual pokemon vc deseja remover de seu time? '))
    time.del_pokemon_time(numero_pokemon)
    continuar = input('Deseja remover outro pokémon do time? S/N ').upper()
    if continuar == 'N':
        break 

print('[TESTE] Time depois da remoção: ')
time.mostrar_time()'''