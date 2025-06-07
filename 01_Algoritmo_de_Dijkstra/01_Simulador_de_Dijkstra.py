import networkx as nx               # Libreria para crear y manejar grafos (nodos, aristas)
import matplotlib.pyplot as plt     # Libreria para graficar el grafo y caminos
import heapq                        # Librerias para manejar una cola de prioridad (min-heap)

# Algoritmo de Dijkstra con impresión paso a paso
def dijkstra_verbose(graph, start):
    # Inicialización de estructuras: distancias a infinito y caminos previos como None
    distances = {node: float('inf') for node in graph}  # Al inicio, se asume que todos los nodos estan lejos (infinito)
    previous = {node: None for node in graph}           # No conocemos aun como llegamos a cada nodo
    distances[start] = 0                                # La distancia al nodo origen es 0 porque estamos alli

    # Creamos la cola de prioridad con la tupla (distancia, nodo)    
    queue = [(0, start)]  # Aqui se almacenan los nodos pendientes de visitar, ordenados por menor costo
    visited = set()       # Conjunto de nodos ya visitados para no repetir

    print(f"\nInicio del algoritmo de Dijkstra desde el nodo '{start}':\n")

    # Recorremos la cola de prioridad mientras haya nodos
    while queue:
        current_distance, current_node = heapq.heappop(queue)  # Obtener el nodo con menor distancia conocida

        if current_node in visited:
            continue  # Si ya fue visitado, lo ignoramos
        visited.add(current_node)

        print(f"Visitando nodo: {current_node} con distancia actual: {current_distance}")

        # Recorrer todos los vecinos del nodo actual
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # Calcular nueva distancia

            # Si encontramos una ruta mas cortas, actualizamos
            if distance < distances[neighbor]:
                print(f" → Actualizando distancia de {neighbor} de {distances[neighbor]} a {distance}")
                distances[neighbor] = distance                  # Actualizar la nueva distancia
                previous[neighbor] = current_node               # Guardamos quien nos llevo a este nodo
                heapq.heappush(queue, (distance, neighbor))     # Agregar el vecino a la cola de prioridad

    # Imprimimos las distancias finales desde el nodo de inicio
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

# Función que construye el grafo a partir de una lista de conexiones
def build_graph_data():
    # Cada tupla representa una ruta directa entre sucursales de una empresa de envios
    # El peso representa el costo o timepo entre ellas
    return [
        ('A', 'B', 1),  # Ruta de sucursal A a B con peso 1
        ('A', 'C', 4),  # Ruta de sucursal A a C con peso 4
        ('B', 'C', 2),  # Ruta de sucursal B a C con peso 2 
        ('B', 'D', 5),  # Ruta de sucursal B a D con peso 5
        ('C', 'D', 1),  # Ruta de sucursal C a D con peso 1
        ('C', 'E', 3),  # Ruta de sucursal C a E con peso 3
        ('D', 'F', 2),  # Ruta de sucursal D a F con peso 2
        ('E', 'F', 1),  # Ruta de sucursal E a F con peso 1
        ('E', 'G', 5),  # Ruta de sucursal E a G con peso 5
        ('F', 'G', 2),  # Ruta de sucursal F a G con peso 2
        ('B', 'E', 7),  # Ruta de sucursal B a E con peso 7
        ('A', 'E', 10)  # Ruta de sucursal A a E con peso 10
    ]


# Función que dibuja el grafo y los caminos más cortos encontrados
def draw_dijkstra_graph(graph_data, source, previous):
    G = nx.DiGraph()  # Crear grafo dirigido (las conexiones tienen direccion)

    # Agregar cada conexion con su peso
    for u, v, w in graph_data:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)  # Posicion automatica para visualizacion
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Pesos de las aristas

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
    plt.axis('off')     # Quitamos ejes del grafico
    plt.show()

# Código principal que se ejecuta al correr el script
if __name__ == "__main__":
    graph_data = build_graph_data()  # Obtenemod la lista de conexiones del grafo

    # Creamos un diccionario de adyacencia para representar el grafo
    adjacency = {}
    for u, v, w in graph_data:
        if u not in adjacency:
            adjacency[u] = []
        if v not in adjacency:
            adjacency[v] = []
        adjacency[u].append((v, w))     #Agregamos cada conexion (u -> v con peso w)

    source = 'A'  # Nodo origen: Simulamos que la ruta parte desde la sucursal A

    # Ejecutar el algoritmo de Dijkstra y dibujar el grafo desde el nodo origen (nodo A)
    distances, previous = dijkstra_verbose(adjacency, source) 

    # Dibujar el grafo y los caminos más cortos encontrados
    draw_dijkstra_graph(graph_data, source, previous)  
