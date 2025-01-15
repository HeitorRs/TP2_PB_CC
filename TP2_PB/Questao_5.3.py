import random
import multiprocessing
import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    with multiprocessing.Pool(2) as pool:
        left_result = pool.apply_async(merge_sort, (arr[:mid],))
        right_result = pool.apply_async(merge_sort, (arr[mid:],))

        left = left_result.get()
        right = right_result.get()

    return merge(left, right)

def measure_time(arr_size, runs=5):
    seq_times = []
    par_times = []

    for _ in range(runs):
        arr = [random.randint(1, arr_size) for _ in range(arr_size)]

        # Tempo sequencial
        start = time.time()
        merge_sort(arr)
        end = time.time()
        seq_times.append(end - start)

        # Tempo paralelo
        start = time.time()
        merge_sort_parallel(arr)
        end = time.time()
        par_times.append(end - start)

    return sum(seq_times) / runs, sum(par_times) / runs

def plot_comparison():
    sizes = [10000, 100000, 1000000, 2000000, 3000000]
    seq_times = []
    par_times = []

    for size in sizes:
        seq_time, par_time = measure_time(size)
        print(f"Tamanho da lista: {size}\nTempo médio sequencial: {seq_time:4f} segundos\nTempo médio paralelo: {par_time:4f} segundos\n")
        seq_times.append(seq_time)
        par_times.append(par_time)

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, seq_times, label="Sequencial", marker='o')
    plt.plot(sizes, par_times, label="Paralela", marker='o')
    plt.xscale('log')
    plt.xlabel('Tamanho da Lista (escala log)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Comparação de Tempo vs Tamanho da Lista (MergeSort Sequencial vs Paralelo)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_comparison()







