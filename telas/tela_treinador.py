import PySimpleGUI as sg
from telas.tela_abstract import AbstractTela

class TelaTreinador(AbstractTela): 
    # def tela_opcoes(self):
    #     self.titulo("Tela Treinadores")
    #     print("\nEscolha uma opção")
    #     print("  1 - Incluir novo Treinador")
    #     print("  2 - Excluir Treinador")
    #     print("  3 - Listar Treinadores + Porcentagem Pokedex")
    #     print("\n  4 - Cadastrar time")
    #     print("  5 - Deletar time")
    #     print("  6 - Alterar time")
    #     print("\n  7 - Listar pokemons de um treinador")
    #     print("  8 - Mostrar time de um treinador")
    #     print("\n  0 - Retornar")
    #
    #     opcao = self.le_num_inteiro("\nEscolha uma opção: ", [0, 1, 2, 3, 4, 5,6, 7, 8]) #* tratamento de exceção FEITO
    #     return opcao
    def __init__(self):
        self.__window = None
        self.init_components()

    def open(self):
        button, values = self.__window.Read()
        return button, values

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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def tela_opcoes_alterar_time(self):
        self.seleciona_funcao_alterar_time()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
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
            #[sg.Combo(['Ash', 'José'], size=(15, 30), font='Arial 12', key='Empresas')],
            [sg.Text('Treinadores', font=("GOST Common", 25))],
            [sg.Text('Escolha sua opção', font=("Roboto", 15))],
            [sg.Radio('Incluir novo treinador', "RD1", key='1')],
            [sg.Radio('Excluir Treinador', "RD1", key='2')],
            [sg.Radio('Listar Treinadores + Porcentagem Pokedex', "RD1", key='3')],
            [sg.Radio('Cadastrar time', "RD1", key='4')],
            [sg.Radio('Deletar time', "RD1", key='5')],
            [sg.Radio('Alterar time', "RD1", key='6')],
            [sg.Radio('Listar pokemons de um treinador', "RD1", key='7')],
            [sg.Radio('Mostrar time de um treinador', "RD1", key='8')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Escolher'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pokémon Application').Layout(layout)

    def seleciona_funcao_alterar_time(self):
        # print("\nEscolha uma opção")
        # print("  1 - Incluir pokemon")
        # print("  2 - Excluir pokemon")
        # print("  3 - Trocar pokemon")
        # opcao = self.le_num_inteiro("\nEscolha uma opção: ", [1, 2, 3])  # * tratamento de exceção FEITO
        # return opcao

        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Treinadores', font=("GOST Common", 25))],
            [sg.Text('Escolha sua opção', font=("Roboto", 15))],
            [sg.Radio('Incluir pokémon', "RD1", key='1')],
            [sg.Radio('Excluir pokémon', "RD1", key='2')],
            [sg.Radio('Trocar pokémon', "RD1", key='3')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Escolher'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pokémon Application').Layout(layout)


    def cadastrar_outro_pokemon(self):
        # print("\nDeseja continuar? \n1- sim \n2- não ")
        # continuar = self.le_num_inteiro() == 1 # * tratamento de exceção FEITO
        # return continuar
        button = 0
        layout = [
            [sg.Text('Deseja continuar? ', size=(15,1))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Treinador').Layout(layout)

        button, values = self.open()
        print(button)
        if button is not None and button == 'Confirmar':
            continuar = True
        else:
            continuar = False
        self.close()
        return continuar

    def cria_nickname_treinador(self):
        sg.ChangeLookAndFeel('DarkAmber')
        #self.titulo2("Cadastrar Treinador")
        #nickname = input("Nickname: ")
        #return {"nickname": nickname, "porcentagem_pokedex": 0.0}'''
        layout = [
            [sg.Text('Nickname: ', size=(15,1)), sg.InputText('',key='nickname')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Treinador').Layout(layout)

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
                sg.popup("Você deve digitar algo!")
    
    def seleciona_treinador(self, treinadores):
        #print('tela com comboxo')
        sg.ChangeLookAndFeel('DarkAmber')
        lista_treinadores = treinadores
        layout = [
            [sg.Text('Nickname: ', size=(15,1)), sg.Combo(lista_treinadores, key='nickname', readonly=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleção de Treinador').Layout(layout)

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

        
    def mostra_treinador(self, dados_treinador):
        """print("Nickname: ", dados_treinador["nickname"])
        print("Porcentagem da pokedéx completa: {:.1f}%".format(dados_treinador["porcentagem_pokedex"]))"""
        string_todos_treinadores = ""
        if len(dados_treinador) == 0:
            string_todos_treinadores = "Não há treinadores cadastrados!"
        else:
            for treinador in dados_treinador:
                string_todos_treinadores = string_todos_treinadores + "\nNickname: " + treinador["nickname"] + '\n'
                string_todos_treinadores = string_todos_treinadores + f"Porcentagem da pokedéx: {treinador['porcentagem_pokedex']:.2f}%\n" #botei para duas casas decimais
        sg.Popup('-------- LISTA DE TREINADORES ----------', string_todos_treinadores)


    '''    def seleciona_treinador(self):
        """nickname = input("Nickname do treinador que deseja selecionar: ")
        return nickname"""
        layout = [
            [sg.Text('Nickname: ', size=(15,1)), sg.InputText('',key='nickname')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Treinador').Layout(layout)

        button, values = self.open()
        nickname = values['nickname']

        self.close()
        return nickname'''

    def seleciona_pokemon_capturado(self):
        # print("\nCódigo do pokémon que deseja selecionar: ")
        # codigo = self.le_num_inteiro() #* tratamento de exceção FEITO
        # return codigo
            sg.ChangeLookAndFeel('DarkAmber')

            layout = [
                [sg.Text('Número do Pokémon que deseja incluir: ', size=(40,1)), sg.InputText('',key='num_pokemon')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Selecionar Pokemon').Layout(layout)

            button, values = self.open()
            num_pokemon = values['num_pokemon']

            self.close()

            if button == 'Cancelar' or button == None: #! se clicar em cancelar ou fechar a janela, deveria retornar para a tela anterior (tela_pokemon) e não para o menu principal
                return None
            #if num_pokemon is not None and num_pokemon != '':
            try:
                return int(num_pokemon)
            except ValueError:
                self.mostra_mensagem('Por favor, digite um número válido!', 'Value Error')

    def seleciona_pokemon_do_time(self):
        # print("\nCódigo do pokémon que deseja substituir: ")
        # codigo = self.le_num_inteiro() #* tratamento de exceção FEITO
        # return codigo
        #while True:
        while True:
            sg.ChangeLookAndFeel('DarkAmber')

            layout = [
                [sg.Text('Número do Pokémon que deseja remover: ', size=(40,1)), sg.InputText('',key='num_pokemon')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Selecionar Pokemon').Layout(layout)

            button, values = self.open()
            num_pokemon = values['num_pokemon']

            self.close()

            if button == 'Cancelar' or button == None: #! se clicar em cancelar ou fechar a janela, deveria retornar para a tela anterior (tela_pokemon) e não para o menu principal
                return None
            #if num_pokemon is not None and num_pokemon != '':
            try:
                return int(num_pokemon)
            except ValueError:
                self.mostra_mensagem('Por favor, digite um número válido!', 'Value Error')

    def mostra_mensagem(self, msg):
        #print(msg)
        sg.Popup('', msg)



