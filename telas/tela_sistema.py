import PySimpleGUI as sg
from telas.tela_abstract import AbstractTela

class TelaSistema(AbstractTela):

    def __init__(self):
        self.__window = None
        self.init_components()

    '''    def tela_opcoes(self):
        self.titulo_sistema("Pokemon\nApplication")
        print("\nEscolha uma opção")
        print("  1 - Treinadores")
        print("  2 - Tipos de Pokemons")
        print("  3 - Pokémons")
        print("  4 - Captura")
        print("\n  0 - Finalizar sistema")

        opcao = self.le_num_inteiro("\nEscolha uma opção: ",[0,1,2,3,4]) #* tratamento de exceção FEITO
        return opcao'''

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Boas-vindas, Treinador Pokémon!', font=("GOST Common", 25))],
            [sg.Text('Escolha sua opção', font=("Roboto", 15))],
            [sg.Radio('Treinadores', "RD1", key='1')],
            [sg.Radio('Tipos', "RD1", key='2')],
            [sg.Radio('Pokemon', "RD1", key='3')],
            [sg.Radio('Captura', "RD1", key='4')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Escolher'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pokémon Application').Layout(layout)