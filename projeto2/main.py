from AVLTree import AVLTree
from Filme import Filme

import os
import random
idList = [0]

def create_random_id():
    while True:
        random_id = random.randint(1,50)
        
        for i in range(len(idList)):
            if idList.count(random_id) == 0:
                idList.append(random_id)
                return random_id   

def create_avl_tree():
    tree = AVLTree()
    
    id = create_random_id()
    filme = Filme(id, 'Eu', '2019')
    tree.insert(id, filme)
    id = create_random_id()
    filme = Filme(id, 'Tu', '2000')
    tree.insert(id, filme)
    id = create_random_id()
    filme = Filme(id, 'Ele', '1999')
    tree.insert(id, filme)
    return tree

avl = create_avl_tree()
while(True):
    os.system('cls') or None
    print('1 - Inserir filme')
    print('2 - Buscar filme pelo id')
    print('3 - Buscar filmes pelo ano')
    print('4 - Listar filmes em ordem alfabética')
    print('5 - Altura da árvore')
    print('6 - Exibir a árvore')
    print('0 - Sair do programa')

    op = int(input('> '))
    os.system('cls') or None

    if op == 1:
        print('Inserir filme')
        nome = input('Título do filme: ')
        ano = input('Ano de lançamento: ')

        id = create_random_id()
        filme = Filme(id, nome, ano)
        avl.insert(id, filme)
        print('\n')
        print('Filme inserido\nTítulo: {}\nAno: {}\nID: {}'.format(nome, ano, id))

    elif op == 2: 
        id = int(input('Id procurado? ')) 
        avl.find_by_id(id) 

    elif op == 3:
        ano = int(input('Ano procurado? '))
        avl.find_by_year(ano)

    elif op == 4:
        filmes = avl.tree_in_order()

        for filme in filmes:
            avl.find_by_id(filme)

    elif op == 5:
        print('Height:',avl.height)

    elif op == 6:
        avl.print_tree()
        
    elif op == 0:
        print('\n# # # # # # # # # #')
        print('\nPrograma encerrado')
        print('\n# # # # # # # # # #\n')
        break
    
    else:
        print('Entada inválida')
    input('Pressione Enter para voltar')
