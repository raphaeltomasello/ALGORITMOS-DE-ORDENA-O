import random
import time


def quick_sort(arr):
    comparacoes = 0
    trocas = 0

    def partition(arr, low, high):
        nonlocal comparacoes, trocas
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas += 1
        return i + 1

    def quick_sort_helper(arr, low, high):
        nonlocal comparacoes, trocas
        if low < high:
            partition_index = partition(arr, low, high)

            quick_sort_helper(arr, low, partition_index - 1)
            quick_sort_helper(arr, partition_index + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    return trocas, comparacoes

def run_quick_sort_experiment(tamanho):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = quick_sort(arr_copy)
    quick_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Quick Sort:")
    print(f"  Tempo de Execução: {quick_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_quick_sort_experiment(tamanho)

"""
   Tamanho   Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Quick Sort                      0.000999                  6284                      10842
1    10000  Quick Sort                      0.012008                 84148                     156757
2   100000  Quick Sort                      0.155503               1050080                    2049857
"""

#!Tamanho: 1000
#!Quick Sort:
#!Tempo de Execução: 0.000999 segundos
#!Quantidade de Trocas: 6284
#!Quantidade de Comparações: 10842

#!Tamanho: 10000
#!Quick Sort:
#!Tempo de Execução: 0.012008 segundos
#!Quantidade de Trocas: 84148
#!Quantidade de Comparações: 156757

#!Tamanho: 100000
#!Quick Sort:
#!Tempo de Execução: 0.155503 segundos
#!Quantidade de Trocas: 1050080
#!Quantidade de Comparações: 2049857