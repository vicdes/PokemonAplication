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
            [sg.Text('-------- Tipo Pokémon ----------', font=("Fixedsys", 25))],
            [sg.HorizontalSeparator()],
            [sg.Text('Escolha sua opção', font=("Fixedsys", 16))],
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

    '''def pega_dados_tipo_pokemon(self):
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

        return {"nome": nome, "vantagens": vantagens, "fraquezas": fraquezas,}'''
    def popup_sim_nao(self, mensagem):
        layout = [[sg.Text(mensagem)], 
                [sg.Button('Sim'),
                sg.Button('Não')]]

        window = sg.Window('SimNão', layout, size = (300, 80))

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Não':
                window.close()
                return False
            elif event == 'Sim':
                window.close()
                return True

    def pega_dados_tipo_pokemon(self): #* acho que os returns estão funcionando corretamente.
        sg.ChangeLookAndFeel('DarkAmber')
        while True:
            nome = sg.popup_get_text('Cadastrar Tipo de Pokémon', 'Nome:')
            if nome == None or nome == '':
                return None
            
            fraquezas = []
            while True:
                fraqueza = sg.popup_get_text('Cadastrar Fraqueza', 'Fraqueza:')
                if fraqueza == None or fraqueza == '':
                    return None
                fraquezas.append(fraqueza)

                if not self.popup_sim_nao('Deseja digitar outra fraqueza?'):
                    break

            vantagens = []
            while True:
                vantagem = sg.popup_get_text('Cadastrar Vantagem', 'Vantagem:')
                if vantagem == None or vantagem == '':
                    return None
                vantagens.append(vantagem)

                if not self.popup_sim_nao('Deseja digitar outra vantagem?'):
                    break
                
            sg.popup('Tipo de Pokémon cadastrado com sucesso!', title = 'Cadastro Tipo')
            return {"nome": nome, "vantagens": vantagens, "fraquezas": fraquezas}


    '''def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        #tipos = dados_tipo_pokemon

        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")'''

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        layout = [[sg.Text('Tipos Registrados',size=(60, 1), justification= 'center', font = ("Fixedsys 25"))],[sg.HorizontalSeparator()],
]

        for tipo in dados_tipo_pokemon:
            layout.append([sg.Text('Nome: ', size=(30, 1)), sg.Text(tipo["nome"])])
            layout.append([sg.Text('Fraquezas: ', size=(30, 1)), sg.Text(tipo["fraquezas"])])
            layout.append([sg.Text('Vantagens: ', size=(30, 1)), sg.Text(tipo["vantagens"])])
            layout.append([sg.Text('-' * 60)])

        layout.append([sg.Button('Voltar')])

        window = sg.Window('Tipos', layout, modal=True, auto_size_text= True, size=(500, 500)) #largura x altura
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar':
                break
        window.close()

    def seleciona_tipo_pokemon(self):
        while True:
            sg.ChangeLookAndFeel('DarkAmber')

            layout = [
                [sg.Text('Digite o tipo do Pokémon: ', size=(35,1)), sg.InputText('',key='tipo_pokemon')], 
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Selecionar Pokemon').Layout(layout)

            button, values = self.open()
            nome = values['tipo_pokemon']
 
            self.close()
            
            if button == 'Cancelar' or button == None: #! se clicar em cancelar ou fechar a janela, deveria retornar para a tela anterior (tela_pokemon) e não para o menu principal
                return None
            #if nome is not None and nome is not "":

            return nome
            '''except ValueError:
                self.mostra_mensagem('AAAPor favor, digite algo válido!', 'Value Error')
'''
        
        #nome = input("Nome do tipo de pokémon que deseja selecionar: ") #não posso colocar capitalize aqui pq quebra.
        #return nome

    def mostra_mensagem(self, msg, titulo = ''):
        sg.popup(msg, title = titulo)