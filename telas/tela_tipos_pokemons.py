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
                
            sg.popup('Tipo de Pokémon cadastrado com sucesso!')
            return {"nome": nome, "vantagens": vantagens, "fraquezas": fraquezas}


    '''def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        #tipos = dados_tipo_pokemon

        print("Nome: ", dados_tipo_pokemon["nome"])
        print("Fraquezas: ", dados_tipo_pokemon["fraquezas"])
        print("Vantagens: ", dados_tipo_pokemon["vantagens"])
        print("\n")'''

    def mostra_tipo_pokemon(self, dados_tipo_pokemon):
        layout = [[sg.Text('Tipos Registrados', font = ("Helvica bold", 25))]]

        for tipo in dados_tipo_pokemon:
            layout.append([sg.Text('Nome: ', size=(15, 1)), sg.Text(tipo["nome"])])
            layout.append([sg.Text('Fraquezas: ', size=(15, 1)), sg.Text(tipo["fraquezas"])])
            layout.append([sg.Text('Vantagens: ', size=(15, 1)), sg.Text(tipo["vantagens"])])
            layout.append([sg.Text('-' * 40)])

        layout.append([sg.Button('Voltar')])

        window = sg.Window('Tipos', layout, modal=True, auto_size_text= True, size=(300, 500)) #largura x altura
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Voltar':
                break
        window.close()

    def seleciona_tipo_pokemon(self):
        nome = input("Nome do tipo de pokémon que deseja selecionar: ") #não posso colocar capitalize aqui pq quebra.
        return nome

    def mostra_mensagem(self, msg):
        sg.popup(msg)