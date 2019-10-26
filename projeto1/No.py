
class No:
    def __init__(self, filme=None, prox=None):
        self._filme = filme
        self._prox = prox 
    
    def get_filme (self):
        return self._filme

    def set_filme (self, novoFilme):
        self._filme = novoFilme

    def get_prox (self):
        return self._prox

    def set_prox (self , outro) :
        self._prox = outro

    def __str__(self):
        texto ='Título: {}\nGênero: {}\nDuração: {} min\nAno: {}\nAtores: {}'.format(
            self._filme._titulo,
            self._filme._genero, 
            self._filme._tempo, 
            self._filme._ano,
            self._filme._atores)
        return texto