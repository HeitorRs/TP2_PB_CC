from multiprocessing import Process, Manager
import time
import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_subtree(node, target, result):
    if node is None or result["found"]:
        return
    if node.value == target:
        result["found"] = True
        result["value"] = node.value
        return
    search_subtree(node.left, target, result)
    search_subtree(node.right, target, result)

def parallel_search(root, target):
    if root is None:
        return None

    with Manager() as manager:
        result = manager.dict({"found": False, "value": "Não encontrado"})

        left_proc = Process(target=search_subtree, args=(root.left, target, result))
        right_proc = Process(target=search_subtree, args=(root.right, target, result))

        left_proc.start()
        right_proc.start()

        left_proc.join()
        right_proc.join()

        return result["value"]

def create_balanced_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_balanced_tree(values[:mid])
    root.right = create_balanced_tree(values[mid+1:])
    return root

def measure_execution_time(tree_size, target):
    values = list(range(1, tree_size + 1))
    root = create_balanced_tree(values)
    start_time = time.time()
    found_value = parallel_search(root, target)
    end_time = time.time()
    return found_value, end_time - start_time

if __name__ == '__main__':
    print("Testando busca paralela em árvores binárias:")
    for i in range(1, 6):
        tree_size = 2 ** i
        target = random.randint(1, tree_size-1)
        found_value, exec_time = measure_execution_time(tree_size, target)
        print(f"Tamanho da árvore: {tree_size}, Valor procurado: {target}, Valor encontrado: {found_value}, Tempo: {exec_time:.6f} segundos")


