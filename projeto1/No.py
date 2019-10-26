
class No:
    def __init__(self, dado=None, prox=None):
        self._dado = dado
        self._prox = prox 
    
    def get_dado (self):
        return self._dado

    def set_dado (self, novodado):
        self._dado = novodado

    def get_prox (self):
        return self._prox

    def set_prox (self , outro) :
        self._prox = outro

    def __str__(self):
        return "{}".format(self._dado)