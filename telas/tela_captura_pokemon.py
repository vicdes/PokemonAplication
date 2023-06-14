
from telas.tela_abstract import AbstractTela
import PySimpleGUI as sg

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

    def digite_para_continuar(self):
        input('\nAperte qualquer coisa para continuar...') #apenas pra dar uma pausa antes de retornar a tela

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

        layout = [[sg.Text(f'Você já capturou um {pokemon.nome}!\nVocê pode fugir ou continuar para a batalha.')],
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

    def batalha_pokemon(self, window1):
        sg.change_look_and_feel('DarkAmber')
    
        layout = [[sg.Text('Batalha Pokémon', font = ("Helvica"))]]
        layout.append([sg.Text('-' * 40)])
        layout.append([sg.Text('pokemon_sorteado: ', size=(20, 1)), sg.Text(window1['pokemon_sorteado'])])

    def log_geral(self):
        pass

    def mostra_mensagem1(self, msg , titulo = None):
        sg.Popup(msg, title = titulo)

    def rodadas(self, rodada):
        sg.Popup(rodada, custom_text='Continuar')

    def mostra_mensagem(self, msg):
        print('',msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values