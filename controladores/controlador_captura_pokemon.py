
from exceptions.pokemon_inexistente import PokemonInexistente
from telas.tela_captura_pokemon import TelaCaptura
from entidades.captura_pokemon import *

class ControladorCaptura():
    capturas = []
    
    def __init__(self):   #! posteriomente recebe controlador_sistema
        self.__tela_captura = TelaCaptura()
        # * self.__controlador_sistema = controlador_sistema

    def escolher_pokemon_aleatorio(self):
        pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        return Pokemon(pokemon_aleatorio.nome, pokemon_aleatorio.num, pokemon_aleatorio.hp, pokemon_aleatorio.ataque)
    
    def inicia_batalha(self):
        capturado = False
        rodada = 0

        self.__tela_captura.titulo('Batalha Pokémon')

        pokemon_oponente = self.escolher_pokemon_aleatorio()
        num = pokemon_oponente.num

        #* usando 'selvagem' como referencias aos jogos
        self.__tela_captura.mostra_mensagem(f"\n[❓❔❓] Um {pokemon_oponente.nome} selvagem apareceu!")

        if self.__treinador.verifica_numero_pokemon_capturado(num): #* codigo implementado de vic
            capturado = True
            fugir_batalha = self.__tela_captura.le_num_inteiro(f"\n[ATENÇÃO] Você já capturou um Pokémon {pokemon_oponente.nome} #{pokemon_oponente.num} antes. Você deseja fugir da batalha?\n1 - Sim     2 - Não\n",[1,2])
            if fugir_batalha == '1':
                self.__tela_captura.mostra_mensagem("\nVocê fugiu da batalha.")
                return
        else:
            capturado = False
    
        #salva os hps originais do pokemon. talvez dê pra corrigir depois de alguma maneira mais bonita
        hp_original = pokemon_oponente.hp
        ataque_original = pokemon_oponente.ataque

        #talvez fazer um método na classe treinador para ver o tamanho da len e retornar ele.
        tamanho_equipe = len(self.__treinador.equipe) #provavelmente o nome vai voltar pra time
        
        #talvez dê pra fazer um método que faça esses multiplicadores isso de um jeito mais bonito
        multiplicador_hp = random.choice([tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, tamanho_equipe, 4, 4, 4, 5,5])
        pokemon_oponente.hp = int(pokemon_oponente.hp * multiplicador_hp)

        multiplicador_ataque = random.choice([2,2,2,3,3,3,4])
        pokemon_oponente.ataque = int(pokemon_oponente.ataque * multiplicador_ataque)
    
        self.__tela_captura.mostra_mensagem(f"O {pokemon_oponente.nome} selvagem tem {pokemon_oponente.ataque} de ataque (*{multiplicador_ataque}) e {pokemon_oponente.hp} de HP (*{multiplicador_hp})! ")

        self.__tela_captura.mostra_mensagem(f"\n {self.__treinador.nome}, sua equipe possui {self.__treinador.ataque_equipe} de ataque e {self.__treinador.hp_equipe} de HP.\n")

        # treinador sempre ataca primeiro. se der tempo:
        # * implementar uma aleatorização de quem ataca primeiro.

        while self.__treinador.hp_equipe > 0 and pokemon_oponente.hp > 0:
            rodada += 1
            self.__tela_captura.mostra_mensagem(f'\n Rodada {rodada}')

            equipe = self.__treinador.equipe 
            
            #* treinador ataca.
            for pokemon in equipe:
                if pokemon.hp > 0:
                    print(f"{pokemon.nome} ataca!")
                    pokemon_oponente.hp -= pokemon.ataque
                    if pokemon_oponente.hp <= 0:
                        break
            
            if pokemon_oponente.hp <= 0:
                pokemon_oponente.hp = 0 #apenas para evitar printar um valor negativo de hp.

                self.__tela_captura.mostra_mensagem(f"\n💤 O {pokemon_oponente.nome} está desmaiado! \nREF: {pokemon_oponente.hp} de hp restantes. {pokemon_oponente.ataque} de ataque")
                self.__tela_captura.mostra_mensagem(f"\n🎉 {self.__treinador.nome} ganhou a batalha!")
                self.__treinador.restaurar_hp_equipe() #método que restaura a vida dos pokemons do time para o valor original
                
                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                win += 1

                if capturado == False:
                    self.tentar_captura(pokemon_oponente)

                self.__treinador.restaurar_hp_equipe() #* função do treinador que cura os pokemons
                break
            
            #* pokemom selvagem ataca
            if pokemon_oponente.hp > 0:
                self.__tela_captura.mostra_mensagem(f'\n O {pokemon_oponente.hp} selvagem tem {pokemon_oponente.hp}HP restantes e {pokemon_oponente.ataque} de ataque!')
                self.__tela_captura.mostra_mensagem(f'{pokemon_oponente.nome} selvagem ataca!\n')
                self.__treinador.hp_equipe -= pokemon_oponente.ataque #talvez um método que diminua o hp do time?

            if self.__treinador.hp_equipe < 0:
                self.__treinador.hp_equipe = 0

                self.__tela_captura.mostra_mensagem(f'💤 {self.__treinador.nome}, sua equipe está desmaiada!') 
                print(f'{self.__treinador.hp_equipe} de hp restantes!') #! teste, apagar depois
                self.__tela_captura.mostra_mensagem(f'\n💥Você perdeu a batalha.')
                self.__treinador.restaurar_hp_equipe()

                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                derrotas += 1

                break

    def tentar_captura(self, pokemon):
        escolha_captura = self.__tela_captura.le_num_inteiro(f"Deseja tentar capturar {pokemon.nome}?\n1 - Sim     2 - Não\n",[1,2])
        if escolha_captura == 1:
            chance_captura = random.randint(1,100) #gera um número aleatório entre 1 e 100.
            self.__tela_captura.mostra_mensagem('Pokebola lançada...')

            if chance_captura >= 25:
                self.__treinador.captura_pokemon(pokemon)
                self.__tela_captura.mostra_mensagem(f'Você tirou {chance_captura} e conseguiu capturar {pokemon.nome}! Parabéns!!!')
                
                escolha_mostra_pokemons_capturados = self.__tela_captura.le_num_inteiro(f"Deseja ver todos os pokémons capturados até o momento?\n1 - Sim     2 - Não\n",[1,2])
                if escolha_mostra_pokemons_capturados == 1:
                    pass #* implementar função que mostra os pokemons capturados
                    #* imagino que deva pegar de treinador
                    #* chamar a função que mostra todos os pokemons capturados
            else:
                self.__tela_captura.mostra_mensagem(f'\n Que pena, o {pokemon.nome} escapou...')
        else:
            return

    def add_captura():
        pass

    def del_captura():
        pass
    
    def log_capturas():
        pass

    def retornar(self):
        exit() # ! - Temporário, alterar para retornar ao controladorSistema depois.

    def abre_tela(self):
        lista_opcoes = {1: self.inicia_batalha, 2: self.log_capturas, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_captura.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
