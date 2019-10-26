from No import No

class Lista:
    def __init__(self, head=None):
        self._head = head
    
    def tamanho(self):
        size = 0
        aux = self._head
        while (aux != None):
            size = size + 1
            aux = aux.get_prox()
        
        print(size+1)
        return size

    def inserir_inicio(self, no):
        p = No()
        p.set_filme(no)
        p.set_prox(self._head)
        self._head = p

    def inserir_final(self, no):
        p = No()
        if (self._head == None):
            p.set_filme(no)
            p.set_prox(None)
            self._head = p

        elif (self._head != None):
            p = self._head 
            while (p.get_prox() != None):
                p = p.get_prox()
            q = No(no)
            q.set_prox(None)
            p.set_prox(q)
    
    def inserir_index(self, dado, index):
        p = No()
        q = No()
        p = self._head
        q = self._head
        i = 0

        if (index == 0):
            self.inserir_inicio(dado)
        
        elif (index >= self.tamanho()):
            self.inserir_final(dado)

        else:
            while (i <= index or q == None):
                p = q
                q = p.get_prox()
                i += 1

            novoNo = No(dado)
            p.set_prox(novoNo)
            novoNo.set_prox(q)

    def caminhar(self):
        aux = self._head
        while (aux != None):
            print(aux,'\n')
            aux = aux.get_prox()