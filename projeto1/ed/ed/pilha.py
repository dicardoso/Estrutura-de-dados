class Pilha:
    def __init__(self,topo):
        self._topo = topo
    
    def add(self, no):
        no.set_prox(self._topo)
        self._topo = no
        
    def remover (self):
        self._topo = self._topo.get_prox()       
    
    def caminhar(self):
        aux = self._topo
        prox = self._topo.get_prox()
        while (aux != None):
            print(aux)
            aux = aux.get_prox()