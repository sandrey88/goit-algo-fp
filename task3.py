"""
Завдання 3. Дерева, алгоритм Дейкстри

"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = []

    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = []
        if destination not in self.graph:
            self.graph[destination] = []
        self.graph[source].append((destination, weight))
        self.edges.append((source, destination, weight))

    def dijkstra(self, start):
        # Відстані від стартової вершини до кожної іншої вершини
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        # Пріоритетна черга для вершини (відстань, вершина)
        priority_queue = [(0, start)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Якщо поточна відстань більша за збережену, продовжуємо
            if current_distance > distances[current_node]:
                continue

            # Перевірка сусідів поточної вершини
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def visualize(self, shortest_paths=None, pos=None):
        G = nx.DiGraph()

        # Додаємо ребра до графа
        for edge in self.edges:
            source, destination, weight = edge
            G.add_edge(source, destination, weight=weight)

        if pos is None:
            pos = nx.spring_layout(G, seed=42)  # Позиціонування вершин з фіксованим seed

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_color='black', edge_color='gray')
        
        edge_labels = {(source, destination): weight for source, destination, weight in self.edges}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.5)

        if shortest_paths:
            path_edges = list(zip(shortest_paths, shortest_paths[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=shortest_paths, node_color='r', node_size=1500)
        
        plt.title("Візуалізація графа")
        plt.axis('off')
        plt.show()

    def visualize_path(self, start, end, pos=None):
        distances = self.dijkstra(start)
        path = []
        if distances[end] != float('inf'):
            current_node = end
            while current_node != start:
                for neighbor, weight in self.graph.items():
                    if current_node in [n for n, w in weight] and distances[neighbor] == distances[current_node] - dict(weight)[current_node]:
                        path.append(current_node)
                        current_node = neighbor
                        break
            path.append(start)
            path.reverse()
        
        self.visualize(path, pos)

if __name__ == "__main__":
    # Створення графа
    graph = Graph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 5)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 4)

    # Обчислення найкоротших шляхів від вершини 0
    start = 0
    distances = graph.dijkstra(start)

    # Виведення найкоротших шляхів
    for node, distance in distances.items():
        if distance != float('inf'):
            print(f"Найкоротший шлях від {start} до {node}: {distance}")
        else:
            print(f"Вершина {node} недосяжна від {start}")

    # Візуалізація графа
    graph.visualize()

    # Візуалізація графа з підсвіченим шляхом від 0 до 4
    graph.visualize_path(0, 4)
