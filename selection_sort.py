import random
import time


def selection_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        if indice_minimo != i:
            trocas += 1
            arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

    return trocas, comparacoes

def run_selection_sort_experiment(tamanho):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = selection_sort(arr_copy)
    selection_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Selection Sort:")
    print(f"  Tempo de Execução: {selection_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_selection_sort_experiment(tamanho)

"""
   Tamanho       Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Selection Sort                      0.020034                   995                     499500
1    10000  Selection Sort                      1.911862                  9990                   49995000
2   100000  Selection Sort                    248.127576                 99991                 4999950000
"""

#!Tamanho: 1000
#!Selection Sort:
#!Tempo de Execução: 0.020034 segundos
#!Quantidade de Trocas: 995
#!Quantidade de Comparações: 499500

#!Tamanho: 10000
#!Selection Sort:
#!Tempo de Execução: 1.911862 segundos
#!Quantidade de Trocas: 9990
#!Quantidade de Comparações: 49995000

#!Tamanho: 100000
#!Selection Sort:
#!Tempo de Execução: 248.127576 segundos
#!Quantidade de Trocas: 99991
#!Quantidade de Comparações: 4999950000