import random

def quickselect_k_menores(array, low, high, k):
    if low < high:
        indice_pivo = partition(array, low, high)

        num_elementos_esquerda = indice_pivo - low + 1
        
        if num_elementos_esquerda == k:
            return array[low:indice_pivo + 1]
        elif num_elementos_esquerda > k:
            return quickselect_k_menores(array, low, indice_pivo - 1, k)
        else:
            return array[low:indice_pivo + 1] + quickselect_k_menores(array, indice_pivo + 1, high, k - num_elementos_esquerda)
    
    return array[low:low + k]

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    
    pivo = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

array = [10, 9, 4, 5, 8, 6, 11, 26, 30, 35, 12, 1, 14]
k = 5
k_menores = quickselect_k_menores(array, 0, len(array) - 1, k)
print(f"Os {k} menores elementos são: {k_menores}")




