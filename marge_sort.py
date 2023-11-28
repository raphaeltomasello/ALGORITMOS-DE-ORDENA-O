import random
import time


def merge_sort(arr):
    comparacoes = 0
    trocas = 0

    def merge(left, right):
        nonlocal comparacoes, trocas
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                trocas += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    if len(arr) <= 1:
        return trocas, comparacoes

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    trocas_left, comparacoes_left = merge_sort(left)
    trocas_right, comparacoes_right = merge_sort(right)

    trocas += trocas_left + trocas_right
    comparacoes += comparacoes_left + comparacoes_right

    arr[:] = merge(left, right)

    return trocas, comparacoes

def run_merge_sort_experiment(tamanho):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = merge_sort(arr_copy)
    merge_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Merge Sort:")
    print(f"  Tempo de Execução: {merge_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_merge_sort_experiment(tamanho)

"""
   Tamanho   Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Merge Sort                      0.001070                  4398                       8702
1    10000  Merge Sort                      0.019999                 61304                     120560
2   100000  Merge Sort                      0.247174                776697                    1536098
"""

#!Tamanho: 1000
#!Merge Sort:
#!Tempo de Execução: 0.001070 segundos
#!Quantidade de Trocas: 4398
#!Quantidade de Comparações: 8702

#!Tamanho: 10000
#!Merge Sort:
#!Tempo de Execução: 0.019999 segundos
#!Quantidade de Trocas: 61304
#!Quantidade de Comparações: 120560

#!Tamanho: 100000
#!Merge Sort:
#!Tempo de Execução: 0.247174 segundos
#!Quantidade de Trocas: 776697
#!Quantidade de Comparações: 1536098