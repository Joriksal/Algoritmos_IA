import heapq    # Importamos la librería heapq, que permite manejar colas de prioridad (min-heaps)

# Importamos networkx para representar grafos y matplotlib.pyplot para visualizarlos
import networkx as nx   
import matplotlib.pyplot as plt

# Definimos el grafo como un diccionario. Cada nodo tiene una lista de tuplas (vecino, peso)
# Es un grafo no dirigido, por eso las conexiones están duplicadas en ambos sentidos.
grafo = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('E', 10), ('D', 14), ('C', 4), ('G', 2)],
    'G': [('F', 2)],  
    'H': [('A', 8), ('B', 11)]
}

# Función que implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST)
def prim(grafo, nodo_inicio):
    visitados = set()   # Conjunto para almacenar nodos ya incluidos en el MST
    arbol = []          # Lista donde guardamos las aristas seleccionadas del MST
    cola = []           # Cola de prioridad para seleccionar la arista con menor peso

    # Agregamos el nodo inicial a los visitados
    visitados.add(nodo_inicio)

    # Añadimos a la cola todas las aristas que salen del nodo inicial
    for vecino, peso in grafo[nodo_inicio]:
        heapq.heappush(cola, (peso, nodo_inicio, vecino))   # (peso, desde, hacia)

    print(f"Inicio en el nodo: {nodo_inicio}")

    # Mientras haya aristas por revisar en la cola
    while cola:
        # Sacamos la arista con el menor peso
        peso, desde, hacia = heapq.heappop(cola)

        # Si el nodo destino ya fue visitado, ignoramos esta arista
        if hacia in visitados:
            continue

        # Agregamos la arista seleccionada al árbol
        print(f"Agregando arista ({desde} - {hacia}) con peso {peso}")
        arbol.append((desde, hacia, peso))

        # Marcamos el nodo como visitado
        visitados.add(hacia)

         # Por cada vecino del nuevo nodo visitado
        for vecino, p in grafo[hacia]:
            # Si aún no ha sido visitado, añadimos su arista a la cola
            if vecino not in visitados:
                heapq.heappush(cola, (p, hacia, vecino))

    # Al final devolvemos todas las aristas que forman el Árbol de Expansión Mínima
    return arbol

# Ejecutamos el algoritmo de Prim desde el nodo 'A' y guardamos el MST resultante
mst = prim(grafo, 'A')

# Imprimimos el resultado: el Árbol de Expansión Mínima como lista de aristas con peso
print("\nArbol de Expansion Minima:")
for desde, hacia, peso in mst:
    print(f"{desde} - {hacia} : {peso}")

# Función que dibuja el MST usando NetworkX y matplotlib
def mostrar_mst(mst):
    G = nx.Graph()  # Creamos un grafo vacío

    # Añadimos las aristas al grafo, incluyendo el peso
    for desde, hacia, peso in mst:
        G.add_edge(desde, hacia, weight=peso)

    # Calculamos posiciones de los nodos para el layout gráfico
    pos = nx.spring_layout(G)

    # Obtenemos los pesos de las aristas para mostrarlos en el dibujo
    pesos = nx.get_edge_attributes(G, 'weight')

    # Dibujamos nodos y aristas
    nx.draw(G,pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)

    # Título del gráfico
    plt.title("Árbol de Expansión Mínima (Prim)")
    plt.show()

# Mostramos el grafo resultante del MST gráficamente
mostrar_mst(mst)