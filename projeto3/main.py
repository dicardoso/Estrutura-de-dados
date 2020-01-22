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
####
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
####
def heapify(lista, n, i):
    maior = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        maior = l

    if r < n and lista[maior] < lista[r]:
        maior = r

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap(lista):
    tInicial = time.time()
    n = len(lista)

    for i in range(n, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

    tFinal = time.time()
    tot = tFinal - tInicial
    print('Tempo: {}ms\n'.format(round (tot*1000, 3)))

    return lista

def getNextGap(gap): 
 
    gap = (gap * 10)/13
    if gap < 1: 
        return 1
    return gap 
 
def comb(lista): 
    tInicial = time.time()
    n = len(lista) 
    gap = n 
  
    troca = True

    while gap != 1 or troca == 1: 
   
        gap = int(getNextGap(gap))
  
        troca = False
        
        for i in range(0, n-gap): 
            if lista[i] > lista[i + gap]: 
                lista[i], lista[i + gap]=lista[i + gap], lista[i] 
                troca = True

    tFinal = time.time()
    tot = tFinal - tInicial
    print('Tempo: {}ms\n'.format(round (tot*1000, 3)))
    return lista
####
def shell(lista):
    tInicial = time.time()
    h = 1
    n = len(lista)
    while h > 0:
            for i in range(h, n):
                c = lista[i]
                j = i
                while j >= h and c < lista[j - h]:
                    lista[j] = lista[j - h]
                    j = j - h
                    lista[j] = c
            h = int(h / 2.2)

    tFinal = time.time()
    tot = tFinal - tInicial
    print('Tempo: {}ms\n'.format(round (tot*1000, 3)))
    
    return lista
####

def partition(array, menor, maior):
    i = (menor - 1)
    pivot = array[maior]

    for j in range(menor, maior):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[maior] = array[maior], array[i + 1]
    return (i + 1)

def quick(lista, menor, maior):
    if menor < maior:
        pi = partition(lista, menor, maior)
        quick(lista, menor, pi - 1)
        quick(lista, pi + 1, maior)

    return lista
####
def merge(lista):
    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        merge(listaDaEsquerda)
        merge(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista
####
def gerarLista():
    for i in range(10000):
        num = random.randint(1,5000)
        lista.append(num)

def menu():
    while True:
        os.system('cls') or None
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
            tInicial = time.time()
            
            quick(lista.copy(), 0, len(lista)-1)
            
            tFinal = time.time()
            tot = tFinal - tInicial
            print('Tempo: {}ms\n'.format(round (tot*1000, 3)))

        if op.count('7'):
            print('Executndo MergeSort...')
            tInicial = time.time()

            merge(lista.copy())

            tFinal = time.time()
            tot = tFinal - tInicial
            print('Tempo: {}ms\n'.format(round (tot*1000, 3)))
        
        if op == '0':
            break
        
        input('Pressione ENTER para voltar ao menu')
    print('Programa encerrado')

gerarLista()
menu()