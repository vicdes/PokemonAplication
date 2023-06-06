
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

    def pega_dados_captura(self): #* tratamento de exceção FEITO
        self.titulo2("Dados Captura") 
        nickname = input("\nNickname do treinador: ")

        return nickname

    def seleciona_pokemon_inicial(self): #* tratamento de exceção FEITO
        codigo_inicial = self.le_num_inteiro("\nDigite o código do pokémon que deseja selecionar:\n#1 Bulbasaur\n#4 Charmander\n#7 Squirtle\n", [1,4,7]) 
        return codigo_inicial
    
    def log_treinador(self):
        nickname = input("\nDigite o nickname do treinador: ")
        return nickname

    def mostra_mensagem(self, msg):
        print(msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values