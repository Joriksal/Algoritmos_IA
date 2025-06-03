import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Algoritmo de Dijkstra con impresión paso a paso (verbose)
def dijkstra_verbose(graph, start):
    # Inicialización de estructuras: distancias a infinito y caminos previos como None
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0  # La distancia al nodo origen es 0

    queue = [(0, start)]  # Cola de prioridad con tuplas (distancia, nodo)
    visited = set()       # Conjunto para rastrear nodos ya visitados

    print(f"\nInicio del algoritmo de Dijkstra desde el nodo '{start}':\n")

    # Mientras haya nodos en la cola...
    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Obtener el nodo más cercano

        if current_node in visited:
            continue  # Si ya fue visitado, lo ignoramos
        visited.add(current_node)

        print(f"Visitando nodo: {current_node} con distancia actual: {current_distance}")

        # Recorrer todos los vecinos del nodo actual
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # Calcular nueva distancia

            # Si la nueva distancia es menor, se actualiza
            if distance < distances[neighbor]:
                print(f" → Actualizando distancia de {neighbor} de {distances[neighbor]} a {distance}")
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))  # Agregar vecino a la cola

    # Mostrar distancias finales desde el nodo origen
    print("\nDistancias finales desde el nodo origen:")
    for node in graph:
        print(f" - {node}: {distances[node]}")

    # Reconstrucción y despliegue de los caminos más cortos desde el nodo origen
    print("\nCaminos más cortos:")
    for node in graph:
        if node == start:
            continue
        path = []
        current = node
        while current:
            path.append(current)
            current = previous[current]
        path = path[::-1]  # Invertir el camino para mostrar desde el origen
        print(f" - {start} → {node}: {' -> '.join(path)}")

    return distances, previous  # Retornar resultados

# Función auxiliar que construye la lista de aristas del grafo
def build_graph_data():
    return [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('C', 'E', 3),
        ('D', 'F', 2),
        ('E', 'F', 1),
        ('E', 'G', 5),
        ('F', 'G', 2),
        ('B', 'E', 7),
        ('A', 'E', 10)
    ]


# Función que dibuja el grafo y los caminos más cortos encontrados
def draw_dijkstra_graph(graph_data, source, previous):
    G = nx.DiGraph()  # Crear grafo dirigido

    # Agregar las aristas con pesos al grafo
    for u, v, w in graph_data:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)  # Disposición visual automática
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Etiquetas con pesos

    # Dibujar nodos y aristas normales
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Dibujar las aristas que forman parte del camino más corto en rojo
    for target in G.nodes:
        if target == source or previous[target] is None:
            continue
        path = []
        current = target
        while current != source:
            path.append((previous[current], current))
            current = previous[current]
        nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='red', width=2)

    plt.title(f"Caminos más cortos desde el nodo '{source}' (Dijkstra)")
    plt.axis('off')
    plt.show()

# Código principal
if __name__ == "__main__":
    graph_data = build_graph_data()  # Crear las aristas del grafo

    # Convertir la lista de aristas a un diccionario de adyacencia
    adjacency = {}
    for u, v, w in graph_data:
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        adjacency[u].append((v, w))

    source = 'A'  # Nodo origen
    distances, previous = dijkstra_verbose(adjacency, source)  # Ejecutar Dijkstra
    draw_dijkstra_graph(graph_data, source, previous)  # Dibujar el resultado
