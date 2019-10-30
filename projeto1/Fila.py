from No import No
from Filme import Filme

class Fila:
    def __init__(self,head=None):
        self._head = head
    
    def get_head(self):
        return self._head
    
    def add(self,no):
        q = No(no)
        p = self._head
        if p == None:
            self._head=q
        else:
            while p.get_prox() != None:
                p=p.get_prox()
            p.set_prox(No(q))

    def remove(self):
        p=self._head
        self._head = self._head.get_prox()
        return p

    def size(self):
        cont=0
        p=self._head
        while p != None:
            cont+=1
            p = p.get_prox()
        return cont

    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False