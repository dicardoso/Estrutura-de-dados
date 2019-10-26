from no import No 
from lista import Lista
from pilha import Pilha

no = No(10)
lista = Pilha(no)
no = No(40)
lista.add(no)
lista.add(No(30))
lista.add(No(15))
lista.add(No(2))

lista.caminhar()

lista.remover()
print('----')
lista.caminhar()