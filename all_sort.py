import random
import time


def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                trocas += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return trocas, comparacoes

def improved_bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                trocas += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return trocas, comparacoes - trocas

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

def timsort(arr):
    min_run = 32
    n = len(arr)
    comparacoes = 0
    trocas = 0

    def merge(left, mid, right):
        nonlocal comparacoes, trocas
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
                trocas += 1
            k += 1

        while i < len_left:
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len_right:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    for i in range(0, n, min_run):
        end = min((i + min_run - 1), n - 1)
        comparacoes_insertion, trocas_insertion = insertion_sort(arr[i:end + 1])
        comparacoes += comparacoes_insertion
        trocas += trocas_insertion

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(left, mid, right)

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
    run_experiment(bubble_sort, tamanho, "Bubble Sort")
    run_experiment(improved_bubble_sort, tamanho, "Improved Bubble Sort")
    run_experiment(insertion_sort, tamanho, "Insertion Sort")
    run_experiment(selection_sort, tamanho, "Selection Sort")
    run_experiment(merge_sort, tamanho, "Merge Sort")
    run_experiment(quick_sort, tamanho, "Quick Sort")
    run_experiment(timsort, tamanho, "Timsort")