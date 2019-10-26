class Lista:
    def __init__(self,head):
        self._head = head
    
    def add(self, no):
        p = self._head
        while (p.get_prox()!=None):
            p = p.get_prox()
        p.set_prox(no)
    
    def caminhar(self):
        aux = self._head
        while (aux != None):
            print(aux)
            aux = aux.get_prox()