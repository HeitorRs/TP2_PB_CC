def quickselect(array, low, high, k):
    if low == high:
        return array[low]
    
    indice_pivo = partition(array, low, high)

    if k == indice_pivo:
        return array[k]
    elif k < indice_pivo:
        return quickselect(array, low, indice_pivo - 1, k)
    else:
        return quickselect(array, indice_pivo + 1, high, k)

def partition(array, low, high):
    pivo = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1

def encontrar_mediana(array):
    n = len(array)
    if n % 2 == 1:
        return quickselect(array, 0, n - 1, n // 2)
    else:
        mediana_esq = quickselect(array, 0, n - 1, n // 2 - 1)
        mediana_dir = quickselect(array, 0, n - 1, n // 2)
        return (mediana_esq + mediana_dir) / 2


array = [10, 4, 5, 8, 6, 11, 26, 30, 35, 12, 14, 22]
mediana = encontrar_mediana(array)
print(f"A mediana é: {mediana}")

