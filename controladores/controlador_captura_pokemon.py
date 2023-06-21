
#* Tratamentos CHECK

from telas.tela_captura_pokemon import TelaCaptura
from entidades.captura_pokemon import CapturaPokemon
from DAO.captura_dao import CapturaDAO

from exceptions.pokemon_inexistente_exception import PokemonInexistenteException
from exceptions.nickname_nao_encontrado_exception import NicknameNaoEncontradoException
import random

class ControladorCaptura():
    #capturas = []
    captura_DAO = CapturaDAO()
    logs_treinadores = {}

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
        self.__controlador_sistema.controlador_treinadores.pega_porcentagem(treinador)

    def escolher_pokemon_aleatorio(self):
        #pokemon_aleatorio = random.choice(ControladorPokemon.lista_pokemons)
        pokemon_aleatorio = random.choice(self.__controlador_sistema.controlador_pokemon.lista_pokemons)
        return pokemon_aleatorio

    def inicia_batalha(self):

        while True:
            try: #checa se o nome do treinador digitado existe na lista de treinadores
                nickname = self.__tela_captura.pega_dados_treinador(self.__controlador_sistema.controlador_treinadores.nome_treinadores())
                if nickname is None:
                    return
                treinador = self.__controlador_sistema.controlador_treinadores.pega_treinador_por_nickname(nickname)
                if treinador is not None:
                    break
                else:
                    raise NicknameNaoEncontradoException(nickname)
            except NicknameNaoEncontradoException as e:
                self.__tela_captura.mostra_mensagem(e)
                self.__tela_captura.mostra_mensagem('Tente novamente.')
        
        capturado = False
        rodada = 0

        self.__tela_captura.titulo('Batalha Pokémon')

        pokemon_oponente = self.escolher_pokemon_aleatorio()
        num = pokemon_oponente.num

        self.__tela_captura.mostra_popup(f'Você encontrou um {pokemon_oponente.nome}!', '???')

        time = treinador.time 
        info_pokemons_time = [pokemon.nome for pokemon in treinador.time.lista_pokemons]  # Lista com nomes dos Pokémon da time do treinador
            
        info_batalha = {
                'treinador': treinador.nickname,
                'pokemons_time': info_pokemons_time, 
                'pokemon_oponente': pokemon_oponente.nome,
                'resultado_batalha': None,  
                'resultado_captura': None  
            }
        
        #* usando 'selvagem' como referencias aos jogos
        #self.__tela_captura.mostra_mensagem(f"\n[❓❔❓] Um {pokemon_oponente.nome} selvagem apareceu! [❓❔❓]")
        
        #tela1 pokemon capturado
        capturado = treinador.verifica_numero_pokemon_capturado(num)
        
        

        treinador.hp_time = treinador.calcular_hp_time()
        treinador.ataque_time = treinador.calcular_ataque_time()

        if treinador.ataque_time == 0 or treinador.hp_time == 0 or treinador.ataque_time == None or treinador.hp_time == None:
            self.__tela_captura.mostra_popup('[!!!] Você provavelmente esqueceu de adicionar pokémons ao seu time!')
            return
        
        #salva os hps originais do pokemon. talvez dê pra corrigir depois de alguma maneira mais bonita
        hp_original = pokemon_oponente.hp
        ataque_original = pokemon_oponente.ataque    #! talvez não seja necessário mais visto q é o pokémon aleatório esta sendo reinstanciado. 

        tamanho_time = len(treinador.time.lista_pokemons) #provavelmente o nome vai voltar pra time
        
        #talvez dê pra fazer um método que faça esses multiplicadores isso de um jeito mais bonito
        multiplicador_hp = random.choice([tamanho_time, tamanho_time, tamanho_time, tamanho_time, tamanho_time, 4, 4, 4, 5,5])
        pokemon_oponente.hp = int(pokemon_oponente.hp * multiplicador_hp)

        multiplicador_ataque = random.choice([2,2,2,3,3,3,4])
        pokemon_oponente.ataque = int(pokemon_oponente.ataque * multiplicador_ataque)
    
        #self.__tela_captura.mostra_mensagem(f"\nO {pokemon_oponente.nome} selvagem tem {pokemon_oponente.ataque} de ataque (*{multiplicador_ataque}) e {pokemon_oponente.hp} de HP (*{multiplicador_hp})! ")

        self.__tela_captura.pokemon_encontrado(pokemon_oponente, capturado, treinador) #! perguntar para Thaís se posso fazer isso ou se fere o mvc

        if capturado:
            info_batalha['resultado_captura'] = 'Já capturado anteriormente'
            #fugir_batalha = self.__tela_captura.le_num_inteiro(f"\n[⚠️  ] Você já capturou um Pokémon {pokemon_oponente.nome} #{pokemon_oponente.num} antes. Você deseja fugir da batalha?\n   1 - Sim     2 - Não\n", [1, 2])
            
            fugir_batalha = self.__tela_captura.pokemon_ja_capturado(pokemon_oponente)
            
            if fugir_batalha == True:
                info_batalha['resultado_batalha'] = 'Fugiu'
                self.__tela_captura.mostra_popup("Você fugiu da batalha.",'💨💨💨')
                self.add_captura(info_batalha)  # Salva as informações da batalha no log
                return

        #self.__tela_captura.mostra_mensagem(f"\n{treinador.nickname}, seu time possui {treinador.ataque_time} de ataque e {treinador.hp_time} de HP.")

        
        # treinador sempre ataca primeiro. 
        #aqui inicia a batalha propriamente
        while treinador.hp_time > 0 and pokemon_oponente.hp > 0:
            rodada += 1

            self.__tela_captura.rodada_popup(f'Rodada {rodada}', 1)

            #* treinador ataca.
            time_ataques = []

            for pokemon in treinador.time.lista_pokemons:
                if pokemon.hp > 0:
                    #self.__tela_captura.mostra_mensagem(f"{pokemon.nome} ataca!")
                    #self.__tela_captura.pokemons_atacando(pokemon.nome, 1)
                    time_ataques.append(pokemon)
                    pokemon_oponente.hp -= pokemon.ataque * 10
                    if pokemon_oponente.hp <= 0:
                        break
                    
            self.__tela_captura.time_ataca(time_ataques)
            
            if pokemon_oponente.hp <= 0:
                pokemon_oponente.hp = 0 #apenas para evitar printar um valor negativo de hp.

                msg_oponente = (f"O {pokemon_oponente.nome} está desmaiado!") 
                msg_hp = (f'REF: {pokemon_oponente.hp} ❤️ restantes. {pokemon_oponente.ataque} 🗡️')
                
                self.__tela_captura.resultado_batalha_popup(msg_oponente, msg_hp)
                
                self.__tela_captura.mostra_popup(f"🥇 {treinador.nickname} ganhou a batalha!","🎉🎉🎉")

                info_batalha['resultado_batalha'] = 'Vitória'
                #self.add_captura(info_batalha)
                treinador.restaurar_hp_time() #método que restaura a vida dos pokemons do time para o valor original
                
                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                #win += 1

                if capturado == False:
                    self.tentar_captura(pokemon_oponente, info_batalha, treinador)

                else: #não estava funcionando de outra maneira
                    self.__tela_captura.mostra_popup('Você já capturou esse pokémon antes, portanto não pode capturá-lo de novo!', 'Pokémon já capturado')
                    info_batalha['resultado_captura'] = 'Já capturado anteriormente'
                    self.add_captura(info_batalha)
                #self.__tela_captura.digite_para_continuar() # como não consigo usar a função sleep
                treinador.restaurar_hp_time() #* função do treinador que cura os pokemons
                break
            
            #* pokemom selvagem ataca
            if pokemon_oponente.hp > 0:
                #self.__tela_captura.mostra_mensagem(f'\n O {pokemon_oponente.nome} selvagem tem {pokemon_oponente.hp}HP restantes e {pokemon_oponente.ataque} de ataque!')
                #self.__tela_captura.mostra_mensagem(f'{pokemon_oponente.nome} selvagem ataca!\n')
                self.__tela_captura.oponente_ataca(pokemon_oponente)
                treinador.hp_time -= pokemon_oponente.ataque #talvez um método que diminua o hp do time?

            if treinador.hp_time < 0:
                treinador.hp_time = 0

                #self.__tela_captura.mostra_mensagem(f'💤 {treinador.nickname}, seu time está desmaiada!') 
                #self.__tela_captura.mostra_mensagem(f'{treinador.hp_time} de hp restantes!') #! teste, apagar depois
                msg_time = (f'💤 {treinador.nickname}, seu time está desmaiado! 💤')
                msg_hp = (f'{treinador.hp_time} ❤️ restantes!')
                
                self.__tela_captura.resultado_batalha_popup(msg_time, msg_hp)


                self.__tela_captura.mostra_popup(f'💔 Você perdeu a batalha.', '💥💥💥')
                info_batalha['resultado_batalha'] = 'Derrota'
                info_batalha['resultado_captura'] = '---'
                self.add_captura(info_batalha)
                treinador.restaurar_hp_time()

                pokemon_oponente.hp = hp_original
                pokemon_oponente.ataque = ataque_original
                #derrotas += 1
                #self.__tela_captura.digite_para_continuar()
                break

    def tentar_captura(self, pokemon, info_batalha, treinador):
        escolha_captura = self.__tela_captura.popup_sim_nao(f"Deseja tentar capturar {pokemon.nome}?", "🎱🎱🎱")
        
        if escolha_captura == True:
            chance_captura = random.randint(1,100) #gera um número aleatório entre 1 e 100.
            self.__tela_captura.mostra_popup('Pokebola lançada...', 'Pokebola')

            if chance_captura >= 2:
                treinador.add_pokemon_capturado(pokemon)
                dao = self.__controlador_sistema.controlador_treinadores.treinador_DAO()
                
                #print(treinador)
                dao.update(treinador)

                self.__tela_captura.mostra_popup(f'Você tirou {chance_captura} e conseguiu capturar {pokemon.nome}! Parabéns!!!', "Capturado")
                info_batalha['resultado_captura'] = "Capturado! "

                self.__controlador_sistema.controlador_treinadores.pega_porcentagem(treinador)
                
                #self.__controlador_sistema.controlador_treinadores.__treinador_DAO.update(treinador)
                #preciso dar dump no arquivo de pokemons capturados
                #para fazerr isso 

            else:
                self.__tela_captura.mostra_popup(f'Que pena, o {pokemon.nome} escapou...', "Fugiu")
                info_batalha['resultado_captura'] = "Pokémon fugiu da Pokébola"
        else:
            info_batalha['resultado_captura'] = "Não quis capturar."
        self.add_captura(info_batalha)

    def add_captura(self, info_batalha):
        self.captura_DAO.add(info_batalha)
        treinador = info_batalha['treinador']
        if treinador not in self.logs_treinadores:
            self.logs_treinadores[treinador] = []
        self.logs_treinadores[treinador].append(info_batalha)
        self.__tela_captura.mostra_popup("Um novo registro foi adicionado com sucesso nos logs!", "Registro")
    
    def log_capturas(self):
        if len(self.captura_DAO) == 0:
            self.__tela_captura.mostra_popup("Nenhuma captura registrada até o momento.")
        else:
            self.__tela_captura.titulo3("Registro de Capturas Gerais:")
            dados_captura = []
            for captura in self.captura_DAO:
                '''self.__tela_captura.mostra_mensagem(f"\nTreinador: {captura['treinador']}")
                self.__tela_captura.mostra_mensagem(f"   Pokémons no time: {captura['pokemons_time']}")
                self.__tela_captura.mostra_mensagem(f"   Pokémon Oponente: {captura['pokemon_oponente']}")
                self.__tela_captura.mostra_mensagem(f"   Resultado da Batalha: {captura['resultado_batalha']}")
                self.__tela_captura.mostra_mensagem(f"   Resultado da Captura: {captura['resultado_captura']}")'''
                dados_captura.append([captura['treinador'], captura['pokemons_time'], captura['pokemon_oponente'], captura['resultado_batalha'], captura['resultado_captura']])     
            self.__tela_captura.log_geral(dados_captura)

    def log_treinador(self, nickname = None):
        nickname = self.__tela_captura.pega_dados_treinador(self.__controlador_sistema.controlador_treinadores.nome_treinadores())
        if nickname not in self.logs_treinadores or len(self.logs_treinadores[nickname]) == 0:
            self.__tela_captura.mostra_popup(f"Nenhuma captura registrada para o treinador {nickname}.")
        else:
            self.__tela_captura.titulo3(f"Registro de Capturas - Treinador {nickname}:")
            dados_captura = []
            for captura in self.logs_treinadores[nickname]:
                dados_captura.append(captura)

                '''self.__tela_captura.mostra_mensagem(f"\nTreinador: {captura['treinador']}")
                self.__tela_captura.mostra_mensagem(f"   Pokémons no time: {captura['pokemons_time']}")
                self.__tela_captura.mostra_mensagem(f"   Pokémon Oponente: {captura['pokemon_oponente']}")
                self.__tela_captura.mostra_mensagem(f"   Resultado da Batalha: {captura['resultado_batalha']}")
                self.__tela_captura.mostra_mensagem(f"   Resultado da Captura: {captura['resultado_captura']}")'''
            self.__tela_captura.log_treinador(nickname, dados_captura)

    def ranking_treinadores(self):
        if not self.logs_treinadores:
            self.__tela_captura.mostra_popup("Nenhuma captura registrada até o momento.")
        else:
            self.__tela_captura.titulo3("Ranking de Treinadores com mais Capturas:")
            ranking = sorted(self.logs_treinadores.items(), key=lambda x: sum(captura['resultado_captura'] == "Capturado! " for captura in x[1]), reverse=True)
            for i, (treinador, capturas) in enumerate(ranking, start=1):
                self.__tela_captura.mostra_mensagem(f"{i}. Treinador: {treinador}")
                self.__tela_captura.mostra_mensagem(f"   Total de Batalhas: {len(capturas)}")
                soma_capturas_com_sucesso = sum(captura['resultado_captura'] == "Capturado! " for captura in capturas)
                self.__tela_captura.mostra_mensagem(f"   Total de Capturas: {soma_capturas_com_sucesso}")
                taxa_de_vitória = float(soma_capturas_com_sucesso/len(capturas)) * 100
                self.__tela_captura.mostra_mensagem(f"   Taxa de Vitória: {taxa_de_vitória:.1f}%")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inicia_batalha, 2: self.log_capturas, 3: self.log_treinador, 4: self.ranking_treinadores, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_captura.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.retornar()