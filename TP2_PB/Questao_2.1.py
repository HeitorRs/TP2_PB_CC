import random
import time

def escolher_pivo(lista, metodo='mediano'):
    if metodo == 'primeiro':
        return lista[0]
    elif metodo == 'ultimo':
        return lista[-1]
    elif metodo == 'maior':
        return max(lista)
    elif metodo == 'menor':
        return min(lista)
    elif metodo == 'mediano':
        lista_ordenada = sorted(lista)
        return lista_ordenada[len(lista_ordenada) // 2]
    elif metodo == 'aleatorio':
        return random.choice(lista)

def quicksort(lista, metodo_pivo='mediano'):
    if len(lista) <= 1:
        return lista
    pivo = escolher_pivo(lista, metodo_pivo)
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores, metodo_pivo) + iguais + quicksort(maiores, metodo_pivo)

def comparar_desempenho(lista):
    for metodo in ['primeiro', 'ultimo', 'maior', 'menor', 'mediano', 'aleatorio']:
        tempos = []
        for _ in range(5):
            inicio = time.time()
            quicksort(lista, metodo)
            fim = time.time()
            tempos.append(fim - inicio)
        
        tempo_medio = sum(tempos) / len(tempos)
        print(f"Desempenho médio usando o pivô '{metodo}': {tempo_medio:.6f} segundos")

lista = [random.randint(0, 1000) for _ in range(1000)]
comparar_desempenho(lista)



