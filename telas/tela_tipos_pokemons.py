from telas.tela_abstract import AbstractTela
import PySimpleGUI as sg

#imagino que não há necessidade de tratar as exceções que recebem strings. 

class TelaTiposPokemons(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # def tela_opcoes(self):
    #     self.titulo("Tipos de Pokémon")
    #     print("\nEscolha uma opção")
    #     print("  1 - Incluir tipo de pokémon")
    #     print("  2 - Excluir tipo de pokémon")
    #     print("  3 - Listar tipos de pokémon")
    #     print("\n  0 - Retornar")
    #     opcao = self.le_num_inteiro("\nEscolha uma opção: ", [0, 1, 2, 3])  #* tratamento de exceção FEITO
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
            [sg.Text('-------- Tipo Pokémon ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir tipo de pokémon', "RD1", key='1')],
            [sg.Radio('Excluir tipo de pokémon', "RD1", key='2')],
            [sg.Radio('Listar tipos de pokémon', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastrar Tipo').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def pega_dados_tipo_pokemon(self):
        self.titulo2("Cadastrar Tipo de Pokémon")
        nome = input("\nNome: ").capitalize()
        fraquezas = []
        while True:
            fraqueza = input("\nFraqueza: ").capitalize()
            fraquezas.append(fraqueza) 
            continuar = self.le_num_inteiro("\nDeseja digitar outra? \n1- Sim \n2- Não\n", [1, 2]) #* tratamento de exceção FEITO
            if continuar == 2:
                break

        vantagens = []
        while True:
            vantagem = input("\nVantagem: ").capitalize()
            vantagens.append(vantagem)
            continuar = self.le_num_inteiro("\nDeseja digitar outra? \n1- Sim \n2- Não\n", [1, 2]) #* tratamento de exceção FEITO
            if continuar == 2:
                break

        return {"nome": nome, "vantagens": vantagens, "fraquezas": fraquezas,}

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")


    def seleciona_tipo_pokemon(self):
        nome = input("Nome do tipo de pokémon que deseja selecionar: ") #não posso colocar capitalize aqui pq quebra.
        return nome

    def mostra_mensagem(self, msg):
        print(msg)