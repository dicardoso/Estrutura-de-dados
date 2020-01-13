import random
import time
import os

lista = []

def bubble(lista):
    tInicial = time.time()

    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False
    
    tFinal = time.time()
    tot = tFinal - tInicial
    print('Tempo: {}ms\n'.format(round (tot*1000, 3)))
    
    return lista 

def insertion(lista): 
    tInicial = time.time()

    for i in range(1, len(lista)): 
        key = lista[i] 
        j = i-1
        while j >=0 and key < lista[j] : 
                lista[j+1] = lista[j] 
                j -= 1
        lista[j+1] = key 
    
    tFinal = time.time()
    tot = tFinal - tInicial
    print('Tempo: {}ms\n'.format(round (tot*1000, 3)))

    return lista

def heap(lista):
    pass

def comb(lista):
    pass

def shell(lista):
    pass

def quick(lista):
    pass

def merge(lista):
    pass     

def gerarLista():
    for i in range(2000):
        num = random.randint(1,5000)
        lista.append(num)

def menu():
    while True:
        print('### Algoritmos de ordenação ###')
        print('1 - BubbleSort\n2 - InsertionSort\n3 - HeapSort\n4 - CombSort')
        print('5 - ShellSort\n6 - QuickSort\n7 - MergeSort\n0 - Sair')
        op = input('> ')
        os.system('cls') or None

        if op.count('1'):
            print('Executando BubbleSort...')
            bubble(lista.copy())

        if op.count('2'):
            print('Executndo InsertionSort...')
            insertion(lista.copy())

        if op.count('3'):
            print('Executndo HeapSort...')
            heap(lista.copy())

        if op.count('4'):
            print('Executndo CombSort...')
            comb(lista.copy())

        if op.count('5'):
            print('Executndo ShellSort...')
            shell(lista.copy())

        if op.count('6'):
            print('Executndo QuickSort...')
            quick(lista.copy())

        if op.count('7'):
            print('Executndo MergeSort...')
            merge(lista.copy())
        
        if op == '0':
            break
        
        input('Pressione ENTER para voltar ao menu')
    print('Programa encerrado')

gerarLista()
menu()