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

def run_bubble_sort_experiment(tamanho):
    random.seed(42)  # Garante que os mesmos valores serão gerados a cada execução
    arr = random.sample(range(1, tamanho + 1), tamanho)

    arr_copy = arr.copy()

    start_time = time.time()
    trocas, comparacoes = bubble_sort(arr_copy)
    bubble_time = time.time() - start_time

    print(f"\nTamanho: {tamanho}")
    print("Bubble Sort:")
    print(f"  Tempo de Execução: {bubble_time:.6f} segundos")
    print(f"  Quantidade de Trocas: {trocas}")
    print(f"  Quantidade de Comparações: {comparacoes}")

# Executar experimentos
tamanhos = [1000, 10000,100000]

for tamanho in tamanhos:
    run_bubble_sort_experiment(tamanho)

"""
   Tamanho    Algoritmo  Tempo de Execução (segundos)  Quantidade de Trocas  Quantidade de Comparações
0     1000  Bubble Sort                      0.060995                251055                     499500
1    10000  Bubble Sort                      5.571696              25201216                   49995000
2   100000  Bubble Sort                    543.018806            2503656633                 4999950000

"""
#!Tempo de Execução: 0.060995 segundos
#!Quantidade de Trocas: 251055
#!Quantidade de Comparações: 499500

#!Tamanho: 10000
#!Bubble Sort:
#!Tempo de Execução: 5.571696 segundos
#!Quantidade de Trocas: 25201216
#!Quantidade de Comparações: 49995000

#!Tamanho: 100000
#!Bubble Sort:
#!Tempo de Execução: 543.018806 segundos
#!Quantidade de Trocas: 2503656633
#!Quantidade de Comparações: 4999950000

