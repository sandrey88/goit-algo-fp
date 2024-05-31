"""
Завдання 5. Візуалізація обходу бінарного дерева

"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None, title="Figure"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    if visited_nodes:
        for node_id, color in visited_nodes.items():
            colors[list(tree.nodes).index(node_id)] = color

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def interpolate_color(step, max_steps):
    start_color = (18, 150, 240)  # RGB для #1296F0
    end_color = (230, 240, 255)  # Світлий відтінок синього
    r = start_color[0] + (end_color[0] - start_color[0]) * step / max_steps
    g = start_color[1] + (end_color[1] - start_color[1]) * step / max_steps
    b = start_color[2] + (end_color[2] - start_color[2]) * step / max_steps
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}"

def bypass_d(root):
    stack = [(root, 0)]
    visited_nodes = {}
    max_steps = len(list(iterate_nodes(root)))
    step = 0

    while stack:
        node, depth = stack.pop()
        color = interpolate_color(step, max_steps)
        visited_nodes[node.id] = color
        draw_tree(root, visited_nodes, title="Обхід дерева в глибину")
        step += 1

        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))

def iterate_nodes(node):
    if node is not None:
        yield node
        yield from iterate_nodes(node.left)
        yield from iterate_nodes(node.right)

def bypass_b(root):
    queue = deque([(root, 0)])
    visited_nodes = {}
    max_steps = len(list(iterate_nodes(root)))
    step = 0

    while queue:
        node, depth = queue.popleft()
        color = interpolate_color(step, max_steps)
        visited_nodes[node.id] = color
        draw_tree(root, visited_nodes, title="Обхід дерева в ширину")
        step += 1

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід в глибину з візуалізацією
print("Обхід дерева в глибину...")
bypass_d(root)

# Обхід в ширину з візуалізацією
print("Обхід дерева в ширину...")
bypass_b(root)
