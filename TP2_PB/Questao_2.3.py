import random
import time

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1

def quickselect(array, low, high, k):
    if low == high:
        return array[low]
    
    pivot_index = partition(array, low, high)

    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    else:
        return quickselect(array, pivot_index + 1, high, k)

def testar_quickselect():
    tempos_execucao_k = {1: [], 10: [], 100: [], 500: [], 1000: []}

    for _ in range(10):
        lista = [random.randint(1, 1000) for _ in range(10000)]
        
        for k in [1, 10, 100, 500, 1000]:
            tempos_execucao_individual = []
            for _ in range(5):
                start_time = time.time()
                resultado = quickselect(lista.copy(), 0, len(lista) - 1, k - 1)
                end_time = time.time()
                tempos_execucao_individual.append(end_time - start_time)
            
            tempo_medio = sum(tempos_execucao_individual) / len(tempos_execucao_individual)
            tempos_execucao_k[k].append(tempo_medio)
    
    for k, tempos in tempos_execucao_k.items():
        media_tempo = sum(tempos) / len(tempos)
        print(f"Tempo médio de execução para o {k}-ésimo menor elemento: {media_tempo:.6f} segundos")

testar_quickselect()


