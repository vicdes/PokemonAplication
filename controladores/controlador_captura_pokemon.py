
from exceptions.pokemon_inexistente_exception import PokemonInexistenteException
from telas.tela_captura_pokemon import TelaCaptura
from entidades.captura_pokemon import *




class ControladorCaptura():
    capturas = []
    
    def __init__(self, controlador_sistema):   #! posteriomente recebe controlador_sistema
        self.__tela_captura = TelaCaptura()
        self.__controlador_sistema = controlador_sistema

    def captura_pokemon_inicial(self, nickname=None):
        codigo_inicial = self.__tela_captura.seleciona_pokemon_inicial()
        treinador = self.__controlador_sistema.controlador_treinadores.pega_treinador_por_nickname(nickname)
        novo_pokemon = None
        for pokemon in self.__controlador_sistema.controlador_pokemon.lista_pokemons_iniciais:
            if pokemon.num == codigo_inicial:
                novo_pokemon = pokemon
                break
        try:
            if novo_pokemon is not None:
                pass
            else:
                raise PokemonInexistenteException(codigo_inicial)
        except PokemonInexistenteException as e:
            self.__tela_captura.mostra_mensagem(e)
        treinador.pokemons_capturados.append(novo_pokemon)

    def escolher_pokemon_aleatorio(self):
        pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        return Pokemon(pokemon_aleatorio.nome, pokemon_aleatorio.num, pokemon_aleatorio.hp, pokemon_aleatorio.ataque, pokemon_aleatorio.tipos)
    
    
    def inicia_batalha(self):
        nickname = self.__tela_captura.pega_dados_captura()
        treinador = self.__controlador_sistema.controlador_treinadores.pega_treinador_por_nickname(nickname)
        
        capturado = False
        rodada = 0

        self.__tela_captura.titulo('Batalha Pokémon')

        pokemon_oponente = self.escolher_pokemon_aleatorio()
        num = pokemon_oponente.num

        time = treinador.time 
        info_pokemons_time = [pokemon.nome for pokemon in treinador.time.lista_pokemons]  # Lista com nomes dos Pokémon da time do treinador
            
        info_batalha = {
                'treinador': treinador.nickname,
                'pokemons_time': info_pokemons_time, 
                'pokemon_oponente': pokemon_oponente.nome,
                'resultado_batalha': None,  
                'resultado_captura': None  
            }

        '''capturado = False
        rodada = 0

        self.__tela_captura.titulo('Batalha Pokémon')

        pokemon_oponente = self.escolher_pokemon_aleatorio()
        num = pokemon_oponente.num'''

        #* usando 'selvagem' como referencias aos jogos
        self.__tela_captura.mostra_mensagem(f"\n[❓❔❓] Um {pokemon_oponente.nome} selvagem apareceu! [❓❔❓]")

        if treinador.verifica_numero_pokemon_capturado(num): #* codigo implementado de vic
            capturado = True
            info_batalha['resultado_captura'] = 'Já capturado anteriormente'
            fugir_batalha = self.__tela_captura.le_num_inteiro(f"\n[⚠️  ] Você já capturou um Pokémon {pokemon_oponente.nome} #{pokemon_oponente.num} antes. Você deseja fugir da batalha?\n   1 - Sim     2 - Não\n",[1,2])
            if fugir_batalha == '1':
                info_batalha['resultado_batalha'] = 'Fugiu'
                
                self.__tela_captura.mostra_mensagem("\nVocê fugiu da batalha.")
                return
        else:
            capturado = False

        treinador.hp_time = treinador.calcular_hp_time()
        treinador.ataque_time = treinador.calcular_ataque_time()

        #salva os hps originais do pokemon. talvez dê pra corrigir depois de alguma maneira mais bonita
        hp_original = pokemon_oponente.hp
        ataque_original = pokemon_oponente.ataque    #! talvez não seja necessário mais visto q é o pokémon aleatório esta sendo reinstanciado. 

        #talvez fazer um método na classe treinador para ver o tamanho da len e retornar ele.
        tamanho_time = len(treinador.time.lista_pokemons) #provavelmente o nome vai voltar pra time
        print(f'tamanho do time de {treinador.nickname} = {tamanho_time}') #! APAGAR
        #talvez dê pra fazer um método que faça esses multiplicadores isso de um jeito mais bonito
        multiplicador_hp = random.choice([tamanho_time, tamanho_time, tamanho_time, tamanho_time, tamanho_time, 4, 4, 4, 5,5])
        pokemon_oponente.hp = int(pokemon_oponente.hp * multiplicador_hp)

        multiplicador_ataque = random.choice([2,2,2,3,3,3,4])
        pokemon_oponente.ataque = int(pokemon_oponente.ataque * multiplicador_ataque)
    
        self.__tela_captura.mostra_mensagem(f"\nO {pokemon_oponente.nome} selvagem tem {pokemon_oponente.ataque} de ataque (*{multiplicador_ataque}) e {pokemon_oponente.hp} de HP (*{multiplicador_hp})! ")

        self.__tela_captura.mostra_mensagem(f"\n{treinador.nickname}, seu time possui {treinador.ataque_time} de ataque e {treinador.hp_time} de HP.")

        # treinador sempre ataca primeiro. se der tempo:
        # * implementar uma aleatorização de quem ataca primeiro.

        while treinador.hp_time > 0 and pokemon_oponente.hp > 0:
            rodada += 1
            self.__tela_captura.mostra_mensagem(f'\n[ Rodada {rodada} ]\n')

            #! TREINADOR.TIME.LISTA_POKEMON

            #* treinador ataca.
            for pokemon in treinador.time.lista_pokemons:
                if pokemon.hp > 0:
                    self.__tela_captura.mostra_mensagem(f"{pokemon.nome} ataca!")
                    pokemon_oponente.hp -= pokemon.ataque
                    if pokemon_oponente.hp <= 0:
                        break
            
            if pokemon_oponente.hp <= 0:
                pokemon_oponente.hp = 0 #apenas para evitar printar um valor negativo de hp.

                self.__tela_captura.mostra_mensagem(f"\n💤 O {pokemon_oponente.nome} está desmaiado! \nREF: {pokemon_oponente.hp} de hp restantes. {pokemon_oponente.ataque} de ataque")
                self.__tela_captura.mostra_mensagem(f"\n🎉 {treinador.nickname} ganhou a batalha!")
                info_batalha['resultado_batalha'] = 'Vitória'
                #self.add_captura(info_batalha)
                treinador.restaurar_hp_time() #método que restaura a vida dos pokemons do time para o valor original
                
                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                #win += 1

                if capturado == False:
                    self.tentar_captura(pokemon_oponente, info_batalha, treinador)

                treinador.restaurar_hp_time() #* função do treinador que cura os pokemons
                break
            
            #* pokemom selvagem ataca
            if pokemon_oponente.hp > 0:
                self.__tela_captura.mostra_mensagem(f'\n O {pokemon_oponente.nome} selvagem tem {pokemon_oponente.hp}HP restantes e {pokemon_oponente.ataque} de ataque!')
                self.__tela_captura.mostra_mensagem(f'{pokemon_oponente.nome} selvagem ataca!\n')
                treinador.hp_time -= pokemon_oponente.ataque #talvez um método que diminua o hp do time?

            if treinador.hp_time < 0:
                treinador.hp_time = 0

                self.__tela_captura.mostra_mensagem(f'💤 {treinador.nickname}, seu time está desmaiada!') 
                print(f'{treinador.hp_time} de hp restantes!') #! teste, apagar depois
                self.__tela_captura.mostra_mensagem(f'\n💥Você perdeu a batalha.')
                info_batalha['resultado_batalha'] = 'Derrota'
                info_batalha['resultado_captura'] = '---'
                self.add_captura(info_batalha)
                treinador.restaurar_hp_time()

                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                #derrotas += 1

                break

    def tentar_captura(self, pokemon, info_batalha, treinador):
        escolha_captura = self.__tela_captura.le_num_inteiro(f"\n[🎱 ] Deseja tentar capturar {pokemon.nome}?\n   1 - Sim     2 - Não\n",[1,2])
        if escolha_captura == 1:
            chance_captura = random.randint(1,100) #gera um número aleatório entre 1 e 100.
            self.__tela_captura.mostra_mensagem('\nPokebola lançada...')

            if chance_captura >= 25:
                treinador.add_pokemon_capturado(pokemon)
                self.__tela_captura.mostra_mensagem(f'Você tirou {chance_captura} e conseguiu capturar {pokemon.nome}! Parabéns!!!')
                info_batalha['resultado_captura'] = "Capturado! "
                self.add_captura(info_batalha)
                escolha_mostra_pokemons_capturados = self.__tela_captura.le_num_inteiro(f"\nDeseja ver todos os pokémons capturados até o momento?\n   1 - Sim     2 - Não\n",[1,2])
                if escolha_mostra_pokemons_capturados == 1:
                    treinador.mostrar_pokemons_capturados()
            else:
                self.__tela_captura.mostra_mensagem(f'\nQue pena, o {pokemon.nome} escapou...')
                info_batalha['resultado_captura'] = "Pokémon fugiu da Pokébola"
                self.add_captura(info_batalha)
        else:
            info_batalha['resultado_captura'] = "Não quis capturar."
            self.add_captura(info_batalha)
            return


    def add_captura(self, info_batalha): 
        self.capturas.append(info_batalha)
        self.__tela_captura.mostra_mensagem("\nUm novo registro foi adicionado com sucesso nos logs!")
    
    def log_capturas(self):
        if len(self.capturas) == 0:
            self.__tela_captura.mostra_mensagem("\n[!] Nenhuma captura registrada até o momento.")
        else:
            self.__tela_captura.titulo3("Registro de Capturas:")
            for captura in self.capturas:
                self.__tela_captura.mostra_mensagem(f"\nTreinador: {captura['treinador']}")
                self.__tela_captura.mostra_mensagem(f"Pokémons no time: {captura['pokemons_time']}")
                self.__tela_captura.mostra_mensagem(f"Pokémon Oponente: {captura['pokemon_oponente']}")
                self.__tela_captura.mostra_mensagem(f"Resultado da Batalha: {captura['resultado_batalha']}")
                self.__tela_captura.mostra_mensagem(f"Resultado da Captura: {captura['resultado_captura']}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inicia_batalha, 2: self.log_capturas, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_captura.tela_opcoes()
            if opcao_escolhida == 1:
                self.inicia_batalha()
            elif opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.retornar()