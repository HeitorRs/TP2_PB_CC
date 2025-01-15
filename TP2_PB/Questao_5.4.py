import threading
import time
import random

def max_in_sublist(sublist, result, index):
    result[index] = max(sublist)

def parallel_max(lst, num_threads):
    chunk_size = len(lst) // num_threads
    chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    
    threads = []
    result = [None] * num_threads
    
    for i in range(num_threads):
        thread = threading.Thread(target=max_in_sublist, args=(chunks[i], result, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return max(result)

def sequential_max(lst):
    return max(lst)

def test_max_operations(list_sizes):
    num_threads = 4
    print(f"Usando {num_threads} threads para paralelização.")
    
    for size in list_sizes:
        print(f"\nTestando lista de tamanho: {size}")
        
        lst = random.sample(range(0, size), size)
        
        start_time = time.time()
        max_sequential = sequential_max(lst)
        sequential_time = time.time() - start_time
        print(f"Máximo sequencial: {max_sequential}")
        print(f"Tempo sequencial: {sequential_time:.5f} segundos")
        
        start_time = time.time()
        max_parallel = parallel_max(lst, num_threads)
        parallel_time = time.time() - start_time
        print(f"Máximo paralelo: {max_parallel}")
        print(f"Tempo paralelo: {parallel_time:.5f} segundos")
        
        print(f"Speedup: {sequential_time / parallel_time:.2f}")

if __name__ == "__main__":
    list_sizes = [100000, 500000, 1000000, 5000000]
    
    test_max_operations(list_sizes)

