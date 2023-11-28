import random
import time


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

def run_improved_bubble_sort_experiment(tamanho):
    random.seed(42)
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = improved_bubble_sort(arr_copy)
    bubble_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Improved Bubble Sort:")
    print(f"  Tempo de Execução: {bubble_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")


tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    run_improved_bubble_sort_experiment(tamanho)

"""
   Tamanho             Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Improved Bubble Sort                      0.037596                251055                     247779
1    10000  Improved Bubble Sort                      3.972917              25201216                   24772256
2   100000  Improved Bubble Sort                    486.777056            2503656633                 2496290364
"""
#!Tamanho: 1000
#!Improved Bubble Sort:
#!Tempo de Execução: 0.037596 segundos
#!Quantidade de Trocas: 251055
#!Quantidade de Comparações: 247779

#!Tamanho: 10000
#!Improved Bubble Sort:
#!Tempo de Execução: 3.972917 segundos
#!Quantidade de Trocas: 25201216
#!Quantidade de Comparações: 24772256

#!Tamanho: 100000
#!Improved Bubble Sort:
#!Tempo de Execução: 486.777056 segundos
#!Quantidade de Trocas: 2503656633
#!Quantidade de Comparações: 2496290364