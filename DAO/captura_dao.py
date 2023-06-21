from DAO.dao import DAO
from entidades.captura_pokemon import CapturaPokemon


class CapturaDAO(DAO):
    def __init__(self):
        super().__init__('capturas.pkl')

    def add(self, captura: CapturaPokemon):
        if((captura is not None) and isinstance(captura, CapturaPokemon)):
            super().add(captura)

    '''def update(self, captura: CapturaPokemon):
        if((captura is not None) and isinstance(captura, CapturaPokemon) and isinstance(captura.id, int)):
            super().update(captura.id, captura)'''

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    '''def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)'''
        