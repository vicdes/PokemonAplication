import os
import sys
import time
import copy

cwd = os.getcwd()
sys.path.append(cwd)

from controladores.controladorPokemon import ControladorPokemon
from entidades.pokemon import Pokemon
import random
win = 0
derrotas = 0

class Treinador:
    def __init__(self, nome, equipe=None):
        self.__nome = nome
        self.__ataque_equipe = 0
        self.__hp_equipe = 0
        self.__pokemons_capturados = []
        self.__set_equipe(equipe)

    def get_pokemons_capturados(self):
        return self.__pokemons_capturados
    
    def __set_equipe(self, equipe):
        if equipe is None:
            self.__equipe = []
        elif len(equipe) > 3:
            raise ValueError("O equipe não pode ter mais do que 3 Pokémons.")
        else:
            self.__equipe = equipe
        self.__ataque_equipe = self.calcular_ataque_equipe()
        self.__hp_equipe = self.calcular_hp_equipe()

    def captura_pokemon(self, pokemon):
        if pokemon in self.__pokemons_capturados:
            print(f"Você já capturou o {pokemon.nome} antes!")
        else:
            self.__pokemons_capturados.append(pokemon)
            print(f"\nParabéns, você capturou o {pokemon.nome}!")

    def calcular_ataque_equipe(self):
        ataque_equipe = 0
        for pokemon in self.__equipe:
            ataque_equipe += pokemon.ataque
        return ataque_equipe

    def calcular_hp_equipe(self):
        hp_equipe = 0
        for pokemon in self.__equipe:
            hp_equipe += pokemon.hp
        return hp_equipe
    
    @property
    def hp_equipe(self):
        return self.__hp_equipe

    @hp_equipe.setter
    def hp_equipe(self, valor):
        self.__hp_equipe = valor

    @property
    def ataque_equipe(self):
        return self.__ataque_equipe
    
    @ataque_equipe.setter
    def ataque_equipe(self, valor):
        self.__ataque_equipe = valor

    def verifica_numero_pokemon_capturado(self, numero_pokemon):
        numeros_capturados = [p.num for p in self.__pokemons_capturados]
        return numero_pokemon in numeros_capturados
    
    # Métodos para acessar os valores calculados
    @property
    def equipe(self):
        return self.__equipe
    
    @equipe.setter
    def equipe(self, equipe):
        self.__set_equipe = equipe

    @property
    def nome(self):
        return self.__nome



#####################################################################
#####################################################################
#####################################################################

def titulo(mensagem):
    #titulo = "Batalha Pokémon"
    linha_separadora = "=" * 80
    print(f"\n{linha_separadora}\n{mensagem.center(len(linha_separadora))}\n{linha_separadora}")

class CapturaPokemon:
    def __init__(self, treinador: Treinador):
        if (isinstance(treinador, Treinador)):
            self.__treinador = treinador
        self.__oponente = None

    
    def escolher_pokemon_aleatorio(self):
        pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        return Pokemon(pokemon_aleatorio['nome'], pokemon_aleatorio['num'], pokemon_aleatorio['hp'], pokemon_aleatorio['ataque'])
    
    def iniciar_batalha(self):
        global win, derrotas
        capturado = False
        rodada = 1

        titulo('Batalha Pokémon')

        oponente = self.escolher_pokemon_aleatorio()
        #pokemon_original = oponente.copy()
        num = oponente.num
        if self.__treinador.verifica_numero_pokemon_capturado(num):
            print(f"\n[ATENÇÃO] Você já capturou um Pokémon {oponente.nome} #{oponente.num} antes. Você não poderá capturá-lo novamente.\n")
            capturado = True
        else:
            capturado = False
        
        #usando 'selvagem' como referencia aos jogos
        print(f"\nUm {oponente.nome} selvagem apareceu!")
    
        hp_original = oponente.hp
        ataque_original = oponente.ataque

        tamanho_equipe = len(self.__treinador.equipe)

        multiplicador = random.choice([tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, 4, 4, 5,])
        oponente.hp = int(oponente.hp * multiplicador)

        multiplicador_ataque = random.choice([2,2,2,3,3,3])
        oponente.ataque = int(oponente.ataque * multiplicador_ataque)

        print(f"O {oponente.nome} selvagem tem {oponente.ataque} de ataque (*{multiplicador_ataque}) e {oponente.hp} de HP (*{multiplicador})! ")
        
        print(f'\nRodada {rodada}')
        print(f"\n{self.__treinador.nome}, seu equipe possui {self.__treinador.ataque_equipe} de ataque e {self.__treinador.hp_equipe} de HP.\n")

        while self.__treinador.hp_equipe > 0 and oponente.hp > 0:
            # turno do treinador
            equipe = self.__treinador.equipe

            for pokemon in equipe:
                if pokemon.hp > 0:
                    print(f"{pokemon.nome} ataca!")
                    oponente.hp -= pokemon.ataque
                    if oponente.hp <= 0:
                        break
                            
            #print(f"\nO {oponente.nome} selvagem tem {oponente.hp}HP restantes! - ({oponente.ataque} de ataque)")

            if oponente.hp <= 0:
                oponente.hp = 0 
                '''for pokemon in self.__treinador.equipe:
                        print(pokemon.hp)
                        pokemon.restaurar_hp()
                        print(pokemon.hp)'''
                print(f"\nO {oponente.nome} está desmaiado! ({oponente.hp} de hp restantes!) - ({oponente.ataque} de ataque)")

                print(f"\n{self.__treinador.nome} GANHOU 💙 a batalha!")
                oponente.hp = hp_original
                oponente.ataque = ataque_original
                win += 1
                if capturado == False:
                    self.tentar_captura(oponente)
                break

            # turno do Pokémon selvagem
            if oponente.hp > 0:
                print(f"\nO {oponente.nome} selvagem tem {oponente.hp}HP restantes! - ({oponente.ataque} de ataque)")
                print(f"O {oponente.nome} selvagem ataca!")
                #equipe_hp = sum([p.hp for p in equipe])
                self.__treinador.hp_equipe -= oponente.ataque
                if self.__treinador.hp_equipe < 0: 
                    self.__treinador.hp_equipe = 0
                print(f"\n{self.__treinador.nome}, sua equipe está desmaiada! ({self.__treinador.hp_equipe} de hp restantes!)")
                
                if self.__treinador.hp_equipe <= 0:
                    for pokemon in self.__treinador.equipe:
                        pokemon.restaurar_hp()
                    print("\nVocê PERDEU 💔 a batalha.")
                    
                    oponente.hp = hp_original
                    oponente.ataque = ataque_original
                    derrotas += 1
                    
                    break
            

    def tentar_captura(self, pokemon):
        #escolha = input(f'Deseja tentar capturar {pokemon.nome}? ').upper()
        escolha = 'S'
        if escolha == 'S':
            chance_captura = random.randint(1, 100)
            print('\nTestando sua sorte!')
            #time.sleep(2)
            
            print(f'Você tirou {chance_captura}.')
            if chance_captura >= 25:
                self.__treinador.captura_pokemon(pokemon)
                print('\nEsses são seus pokémons capturados até o momento: ')
                for pokemon in ash.get_pokemons_capturados():
                    print(  pokemon.nome, "-", pokemon.hp, "-", pokemon.ataque)
            else:
                print(f"\nQue pena, o {pokemon.nome} escapou...")
        else:
            return 


