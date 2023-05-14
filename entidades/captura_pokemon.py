
class CapturaPokemon:
    def __init__(self, treinador):
        self.__treinador = treinador
        self.__oponente = None

    @property
    def treinador(self):
        return self.__treinador

    @property
    def oponente(self):
        return self.__oponente

    @treinador.setter
    def treinador(self, treinador):
        self.__treinador = treinador

    @oponente.setter
    def oponente(self, oponente):
        self.__oponente = oponente

######################################################################
#######################     ÁREA DE TESTES     #######################
######################################################################
#! REMOVER LINHAS ABAIXO DEPOIS
#! TUDO TEMPORÁRIO

'''import json

with open('populacao_pokemons.json', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# acessa a lista de pokémons do JSON
pokemons_json = dados['pokemons']

# instancia propriamente o pokemon com as informações do JSON e o objeto da classe Tipo
for pokemon_json in pokemons_json:
    #tipo_json = pokemon_json['tipo']
    #tipo = Tipo(tipo_json['nome'], tipo_json['fraquezas'], tipo_json['vantagens'])
    pokemon = Pokemon(pokemon_json['nome'], pokemon_json['num'], pokemon_json['hp'], pokemon_json['ataque'])
    ControladorPokemon.add_lista(pokemon)


#controlador_pokemon = ControladorPokemon()
#ControladorPokemon.add_lista(pokemon_testes)
#controlador_pokemon.mostra_tudo()

#controlador_pokemon = ControladorPokemon()

#controlador_pokemon.abre_tela()
pikachu = Pokemon("Pikachu", 25, 35, 55)
charmander = Pokemon("Charmander", 4, 39, 52)
squirtle = Pokemon("Squirtle", 7, 44, 48)

# criar o time do treinador
equipe = [pikachu, charmander, squirtle]

# criar o treinador com o time
ash = Treinador("NOME.DO.TREINADOR", equipe)

ash.captura_pokemon(pikachu)
ash.captura_pokemon(charmander)
ash.captura_pokemon(squirtle)

for pokemon in ash.get_pokemons_capturados():
    print(pokemon.nome, "-", pokemon.hp, "-", pokemon.ataque)

capture = CapturaPokemon(ash)


#while True:
for i in range(10):
    capture.iniciar_batalha()
    #continuar = input('\n Deseja continuar? [S/N]').upper()
    #if continuar != 'S':
    #    break

#* teste de vitórias e derrotas
print('\nVitórias',win)
print('Derrotas',derrotas)'''