import random
import time


def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    comparacoes = 0
    trocas = 0

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            comparacoes += 1
            arr[j + 1] = arr[j]
            j -= 1
            trocas += 1
        arr[j + 1] = key_item

    return comparacoes, trocas

def merge(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_arr = arr[left:left + len_left]
    right_arr = arr[mid + 1:mid + 1 + len_right]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def timsort(arr):
    min_run = 32
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(0, n, min_run):
        comparacoes_insertion, trocas_insertion = insertion_sort(arr, i, min((i + min_run - 1), n - 1))
        comparacoes += comparacoes_insertion
        trocas += trocas_insertion

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

    return comparacoes, trocas

def run_experiment(sort_function, tamanho, sort_name):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    comparacoes, trocas = sort_function(arr_copy)
    sort_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print(f"{sort_name}:")
    print(f"  Tempo de Execução: {sort_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_experiment(timsort, tamanho, "Timsort")


"""
   Tamanho Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000   Timsort                      0.000998                  7449                       7449
1    10000   Timsort                      0.012548                 77156                      77156
2   100000   Timsort                      0.168424                776223                     776223
"""

#!Tamanho: 1000
#!Timsort:
#!Tempo de Execução: 0.000998 segundos
#!Quantidade de Trocas: 7449
#!Quantidade de Comparações: 7449

#!Tamanho: 10000
#!Timsort:
#!Tempo de Execução: 0.012548 segundos
#!Quantidade de Trocas: 77156
#!Quantidade de Comparações: 77156

#!Tamanho: 100000
#!Timsort:
#!Tempo de Execução: 0.168424 segundos
#!Quantidade de Trocas: 776223
#!Quantidade de Comparações: 776223