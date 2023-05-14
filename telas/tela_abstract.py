from abc import ABC, abstractmethod
#from controladores.controladorPokemon import ControladorPokemon

class AbstractTela(ABC):
    @abstractmethod
    def tela_opcoes(self):
        pass

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


    def le_num_float(self, mensagem="", floats_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_float = float(valor_lido)
                if floats_validos and valor_float not in floats_validos:
                    raise ValueError
                return valor_float
            except ValueError:
                print("\nValor incorreto! Tente novamente: ")
                if floats_validos:
                    print("Valores válidos: ", floats_validos)

    def le_string(self, mensagem="", str_validos=None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_str = str(valor_lido)
                if str_validos and valor_str not in str_validos:
                    raise ValueError
                return valor_str
            except ValueError:
                print("\nValor incorreto! Tente novamente: ")
                if str_validos:
                    print("Valores válidos: ", str_validos)

    def cadastrado_com_sucesso(self):
        print("Cadastro realizado com sucesso!")

    def titulo_sistema(self, mensagem):
        tamanho_linha = 60
        linha = "~" * tamanho_linha
        primeira_palavra = mensagem.split()[0]
        segunda_palavra = mensagem.split()[1]
        centralizado_primeira = primeira_palavra.center(tamanho_linha)
        centralizado_segunda = segunda_palavra.center(tamanho_linha)
        print(f"\n{linha}\n\n{centralizado_primeira}\n{centralizado_segunda}\n\n{linha}")

    def titulo(self, mensagem):
        linha_separadora = "=" * 80
        print(f"\n{linha_separadora}\n{mensagem.center(len(linha_separadora))}\n{linha_separadora}")

    def titulo2(self, mensagem):
        tamanho_linha = 80
        linha_superior = "=" * tamanho_linha
        linha_inferior = "-" * tamanho_linha
        print(f"\n{linha_superior}\n{mensagem.center(tamanho_linha)}\n{linha_inferior}")

    def titulo3(self, mensagem):
        tamanho_linha = 80
        linha_superior = "-" * tamanho_linha
        linha_inferior = "-" * tamanho_linha
        print(f"\n{linha_superior}\n{mensagem.center(tamanho_linha)}\n{linha_inferior}")
