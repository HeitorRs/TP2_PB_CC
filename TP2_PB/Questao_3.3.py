import time
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.value == value:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def measure_time_search(linked_list, value):
    start_time = time.perf_counter()
    position = linked_list.search(value)
    end_time = time.perf_counter()
    return end_time - start_time, position

def measure_time_reverse(linked_list):
    start_time = time.perf_counter()
    linked_list.reverse()
    end_time = time.perf_counter()
    return end_time - start_time

def run_tests():
    sizes = [2**i for i in range(1, 16)]
    search_times = []
    reverse_times = []

    for size in sizes:
        linked_list = LinkedList()
        values = random.sample(range(size * 2), size)
        for value in values:
            linked_list.insert_at_end(value)

        search_value = random.choice(values)

        total_search_time = 0
        for _ in range(5):
            time_taken, position = measure_time_search(linked_list, search_value)
            total_search_time += time_taken

        average_search_time = total_search_time / 5
        search_times.append(average_search_time)

        total_reverse_time = 0
        for _ in range(5):
            time_taken = measure_time_reverse(linked_list)
            total_reverse_time += time_taken

        average_reverse_time = total_reverse_time / 5
        reverse_times.append(average_reverse_time)

        print(f"Tamanho da lista: {size}, Valor buscado: {search_value}, Posição encontrada: {position}"
              f"\nTempo médio de busca: {average_search_time:.8f} segundos, "
              f"\nTempo médio de inversão da lista: {average_reverse_time:.8f} segundos\n--------------------------------------------")
    return sizes, search_times, reverse_times

def plot_times():
    sizes, search_times, reverse_times = run_tests()

    plt.plot(sizes, search_times, label='Tempo de busca', color='blue', marker='o')
    plt.plot(sizes, reverse_times, label='Tempo de inversão', color='red', marker='x')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo Médio (segundos)')
    plt.title('Tempo Médio de Busca e Inversão por Tamanho da Lista')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

plot_times()
