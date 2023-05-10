import os
import sys
import time
import copy

# Get the current working directory
cwd = os.getcwd()

# Append the current working directory to sys.path
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
        self.__ataque_equipe = self.__calcular_ataque_equipe()
        self.__hp_equipe = self.__calcular_hp_equipe()

    def captura_pokemon(self, pokemon):
        if pokemon in self.__pokemons_capturados:
            print(f"Você já capturou o {pokemon.nome} antes!")
        else:
            self.__pokemons_capturados.append(pokemon)
            print(f"\nParabéns, você capturou o {pokemon.nome}!")

            
    def __calcular_ataque_equipe(self):
        ataque_equipe = 0
        for pokemon in self.__equipe:
            ataque_equipe += pokemon.ataque
        return ataque_equipe

    def __calcular_hp_equipe(self):
        hp_equipe = 0
        for pokemon in self.__equipe:
            hp_equipe += pokemon.hp
        return hp_equipe
    
    def verifica_numero_pokemon_capturado(self, numero_pokemon):
        numeros_capturados = [p.num for p in self.__pokemons_capturados]
        return numero_pokemon in numeros_capturados
    
    # Métodos para acessar os valores calculados
    def get_ataque_equipe(self):
        return self.__ataque_equipe

    def get_hp_equipe(self):
        return self.__hp_equipe

    def get_equipe(self):
        return self.__equipe

    def set_equipe(self, equipe):
        self.__set_equipe(equipe)

    @property
    def nome(self):
        return self.__nome

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
        print()
        print("==="*10)
        print("Iniciando batalha...")
        print("==="*10)

        oponente = self.escolher_pokemon_aleatorio()
        #pokemon_original = oponente.copy()
        num = oponente.num
        if self.__treinador.verifica_numero_pokemon_capturado(num):
            print(f"\n[ATENÇÃO] Você já capturou um Pokémon {oponente.nome} #{oponente.num} antes. Você não poderá capturá-lo novamente.\n")
            capturado = True
        else:
            capturado = False
        
        #usando 'selvagem' como referencia aos jogos
        print(f"Um {oponente.nome} selvagem apareceu!")
        hp_equipe = sum([p.hp for p in self.__treinador.get_equipe()])
        ataque_equipe = sum([p.ataque for p in self.__treinador.get_equipe()])
        #hpFixo = oponente.hp #! GAMBIARRA
        #ataqueFixo = oponente.ataque #! GAMBIARRA

        multiplicador = random.choice([3, 3, 3, 4, 4])
        oponente.hp = int(oponente.hp * multiplicador)

        multiplicador_ataque = random.choice([1,2,2,2,3,3,3])
        oponente.ataque = int(oponente.ataque * multiplicador_ataque)

        print(f"O {oponente.nome} selvagem tem {oponente.ataque} de ataque (*{multiplicador_ataque}) e {oponente.hp} de HP (*{multiplicador})! ")
        print(f"\n{self.__treinador.nome}, seu equipe possui {ataque_equipe} de ataque e {hp_equipe} de HP.\n")

        while hp_equipe > 0 and oponente.hp > 0:
            # turno do treinador
            equipe = self.__treinador.get_equipe()

            for pokemon in equipe:
                if pokemon.hp > 0:
                    print(f"{pokemon.nome} ataca!")
                    oponente.hp -= pokemon.ataque
                    if oponente.hp <= 0:
                        break

            print(f"\nO {oponente.nome} selvagem agora tem {oponente.hp} de HP! - ({oponente.ataque} de ataque)")

            if oponente.hp <= 0:
                print(f"\n{self.__treinador.nome} GANHOU 💙 a batalha!")
                #oponente.hp = hpFixo #! GAMBIARRA
                win += 1
                if capturado == False:
                    self.tentar_captura(oponente)
                break

            # turno do Pokémon selvagem
            if oponente.hp > 0:
                print(f"O {oponente.nome} selvagem ataca!")
                equipe_hp = sum([p.hp for p in equipe])
                hp_equipe -= oponente.ataque
                print(f"\n{self.__treinador.nome}, sua equipe agora tem {hp_equipe} de HP!")
                if hp_equipe <= 0:
                    print("\nVocê PERDEU 💔 a batalha.")
                    #oponente.hp = hpFixo #! GAMBIARRA
                    derrotas += 1
                    break


    def tentar_captura(self, pokemon_original):
        escolha = input(f'Deseja tentar capturar {pokemon_original.nome}? ').upper()
        if escolha == 'S':
            chance_captura = random.randint(1, 100)
            print('Testando sua sorte...')
            time.sleep(2)
            
            print(f'Você tirou {chance_captura}.')
            if chance_captura >= 25:
                self.__treinador.captura_pokemon(pokemon_original)
                print('Esses são seus pokémons capturados até o momento: ')
                for pokemon in ash.get_pokemons_capturados():
                    print(pokemon.nome, "-", pokemon.hp, "-", pokemon.ataque)
            else:
                print(f"Que pena, o {pokemon.nome} escapou...")
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

ControladorPokemon.add_lista(pokemon_testes.copy())
#controlador_pokemon.mostra_tudo()

#controlador_pokemon = ControladorPokemon()

#controlador_pokemon.abre_tela()
pikachu = Pokemon("Pikachu", 25, 35, 55)
charmander = Pokemon("Charmander", 4, 39, 52)
squirtle = Pokemon("Squirtle", 7, 44, 48)

# criar o time do treinador
equipe = [pikachu, charmander, squirtle]

# criar o treinador com o time
ash = Treinador("Ash", equipe)

ash.captura_pokemon(pikachu)
ash.captura_pokemon(charmander)
ash.captura_pokemon(squirtle)

for pokemon in ash.get_pokemons_capturados():
    print(pokemon.nome, "-", pokemon.hp, "-", pokemon.ataque)

# Create a CapturePokemon object and initiate a battle
capture = CapturaPokemon(ash)
while True:
    capture.iniciar_batalha()
    continuar = int(input('1 - CONTINUA'))
    if continuar != 1:
        break

print(win)
print(derrotas)