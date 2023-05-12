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

    def titulo(self, mensagem):
        linha_separadora = "=" * 80
        print(f"\n{linha_separadora}\n{mensagem.center(len(linha_separadora))}\n{linha_separadora}")