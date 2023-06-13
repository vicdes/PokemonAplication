
import PySimpleGUI as sg
from telas.tela_abstract import AbstractTela

class TelaPokemon(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()


    # def tela_opcoes(self):
    #     self.titulo("Tela Pokémon")
    #     print("\nEscolha uma opção")
    #     print("  1 - Deletar Pokémon")
    #     print("  2 - Mostrar Pokémons existentes")
    #     print("  3 - Alterar HP ou Ataque de Pokémon")
    #     print("\n  0 - Retornar")
    #     print('  [OBS.] Essas alterações causam impacto em todo o jogo. Faça com moderação.')
    #
    #     opcao = self.le_num_inteiro("\nEscolha uma opção: ", [1, 2, 3, 0]) #* tratamento de exceção FEITO
    #     return opcao

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
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
            [sg.Text('-------- Pokémon ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Deletar Pokémon', "RD1", key='1')],
            [sg.Radio('Mostrar Pokémons existentes', "RD1", key='2')],
            [sg.Radio('Alterar HP ou Ataque de Pokémon', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Pokémon').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    # * talvez isso possa se tornar um método abstrato pra ser usado no time?
    def seleciona_pokemon_numero(self):
        '''print("\nDigite o número do pokémon: ")
        num_pokemon = self.le_num_inteiro() #* tratamento de exceção FEITO
        return num_pokemon'''
        while True:
            sg.ChangeLookAndFeel('DarkAmber')

            layout = [
                [sg.Text('Digite o número do Pokémon: ', size=(25,1)), sg.InputText('',key='num_pokemon')], 
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Selecionar Pokemon').Layout(layout)

            button, values = self.open()
            num_pokemon = values['num_pokemon']
 
            self.close()

            if button == 'Cancelar' or button == None: #! se clicar em cancelar ou fechar a janela, deveria retornar para a tela anterior (tela_pokemon) e não para o menu principal
                return None   
            if num_pokemon is not None and num_pokemon != '':
                return int(num_pokemon) #! é preciso colocar int para converter a string em int
    
    def mostra_status_pokemon(self, pokemon, nome_janela): #! é preciso fazer o usuário retornar pra tela anterior caso selecione cancelar na janela de status
        sg.ChangeLookAndFeel('DarkAmber')
        
        layout = [[sg.Text('Pokémon selecionado com seus atributos alterados:', size=(40, 1), font=("Helvetica", 14))],
                [sg.Text(pokemon.nome, size=(15, 1)), sg.Text(pokemon.nome, size=(25, 1))],
                [sg.Text('Número:', size=(15, 1)), sg.Text(pokemon.num, size=(25, 1))],
                [sg.Text('HP:', size=(15, 1)), sg.Text(pokemon.hp, size=(25, 1))],
                [sg.Text('Ataque:', size=(15, 1)), sg.Text(pokemon.ataque, size=(25, 1))],
                [sg.Button('OK')]]

        window = sg.Window(nome_janela, layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()
        
    def alterar_hp_ou_ataque(self, dados_pokemon_selecionado): #* TRATAR EXCEÇÃO SOMENTE INTS PARA HP E ATAQUE
        while True:
            sg.ChangeLookAndFeel('DarkAmber')
            nome_selecionado = dados_pokemon_selecionado[0]
            hp_atual = dados_pokemon_selecionado[1]
            ataque_atual = dados_pokemon_selecionado[2]

            status_atuais = f'{nome_selecionado} - HP: {hp_atual} - Ataque: {ataque_atual}'

            layout = [
                #[sg.Text('Digite o número do Pokémon: ', size=(25,1)), sg.InputText('',key='num_pokemon')],
                [sg.Text('Pokémon selecionado: ', size=(25,1)), sg.Text(status_atuais)],
                [sg.Text('Digite o novo HP: ', size=(25,1)), sg.InputText('',key='hp')],
                [sg.Text('Digite o novo Ataque: ', size=(25,1)), sg.InputText('',key='ataque')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Alterar HP ou Ataque').Layout(layout)

            button, values = self.open()
            hp = values['hp']
            ataque = values['ataque']
 
            self.close()

            if button == 'Cancelar' or button == None:
                return None
            
            if hp is not None and hp != '' and ataque is not None and ataque != '':
                return int(hp), int(ataque)
        
    '''def pega_dados_amigo(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS AMIGO ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        telefone = values['telefone']
        cpf = values['cpf']

        self.close()
        return {"nome": nome, "telefone": telefone, "cpf": cpf}'''


    def mostrar_pokemons(self, lista): # recebe a lista nomes e nums vindas do controlador de pokemons
        if len(lista) == 0:
            sg.popup("Algo está errado... não existem pokémons registrados no jogo.")
        else:
            # criar duas colunas de textos
            dados = [[nome, num] for nome, num in lista]

            # criar layout com tabela
            layout = [
                [sg.Text('Pokémons disponíveis no jogo')],
                [sg.Table(values=dados, headings=['Nome', 'Número'], display_row_numbers=False,
                        auto_size_columns=True, num_rows=min(25, len(dados)))],
                [sg.Button('Voltar')]
            ]

            # criar e mostrar janela
            janela = sg.Window('Pokémons', layout, modal=True, element_justification='c', size=(300, 500)) #largura x altura
            while True:
                event, values = janela.read()
                if event == sg.WINDOW_CLOSED or event == 'Voltar':
                    break
            janela.close()




            '''print(f"\nOs pokémons disponíveis são: ")
            for i, (nome, num) in enumerate(lista):
                print(f"- {nome} #{num}")
            print(f'\nTotal -> {len(lista)} pokémons.')'''
    
    '''def mostra_amigo(self, dados_amigo):
    string_todos_amigos = ""
    for dado in dados_amigo:
      string_todos_amigos = string_todos_amigos + "NOME DO AMIGão: " + dado["nome"] + '\n'
      string_todos_amigos = string_todos_amigos + "FONE DO AMIGO: " + str(dado["telefone"]) + '\n'
      string_todos_amigos = string_todos_amigos + "CPF DO AMIGO: " + str(dado["cpf"]) + '\n\n'

    sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_amigos)'''

    def mostra_mensagem(self, msg):
        sg.popup(msg)
