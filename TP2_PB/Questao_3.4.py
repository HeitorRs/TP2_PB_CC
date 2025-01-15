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

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        print(" -> ".join(map(str, values)))

    def sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head.next
        while current:
            key = current
            key_value = current.value
            prev = current.prev

            while prev and prev.value > key_value:
                prev.next.value = prev.value
                prev = prev.prev
            if prev:
                prev.next.value = key_value
            else:
                self.head.value = key_value

            current = current.next


def merge_sorted_lists(list1, list2):
    merged_list = DoublyLinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.value < current2.value:
            merged_list.insert_at_end(current1.value)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.value)
            current2 = current2.next

    while current1:
        merged_list.insert_at_end(current1.value)
        current1 = current1.next

    while current2:
        merged_list.insert_at_end(current2.value)
        current2 = current2.next

    return merged_list

#Criar e ordenar uma lista
dll = DoublyLinkedList()
dll.insert_at_end(4)
dll.insert_at_end(2)
dll.insert_at_end(5)
dll.insert_at_end(1)
dll.insert_at_end(3)
print("Lista desordenada:")
dll.display()
dll.sort()
print("Lista Ordenada:")
dll.display()

#Mesclar duas listas
list1 = DoublyLinkedList()
list1.insert_at_end(1)
list1.insert_at_end(7)
list1.insert_at_end(5)
list1.insert_at_end(11)
list1.sort()
print("---------------------\nLista 1 ordenada:")
list1.display()

list2 = DoublyLinkedList()
list2.insert_at_end(2)
list2.insert_at_end(99)
list2.insert_at_end(3)
list2.insert_at_end(23)
list2.sort()
print("Lista 2 ordenada:")
list2.display()

merged_list = merge_sorted_lists(list1, list2)

print("Lista 1 e 2 mescladas:")
merged_list.display()
