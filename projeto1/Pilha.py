from No import No

class Pilha:
    def __init__(self,topo=None):
        self._topo = topo

    def get_topo(self):
        return self

    def push(self,dado):
        p = No(dado)
        p.set_prox(self._topo)
        self._topo = p
        
    def pop(self):
        p = self._topo
        self._topo = self._topo.get_prox()
        return p

    def is_empty(self):
        if self._topo == None:
            return True
        else:
            return False

    def size(self):
        cont=0
        p=self._topo
        while p != None:
            cont+=1
            p = p.get_prox()
        return cont