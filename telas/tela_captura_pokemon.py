
from telas.tela_abstract import AbstractTela
import PySimpleGUI as sg
import time

class TelaCaptura(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    '''def tela_opcoes(self):
        self.titulo('Tela Captura')
        print("\nEscolha sua opcao")
        print("  1 - Procurar Pokémons nas redondezas")
        print("\n  2 - Log Geral")
        print("  3 - Log Treinador")
        print("  4 - Ranking de Treinadores")
        print("\n  0 - Retornar")

        opcao = self.le_num_inteiro("\nEscolha a opção: ", [1, 2, 3, 4, 0]) #* tratamento de exceção FEITO
        return opcao'''

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('-------- Captura Pokémon ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Procurar pokémon', "RD1", key='1')],
            [sg.Radio('Log Geral', "RD1", key='2')],
            [sg.Radio('Log Treinador', "RD1", key='3')],
            [sg.Radio('Ranking', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Captura').Layout(layout)

    '''def digite_para_continuar(self):
        input('\nAperte qualquer coisa para continuar...') #apenas pra dar uma pausa antes de retornar a tela
    '''
    '''def pega_dados_captura(self): #* tratamento de exceção FEITO
        self.titulo2("Dados Captura") 
        nickname = input("\nNickname do treinador: ")
        sg.ChangeLookAndFeel('DarkAmber')

        layout = [
            [sg.Text('Nickname: ', size=(15,1)), sg.InputText('',key='nickname')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Treinador').Layout(layout)

        button, values = self.open()
        nickname = values['nickname']

        self.close()
        return nickname'''

    def seleciona_pokemon_inicial(self): #* tratamento de exceção FEITO
        codigo_inicial = self.le_num_inteiro("\nDigite o código do pokémon que deseja selecionar:\n#1 Bulbasaur\n#4 Charmander\n#7 Squirtle\n", [1,4,7]) 
        return codigo_inicial

    def pega_dados_treinador(self, treinadores):
        sg.ChangeLookAndFeel('DarkAmber')
        lista_treinadores = treinadores
        '''layout = [
            [sg.Text('Nickname: ', size=(15,1)), sg.InputText('',key='nickname')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dado Treinador').Layout(layout)'''
        layout = [
        [sg.Text('Nickname: ', size=(15,1)), sg.Combo(lista_treinadores, key='nickname', readonly=True)],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dado Treinador').Layout(layout)

        while True:
            button, values = self.open()
            if button == 'Confirmar' and values['nickname']:
                nickname = values['nickname']
                self.close()
                return nickname
            elif button == 'Cancelar' or button is None:
                self.close()
                return None
            else:
                sg.popup("Você deve selecionar um treinador!")


    def log_treinador(self, nickname, dado_treinador):

        nome_treinador = str(nickname) # usando apenas para o título da janela
        dados = dado_treinador
        
        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text(f'Log Treinador - {nome_treinador}', font = ("Helvica"))]]
        layout.append([sg.Text('-' * 40)])
        for dado in dados:
            #layout.append([sg.Text('Treinador: ', size=(15, 1)), sg.Text(dado['treinador'])])
            layout.append([sg.Text('Pokémons no Time: ', size=(20, 1)), sg.Text(dado['pokemons_time'])])
            layout.append([sg.Text('Pokémon Oponente: ', size=(20, 1)), sg.Text(dado['pokemon_oponente'])])
            layout.append([sg.Text('Resultado da Batalha: ', size=(20, 1)), sg.Text(dado['resultado_batalha'])])
            layout.append([sg.Text('Resultado da Captura: ', size=(20, 1)), sg.Text(dado['resultado_captura'])])
            layout.append([sg.Text('-' * 40)])

        layout.append([sg.Button('Voltar')])

        window = sg.Window(f'Log Treinador', layout, modal=True, auto_size_text= True) #largura x altura
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar':
                break
        window.close()

    def pokemon_ja_capturado(self, pokemon):
        sg.change_look_and_feel('DarkAmber')

        layout = [[sg.Text(f'Você já capturou um {pokemon.nome}!\nPode fugir ou continuar para a batalha.')],
                  [sg.Text(f'Lembrando que você não poderá capturá-lo novamente!',font = ('Helvetica',10,'italic'))],
                  [sg.Button('Fugir'), sg.Button('Batalhar')]]

        self.__window = sg.Window('Escolha').Layout(layout)

        button, values = self.open()
        self.close()
        if button == 'Fugir' or sg.WINDOW_CLOSED:
            return True
        return False


    def pokemon_encontrado(self, pokemon, capturado, treinador):
        sg.change_look_and_feel('DarkAmber')
        
        if capturado:
            capturado = 'Sim'
        else:
            capturado = 'Não'

        layout = [[sg.Text(f'O {pokemon.nome} selvagem tem {pokemon.ataque} ATK e {pokemon.hp} HP.')],
                [sg.Text(f'Já capturado? {capturado}')],
                [sg.Text(f'{treinador.nickname}, seu time possui {treinador.ataque_time} de ataque e {treinador.hp_time} de HP.')],
                [sg.Button('OK')]]

        window = sg.Window(f'Pokemon Encontrado', layout, modal=True, auto_size_text= True) #largura x altura
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break
        window.close()

    def time_ataca(self, time_ataques):
        
        ataques = time_ataques

        sg.change_look_and_feel('DarkAmber')
        #layout = [[sg.Text(f'Log Treinador - {nome_treinador}', font = ("Helvica"))]]
        #layout.append([sg.Text('-' * 40)])

        layout = [[sg.Text(f'Seu time ataca primeiro: ')]]
        layout.append([sg.Text('-' * 40)])
        for pokemon in ataques:
            #layout.append([sg.Text('Pokémons no Time: ', size=(20, 1)), sg.Text(dado['pokemons_time'])])
            layout.append([sg.Text(f'{pokemon.nome} ataca com {pokemon.ataque} ATK!')])

        #como faço para colocar o botão a direita? 

        layout.append([sg.Button('>')]) 

        self.__window = sg.Window('Batalha Pokémon', layout)

        while True:
            event, values = self.open()
            if event == sg.WINDOW_CLOSED or event == '>':
                break
        self.close()

    def oponente_ataca(self, pokemon_oponente):

        layout = [[sg.Text(f'O Pokémon oponente ataca: ')]]
        layout.append([sg.Text('-' * 40)])

        layout.append([sg.Text(f'{pokemon_oponente.nome} ataca com {pokemon_oponente.ataque} ATK!')])
        
        layout.append([sg.Button('>')]) 
        self.__window = sg.Window('Batalha Pokémon', layout)

        while True:
            event, values = self.open()
            if event == sg.WINDOW_CLOSED or event == '>':
                break
        self.close()  
       

    def popup_sim_nao(self, mensagem): #* talvez seja interessante adicionar isso na classe abstrata 
        layout = [[sg.Text(mensagem)], 
                [sg.Button('Sim', button_color=('white', 'green')), #apenas teste de cores
                sg.Button('Não', button_color=('white', 'red'))]]

        window = sg.Window('SimNão', layout, size = (300, 80))

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Não':
                window.close()
                return False
            elif event == 'Sim':
                window.close()
                return True
            
    '''def batalha_pokemon(self, time_ataques, pokemon_oponente):
        print('dentro da função batalha')
        print(time_ataques)
        sg.change_look_and_feel('DarkAmber')

        layout = [
            [sg.Text('Batalha Pokémon', font=("Helvica"))],
            [sg.Text('-' * 40)],
            [sg.Multiline(size=(30, 10), key='batalha', disabled=True, autoscroll=False, justification='center',
                        no_scrollbar=True, background_color=None)]
        ]

        self.__window = sg.Window('Batalha Pokémon', layout, finalize=True)

        attack_index = 0
        attack_time = time.time()
        print(len(time_ataques))

        while True:
            event, values = self.__window.read(timeout=100)

            if event == sg.WINDOW_CLOSED:
                break

            if attack_index < len(time_ataques) and time.time() - attack_time >= 2:
                print(attack_index)
                print('dentro do if attack_index')
                self.__window['batalha'].update(f'{time_ataques[attack_index]} atacou!\n', append=True)
                attack_index += 1
                attack_time = time.time()

            if attack_index >= len(time_ataques) and pokemon_oponente.hp <= 0:
                time.sleep(1)  # Adicione um atraso antes de fechar a janela
                break

        self.__window.close()'''

    def log_geral(self):
        pass

    def mostra_popup(self, msg , titulo = None):
        sg.Popup(msg, title = titulo)

    def rodada_popup(self, message, auto_close_duration = 1):
        layout = [[sg.Text(message)]]

        self.__window = sg.Window('Popup', layout, auto_close=True, auto_close_duration=auto_close_duration, element_justification='c')

        event, values = self.open()
        self.close()

    def resultado_batalha_popup(self, msg1, msg2, auto_close_duration = 3):
            layout = [[sg.Text(msg1)],
                      [sg.Text(msg2)]]

            self.__window = sg.Window('Popup', layout, auto_close=True, auto_close_duration=auto_close_duration, element_justification='c')

            event, values = self.open()
            self.close()

    def mostra_mensagem(self, msg):
        print('',msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values