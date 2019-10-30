import json
import os

from No import No
from Filme import Filme
from Lista import Lista
from Pilha import Pilha

def listarJSON (lista):
    #https://www.programiz.com/python-programming/json
    with open("filmes.json", "r", encoding='utf-8') as f:
        filmes = json.load(f)

    
    for f in filmes:
        f = Filme(f['titulo'], f['genero'], f['tempo'], f['atores'], f['ano'])
        lista.inserir_final(f)

def menu(lista):
    while True:
        os.system('cls') or None
        print ('- Filmes favoritos -')
        print ('------- Menu -------\n')
        print ('1 - Inserção\n2 - Remoção\n3 - Exibir lista\n0 - Sair\n')
        op = int(input('> '))
        
        if op == 1:
            menuInserir(lista)

        elif op == 2:
            menuRemover()

        elif op == 3:
            lista.caminhar()
        
        elif op == 0:
            return
        
        else:
            input('Opção inválida! Pressione ENTER')

def menuInserir(lista):
    os.system('cls') or None
    print ('- Filmes favoritos -')
    print ('------ Inserir -----\n')
    print ('1 - Início\n2 - Índice\n3 - Final\n0 - Voltar\n')
    op = (input('> '))
    os.system('cls') or None

    titulo = input('Título:')
    genero = input('Gênero:')
    tempo = (input('Tempo:'))
    atores = input('Atores (separe por ;):')
    ano = (input('Ano:'))
    ano = ano.split(';')
    no = No(Filme(titulo, genero, tempo, atores, ano))
    print(op)
    if op == 1:
        lista.inserir_inicio(no)

    elif op == 2:
        index = (input('Índice:'))
        lista.inserir_index(no, index)

    elif op == 3:
        lista.inserir_final(no)
        
    elif op == 0:
        return
        
    else:
        input('Opção inválida! Pressione ENTER')

def menuRemover():
    os.system('cls') or None



lista = Lista()
listarJSON(lista)

lista.sort()
#lista.caminhar()
menu(lista)