pokemon_testes = [
    {"nome": "Bulbasaur", "num": 1, "hp": 45, "ataque": 49},
    {"nome": "Charmander", "num": 4, "hp": 39, "ataque": 52},
    {"nome": "Squirtle", "num": 7, "hp": 44, "ataque": 48},
    {"nome": "Mankey", "num": 56, "hp": 40, "ataque": 80},
    {"nome": "Pidgey", "num": 16, "hp": 40, "ataque": 45},
    {"nome": "Jigglypuff", "num": 39, "hp": 115, "ataque": 45},
    {"nome": "Pikachu", "num": 25, "hp": 35, "ataque": 55},
    {"nome": "Geodude", "num": 74, "hp": 40, "ataque": 80},
    {"nome": "Abra", "num": 63, "hp": 25, "ataque": 20},
    {"nome": "Magikarp", "num": 129, "hp": 20, "ataque": 10},
    {"nome": "Diglett", "num": 50, "hp": 10, "ataque": 55},
    {"nome": "Caterpie", "num": 10, "hp": 45, "ataque": 30},
    {"nome": "Ekans", "num": 23, "hp": 35, "ataque": 60},
    {"nome": "Sandshrew", "num": 27, "hp": 50, "ataque": 75},
    {"nome": "Nidoran♀", "num": 29, "hp": 55, "ataque": 47},
    {"nome": "Nidoran♂", "num": 32, "hp": 46, "ataque": 57},
    {"nome": "Clefairy", "num": 35, "hp": 70, "ataque": 45},
    {"nome": "Vulpix", "num": 37, "hp": 38, "ataque": 41},
    {"nome": "Zubat", "num": 41, "hp": 40, "ataque": 45},
    {"nome": "Golbat", "num": 42, "hp": 75, "ataque": 80},
    {"nome": "Oddish", "num": 43, "hp": 45, "ataque": 50},
    {"nome": "Paras", "num": 46, "hp": 35, "ataque": 70},
    {"nome": "Venonat", "num": 48, "hp": 60, "ataque": 55},
    {"nome": "Diglett", "num": 50, "hp": 10, "ataque": 55},
    {"nome": "Meowth", "num": 52, "hp": 40, "ataque": 45},
    {"nome": "Psyduck", "num": 54, "hp": 50, "ataque": 52}
]


controlador_pokemon = ControladorPokemon()

ControladorPokemon.add_lista(pokemon_testes)
#controlador_pokemon.mostra_tudo()

#controlador_pokemon = ControladorPokemon()

#controlador_pokemon.abre_tela()
pikachu = Pokemon("Pikachu", 25, 35, 55)
charmander = Pokemon("Charmander", 4, 39, 52)
squirtle = Pokemon("Squirtle", 7, 44, 48)

# criar o time do treinador
equipe = [pikachu, charmander, squirtle]

# criar o treinador com o time
ash = Treinador("Lulu", equipe)

ash.captura_pokemon(pikachu)
ash.captura_pokemon(charmander)
ash.captura_pokemon(squirtle)

for pokemon in ash.get_pokemons_capturados():
    print(pokemon.nome, "-", pokemon.hp, "-", pokemon.ataque)

capture = CapturaPokemon(ash)


#while True:
#for i in range(3):
capture.iniciar_batalha()
    #continuar = input('\n Deseja continuar? [S/N]').upper()
    #if continuar != 'S':
    #    break

#* teste de vitórias e derrotas
print('\nVitórias',win)
print('Derrotas',derrotas)