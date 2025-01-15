import random
import time
from multiprocessing import Pool, cpu_count
import threading

def partial_sum(numbers):
    return sum(numbers)

def parallel_sum_threading(vector, num_threads):
    chunk_size = len(vector) // num_threads
    threads = []
    results = []

    def worker(start, end, result_list):
        partial_result = sum(vector[start:end])
        result_list.append(partial_result)

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else len(vector)
        thread = threading.Thread(target=worker, args=(start, end, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

def main():
    vector_size = 10_000_000
    vector = [random.randint(1, 100_000) for _ in range(vector_size)]

    start_seq = time.time()
    total_sequential = sum(vector)
    end_seq = time.time()
    print(f"Soma Sequencial: {total_sequential}")
    print(f"Tempo Sequencial: {end_seq - start_seq:.4f} segundos")

    start_parallel_mp = time.time()
    num_processes = cpu_count()
    chunk_size = len(vector) // num_processes
    chunks = [vector[i:i + chunk_size] for i in range(0, len(vector), chunk_size)]

    with Pool(processes=num_processes) as pool:
        partial_sums = pool.map(partial_sum, chunks)

    total_parallel_mp = sum(partial_sums)
    end_parallel_mp = time.time()
    print(f"Soma Paralela (multiprocessing): {total_parallel_mp}")
    print(f"Tempo Paralelo (multiprocessing): {end_parallel_mp - start_parallel_mp:.4f} segundos")

    start_parallel_thread = time.time()
    total_parallel_thread = parallel_sum_threading(vector, num_threads=cpu_count())
    end_parallel_thread = time.time()
    print(f"Soma Paralela (threading): {total_parallel_thread}")
    print(f"Tempo Paralelo (threading): {end_parallel_thread - start_parallel_thread:.4f} segundos")

if __name__ == "__main__":
    main()

