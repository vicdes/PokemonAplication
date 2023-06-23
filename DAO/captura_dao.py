from DAO.dao import DAO
from entidades.captura_pokemon import CapturaPokemon
import pickle

class CapturaDAO(DAO):
    def __init__(self):
        super().__init__('capturas.pkl')

    def add(self, id, captura: CapturaPokemon):
        if captura is not None and isinstance(captura, CapturaPokemon):
            print('ADD captura DAO')
            super().add(id, captura)

    def get_capturas_by_treinador(self, nickname):
        capturas = []
        for captura in self.get_all():
            if captura.treinador == nickname:
                capturas.append(captura)
        return capturas
    
    '''def update(self, captura: CapturaPokemon):
        if((captura is not None) and isinstance(captura, CapturaPokemon) and isinstance(captura.id, int)):
            super().update(captura.id, captura)'''

    def get(self, key:int):
        if isinstance(key, int):
            print('GET captura DAO')
            return super().get(key)

    '''def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)'''
        