import time
import random
import matplotlib.pyplot as plt

class DNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, value):
        new_node = DNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        new_node = DNode(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

def run_tests():
    num_operations = [2**i for i in range(1, 11)]
    
    insert_beginning_times = []
    insert_end_times = []
    delete_node_times = []
    
    for ops in num_operations:
        linked_list = DoublyLinkedList()
        
        random_values = random.sample(range(1000), 1000)
        for value in random_values:
            linked_list.insert_at_end(value)

        insert_times = []
        for _ in range(5):
            start_time = time.perf_counter()
            for _ in range(ops):
                linked_list.insert_at_beginning(random.randint(1, 1000))
            end_time = time.perf_counter()
            insert_times.append(end_time - start_time)
        insert_beginning_times.append(sum(insert_times) / 5)

        insert_times = []
        for _ in range(5):
            start_time = time.perf_counter()
            for _ in range(ops):
                linked_list.insert_at_end(random.randint(1, 1000))
            end_time = time.perf_counter()
            insert_times.append(end_time - start_time)
        insert_end_times.append(sum(insert_times) / 5)

        delete_times = []
        for _ in range(5):
            random_value = random.choice(random_values)
            start_time = time.perf_counter()
            for _ in range(ops):
                linked_list.delete_node(random_value)
            end_time = time.perf_counter()
            delete_times.append(end_time - start_time)
            
            linked_list = DoublyLinkedList()
            for value in random_values:
                linked_list.insert_at_end(value)
        
        delete_node_times.append(sum(delete_times) / 5)
    
    return num_operations, insert_beginning_times, insert_end_times, delete_node_times

def plot_times():
    num_operations, insert_beginning_times, insert_end_times, delete_node_times = run_tests()
    
    plt.plot(num_operations, insert_beginning_times, label='Inserir no Início', color='blue', marker='o')
    plt.plot(num_operations, insert_end_times, label='Inserir no Final', color='green', marker='s')
    plt.plot(num_operations, delete_node_times, label='Deletar Nó', color='red', marker='^')
    
    plt.xlabel('Número de Operações')
    plt.ylabel('Tempo Médio de Execução (segundos)')
    plt.title('Tempo Médio de Execução das Operações em Lista Duplamente Encadeada')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_times()
