class Filme:
    def __init__(self, titulo='', genero='',tempo='', atores=[], ano=''):
        self._titulo = titulo
        self._genero = genero
        self._tempo = tempo
        self._atores = atores
        self._ano = ano

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_genero(self, genero):
        self._genero = genero
    
    def set_tempo(self, tempo):
        self._tempo = tempo
    
    def set_ator(self, ator):
        self._atores.append(ator)

    def set_ano(self, ano):
        self._ano = ano

    def get_titulo(self):
        return self._titulo

    def get_genero(self):
        return self._genero 
    
    def get_tempo(self):
        return self._tempo
    
    def get_ator(self):
        return self._atores

    def get_ano(self):
        return self._ano