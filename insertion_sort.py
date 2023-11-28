import random
import time


def insertion_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        comparacoes += 1

        while j >= 0 and chave < arr[j]:
            comparacoes += 1
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1

        arr[j + 1] = chave

    return trocas, comparacoes

def run_insertion_sort_experiment(tamanho):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = insertion_sort(arr_copy)
    insertion_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Insertion Sort:")
    print(f"  Tempo de Execução: {insertion_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_insertion_sort_experiment(tamanho)

"""
   Tamanho       Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Insertion Sort                      0.018802                251055                     252054
1    10000  Insertion Sort                      1.947069              25201216                   25211215
2   100000  Insertion Sort                    222.720347            2503656633                 2503756632
"""

#!Tamanho: 1000
#!Insertion Sort:
#!Tempo de Execução: 0.018802 segundos
#!Quantidade de Trocas: 251055
#!Quantidade de Comparações: 252054

#!Tamanho: 10000
#!Insertion Sort:
#!Tempo de Execução: 1.947069 segundos
#!Quantidade de Trocas: 25201216
#!Quantidade de Comparações: 25211215

#!Tamanho: 100000
#!Insertion Sort:
#!Tempo de Execução: 222.720347 segundos
#!Quantidade de Trocas: 2503656633
#!Quantidade de Comparações: 2503756632