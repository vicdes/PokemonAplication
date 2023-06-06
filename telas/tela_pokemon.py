
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
        print("\nDigite o número do pokémon: ")
        num_pokemon = self.le_num_inteiro() #* tratamento de exceção FEITO
        return num_pokemon

    def mostrar_pokemons(self, lista): #recebe a lista nomes e nums vindas do controlador de pokemons
        if len(lista) == 0:
            print("Algo está errado... não existem pokémons registrados no jogo.")
        else:
            print(f"\nOs pokémons disponíveis são: ")
            for i, (nome, num) in enumerate(lista):
                print(f"- {nome} #{num}")
            print(f'\nTotal -> {len(lista)} pokémons.')
    
    def mostra_mensagem(self, msg):
        print(msg)
