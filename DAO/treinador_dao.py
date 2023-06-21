from DAOs.dao import DAO
from entidade.treinador import Treinador

#cada entidade terá uma classe dessa, implementação bem simples.
class TreinadorDAO(DAO):
    def __init__(self):
        super().__init__('treinadores.pkl')

    def add(self, treinador: Treinador):
        if((treinador is not None) and isinstance(treinador, Treinador) and isinstance(treinador.nickname, str)):
            super().add(treinador.nickname, treinador)

    def update(self, treinador: Treinador):
        if((treinador is not None) and isinstance(treinador, Treinador) and isinstance(treinador.nickname, str)):
            super().update(treinador.nickname, treinador)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
