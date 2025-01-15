import random
import time
import multiprocessing
import threading

def soma_sequencial(vetor):
    return sum(vetor)

def somar_parte(vetor, inicio, fim):
    return sum(vetor[inicio:fim])

def soma_multiprocessing(vetor):
    num_processos = 4
    chunk_size = len(vetor) // num_processos
    with multiprocessing.Pool(num_processos) as pool:
        ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processos)]
        resultados = pool.starmap(somar_parte, [(vetor, inicio, fim) for inicio, fim in ranges])
    return sum(resultados)

def soma_threading(vetor):
    def somar_parte(inicio, fim):
        return sum(vetor[inicio:fim])

    num_threads = 4
    chunk_size = len(vetor) // num_threads
    threads = []
    resultados = [0] * num_threads

    def worker(i, inicio, fim):
        resultados[i] = somar_parte(inicio, fim)

    for i in range(num_threads):
        inicio = i * chunk_size
        fim = (i + 1) * chunk_size
        thread = threading.Thread(target=worker, args=(i, inicio, fim))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(resultados)

def calcular_tempo_medio(funcao, vetor, num_execucoes=5):
    tempos = []
    for _ in range(num_execucoes):
        inicio = time.time()
        funcao(vetor)
        fim = time.time()
        tempos.append(fim - inicio)
    return sum(tempos) / len(tempos)


if __name__ == "__main__":
    vetor = [random.randint(1, 100000) for _ in range(10000000)]

    # Teste para soma sequencial
    tempo_medio_sequencial = calcular_tempo_medio(soma_sequencial, vetor)
    print(f"Soma Sequencial - Tempo médio: {tempo_medio_sequencial:.4f} segundos")

    # Teste para soma com multiprocessing
    tempo_medio_multiprocessing = calcular_tempo_medio(soma_multiprocessing, vetor)
    print(f"Soma com Multiprocessing - Tempo médio: {tempo_medio_multiprocessing:.4f} segundos")

    # Teste para soma com threading
    tempo_medio_threading = calcular_tempo_medio(soma_threading, vetor)
    print(f"Soma com Threading - Tempo médio: {tempo_medio_threading:.4f} segundos")

