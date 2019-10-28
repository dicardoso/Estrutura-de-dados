import json
import os

from No import No
from Filme import Filme
from Lista import Lista

def listarJSON (lista):
    #https://www.programiz.com/python-programming/json
    with open("filmes.json", "r", encoding='utf-8') as f:
        filmes = json.load(f)

    
    for f in filmes:
        f = Filme(f['titulo'], f['genero'], f['tempo'], f['atores'], f['ano'])
        lista.inserir_final(f)

def menu():
    while True:
        os.system('cls') or None
        print ('- Filmes favoritos -')
        print ('------- Menu -------\n')
        print ('1 - Inserção\n2 - Remoção\n3 - Exibir lista\n0 - Sair\n')
        op = int(input('> '))

        if op == 1:
            menuInserir()

        elif op == 2:
            menuRemover()

        elif op == 3:
            lista.caminhar()
        
        elif op == 0:
            return
        
        else:
            input('Opção inválida! Pressione ENTER')

def menuInserir():
    os.system('cls') or None
    print ('- Filmes favoritos -')
    print ('------ Inserir -----\n')
    

def menuRemover():
    os.system('cls') or None
    

lista = Lista()
listarJSON(lista)
menu()



#lista.inserir_final(f1)
#lista.inserir_inicio(f2)
#lista.inserir_final(f3)
#lista.inserir_index(f4,2)

#lista.caminhar()
#print('### Nova Lista ###\n')
#lista.remover_index(3)
#lista.remover_final()
#lista.caminhar()