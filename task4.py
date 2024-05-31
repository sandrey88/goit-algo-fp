"""
Завдання 4. Візуалізація піраміди

"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

# Рекурсивне додавання вузлів та ребер до графа, встановлення позиції вузлів
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол до графа з відповідним кольором та міткою
        graph.add_node(node.id, color=node.color, label=node.val)
        
        # Якщо існує лівий нащадок, додаємо його
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        
        # Якщо існує правий нащадок, додаємо його
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Візуалізація дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Створення порожнього графа
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додавання всіх вузлів та ребер до графа

    # Кольори та мітки вузлів для візуалізації
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарного дерева з бінарної купи, представленої у вигляді списку
def build_heap_tree(heap):

    nodes = [Node(key) for key in heap]  # Створення вузлів для кожного елемента купи
    n = len(nodes)
    
    # Встановлення лівого та правого нащадків для кожного вузла
    for i in range(n):
        if 2*i + 1 < n:
            nodes[i].left = nodes[2*i + 1]
        if 2*i + 2 < n:
            nodes[i].right = nodes[2*i + 2]
    
    return nodes[0] if nodes else None  # Повернення кореневого вузла або None, якщо купа порожня

if __name__ == "__main__":
    # Приклад бінарної купи у вигляді списку
    heap = [10, 5, 4, 3, 1, 0]

    # Побудова дерева з купи
    heap_tree_root = build_heap_tree(heap)

    # Відображення дерева
    draw_tree(heap_tree_root)
