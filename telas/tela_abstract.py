from abc import ABC, abstractmethod
import PySimpleGUI as sg
#from controladores.controladorPokemon import ControladorPokemon

class AbstractTela(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass
    
    #! essa função deixará de existir :(
    def le_num_inteiro(self, mensagem="", ints_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido)
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError
                return valor_int
            except ValueError:
                print("\nValor incorreto! Tente novamente: ")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    
    def cadastrado_com_sucesso(self):
        sg.Popup("Cadastro realizado com sucesso!",title = 'Cadastro')

    def mostra_mensagem(self, msg, titulo = ''):
        sg.popup(msg, title = titulo)


    '''def titulo_sistema(self, mensagem):
        tamanho_linha = 60
        linha = "~" * tamanho_linha
        primeira_palavra = mensagem.split()[0]
        segunda_palavra = mensagem.split()[1]
        centralizado_primeira = primeira_palavra.center(tamanho_linha)
        centralizado_segunda = segunda_palavra.center(tamanho_linha)
        sg.Popup(f"\n{linha}\n\n{centralizado_primeira}\n{centralizado_segunda}\n\n{linha}")'''

    def titulo(self, mensagem):
        linha_separadora = "=" * 80
        sg.Popup(f"\n{linha_separadora}\n{mensagem.center(len(linha_separadora))}\n{linha_separadora}")
    
    '''    def titulor(self, message, auto_close_duration = 1):
        print('função titlo')

        layout = [[sg.Text(message, font = (('Fixedsys'), 24))]]

        self.__window = sg.Window('Batalha', layout, auto_close=True, auto_close_duration=auto_close_duration, element_justification='center', text_justification='center', size=(500, 60))

        event, values = self.open()
        self.close()'''


    def titulo2(self, mensagem):
        tamanho_linha = 80
        linha_superior = "=" * tamanho_linha
        linha_inferior = "-" * tamanho_linha
        sg.Popup(f"\n{linha_superior}\n{mensagem.center(tamanho_linha)}\n{linha_inferior}")

    def titulo3(self, mensagem):
        tamanho_linha = 80
        linha_superior = "-" * tamanho_linha
        linha_inferior = "-" * tamanho_linha
        sg.Popup(f"\n{linha_superior}\n{mensagem.center(tamanho_linha)}\n{linha_inferior}")
