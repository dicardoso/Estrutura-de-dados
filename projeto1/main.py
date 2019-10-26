from No import No
from Filme import Filme
from Lista import Lista

f1 = Filme('Star Wars IX','Aventura','120',['Mark Hammil', 'Carie Fischer'],2019)
f2 = Filme('Vingadores','Aventura','130',['RDJ', 'Chris Evans'],2012)
f3 = Filme('Joker','Ação','123',['Joaquim Fenix', 'Robert de Niro'],2019)
f4 = Filme('Os Incríveis 2','Animação','132',['Fulano', 'Sicrano'],2018)

lista = Lista()
print(lista.tamanho())
lista.inserir_final(f1)
print(lista.tamanho())
lista.inserir_inicio(f2)
print(lista.tamanho())
lista.inserir_final(f3)
print(lista.tamanho())
lista.inserir_index(f4,2)

lista.caminhar()
print('### Nova Lista ###\n')
lista.remover_index(3)
lista.remover_final()
#lista.caminhar()