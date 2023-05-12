import os
import sys
import time

'''cwd = os.getcwd()
sys.path.append(cwd)'''

from controladores.controlador_pokemon import ControladorPokemon
from entidades.pokemon import Pokemon
import random

win = 0
derrotas = 0

'''#classe temporária, juntar com as classes da vic posteriormente
class Treinador: #! classe temporária. usar a de vic como correta. 
    #não lembro precisamente como q eu faria para referenciar a classe Time.
    #? self.__time = Time      basta assim? ou preciso colocar no construtor      time: Time ?
    # o mesmo vale para outras classes que precisam de classes.
    def __init__(self, nome, equipe=None):
        self.__nome = nome
        self.__ataque_equipe = 0
        self.__hp_equipe = 0
        self.__pokemons_capturados = [] #! isso não deve estar aqui, mas sim na classe pokémon ou treinador... a classe que conter a lista de pokemons capturados. corrigir posteriormente
        self.__set_equipe(equipe)

    def get_pokemons_capturados(self):
        return self.__pokemons_capturados
    
    #! método temporário e incompleto, apenas para fins de teste. funciona somente nessa estrutura. necessário mergir com a de vic
    def __set_equipe(self, equipe):
        if equipe is None:
            self.__equipe = []
        elif len(equipe) > 3:
            raise ValueError("O equipe não pode ter mais do que 3 Pokémons.")
        else:
            self.__equipe = equipe
        self.__ataque_equipe = self.calcular_ataque_equipe()
        self.__hp_equipe = self.calcular_hp_equipe()

    #! método deve ser corrigido para ir para o controlador respectivo que tem acesso aos pokémons capturados.
    def captura_pokemon(self, pokemon):
        if pokemon in self.__pokemons_capturados:
            print(f"Você já capturou o {pokemon.nome} antes!")
        else:
            self.__pokemons_capturados.append(pokemon)
            print(f"\nParabéns, você capturou o {pokemon.nome}!")

    #! método temporário e incompleto, apenas para fins de teste. funciona somente nessa estrutura. necessário mergir com a de vic
    #! a mensagem assim vale para todos os métodos abaixo até a divisória.
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
    
   
    def restaurar_hp_equipe(self):
        self.__hp_equipe = self.calcular_hp_equipe()

   
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
        capturados = [p.num for p in self.__pokemons_capturados]
        return numero_pokemon in capturados
    
    @property
    def equipe(self):
        return self.__equipe
    
    
    @equipe.setter
    def equipe(self, equipe):
        self.__set_equipe = equipe
    
    
    @property
    def nome(self):
        return self.__nome'''

    #! ###########################################################################################

#############################################################
####################### BAGUNÇA TOTAL #######################
#############################################################

#?      provavelmente dá pra usar isso na classe abstract tela? aí todos os títulos ficariam padronizados.
def titulo(mensagem):
    #titulo = "Batalha Pokémon"
    linha_separadora = "=" * 80
    print(f"\n{linha_separadora}\n{mensagem.center(len(linha_separadora))}\n{linha_separadora}")

class CapturaPokemon:
    # ? tentei assim, mas não sei se tá correto. 
    #! APAGAR O QUE NÃO DEVE ESTAR AQUI, MAS SIM NO CONTROLADOR DEPOIS. 
    def __init__(self, treinador: Treinador):
        if (isinstance(treinador, Treinador)):
            self.__treinador = treinador
        self.__oponente = None

    def escolher_pokemon_aleatorio(self):
        pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        return pokemon_aleatorio
        #return Pokemon(pokemon_aleatorio.nome, pokemon_aleatorio.num, pokemon_aleatorio.hp, pokemon_aleatorio.ataque)

    def iniciar_batalha(self):
        global win, derrotas
        capturado = False
        rodada = 0
        
        titulo('Batalha Pokémon')

        oponente = self.escolher_pokemon_aleatorio()
        #num = oponente.num
        print(f"\nUm {oponente.nome} selvagem apareceu!")
        
        if self.__treinador.verifica_numero_pokemon_capturado(oponente.num):
            capturado = True
            resposta = input(f"\n[ATENÇÃO] Você já capturou um Pokémon {oponente.nome} #{oponente.num} antes. Você deseja fugir da batalha? \n1 - Sim     2 - Não\n")
            if resposta == '1':
                print("\nVocê saiu da batalha.")
                return
        else:
            capturado = False
        
        #usando 'selvagem' como referencia aos jogos

        hp_original = oponente.hp
        ataque_original = oponente.ataque

        tamanho_equipe = len(self.__treinador.equipe)

        multiplicador = random.choice([tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, 4, 4, 4, 5,5])
        oponente.hp = int(oponente.hp * multiplicador)

        multiplicador_ataque = random.choice([2,2,2,3,3,3,4])
        oponente.ataque = int(oponente.ataque * multiplicador_ataque)

        print(f"O {oponente.nome} selvagem tem {oponente.ataque} de ataque (*{multiplicador_ataque}) e {oponente.hp} de HP (*{multiplicador})! ")
        
        print(f"\n{self.__treinador.nome}, sua equipe possui {self.__treinador.ataque_equipe} de ataque e {self.__treinador.hp_equipe} de HP.\n")

        #treinador sempre ataca primeiro. se der tempo:
        #* implementar algo que aleatoriza quem ataca primeiro.
        while self.__treinador.hp_equipe > 0 and oponente.hp > 0:
            rodada += 1
            print(f'\nRodada {rodada}')
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

                print(f"\nO {oponente.nome} está desmaiado! ({oponente.hp} de hp restantes!) - ({oponente.ataque} de ataque)")
                print(f"\n{self.__treinador.nome} GANHOU 💙 a batalha!")
                self.__treinador.restaurar_hp_equipe()   

                oponente.hp = hp_original
                oponente.ataque = ataque_original
                win += 1
                
                if capturado == False:
                    self.tentar_captura(oponente)
                
                self.__treinador.restaurar_hp_equipe()
                break

            # turno do Pokémon selvagem
            if oponente.hp > 0:
                print(f"\nO {oponente.nome} selvagem tem {oponente.hp}HP restantes! - ({oponente.ataque} de ataque)")
                print(f"O {oponente.nome} selvagem ataca!\n")
                self.__treinador.hp_equipe -= oponente.ataque
            
            if self.__treinador.hp_equipe < 0: 
                self.__treinador.hp_equipe = 0

                print(f"\n{self.__treinador.nome}, sua equipe está desmaiada! ({self.__treinador.hp_equipe} de hp restantes!)")
                print("\nVocê PERDEU 💔 a batalha.")
                self.__treinador.restaurar_hp_equipe()           
                
                oponente.hp = hp_original
                oponente.ataque = ataque_original
                derrotas += 1
                
                break
        
            
    def tentar_captura(self, pokemon):
        #escolha = input(f'Deseja tentar capturar {pokemon.nome}? ').upper() #! apagar esse comentário e a linha abaixo depois
        escolha = 'S' #! temporário, apenas para fins de praticidade nos testes
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