import time
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def delete_node(self, value):
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        
        if not current:
            return
        
        prev.next = current.next

def run_tests():
    linked_list = LinkedList()
    
    random_values = random.sample(range(1000), 1000)
    for value in random_values:
        linked_list.insert_at_end(value)

    insert_beginning_times = []
    insert_end_times = []
    delete_node_times = []
    
    num_operations = [2**i for i in range(1, 11)]
    
    for ops in num_operations:

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
            
            linked_list = LinkedList()
            for value in random_values:
                linked_list.insert_at_end(value)
        
        delete_node_times.append(sum(delete_times) / 5)
    
    return num_operations, insert_beginning_times, insert_end_times, delete_node_times

def plot_times():
    num_operations, insert_beginning_times, insert_end_times, delete_node_times = run_tests()
    
    plt.plot(num_operations, insert_beginning_times, label='Insert at Beginning', color='blue', marker='o')
    plt.plot(num_operations, insert_end_times, label='Insert at End', color='green', marker='s')
    plt.plot(num_operations, delete_node_times, label='Delete Node', color='red', marker='^')
    
    plt.xlabel('Número de Operações')
    plt.ylabel('Tempo Médio de Execução (segundos)')
    plt.title('Tempo Médio de Execução das Operações em Lista Encadeada Simples')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_times()




