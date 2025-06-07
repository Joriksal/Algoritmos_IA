import heapq
import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

def prim(grafo, nodo_inicio):
    visitados = set()
    arbol = []
    cola = []

    visitados.add(nodo_inicio)
    for vecino, peso in grafo[nodo_inicio]:
        heapq.heappush(cola, (peso, nodo_inicio, vecino))

    print(f"Inicio en el nodo: {nodo_inicio}")

    while cola:
        peso, desde, hacia = heapq.heappop(cola)

        if hacia in visitados:
            continue

        print(f"Agregando arista ({desde} - {hacia}) con peso {peso}")
        arbol.append((desde, hacia, peso))
        visitados.add(hacia)

        for vecino, p in grafo[hacia]:
            if vecino not in visitados:
                heapq.heappush(cola, (p, hacia, vecino))

    return arbol

mst = prim(grafo, 'A')
print("\nArbol de Expansion Minima:")
for desde, hacia, peso in mst:
    print(f"{desde} - {hacia} : {peso}")

def mostrar_mst(mst):
    G = nx.Graph()
    for desde, hacia, peso in mst:
        G.add_edge(desde, hacia, weight=peso)

    pos = nx.spring_layout(G)
    pesos = nx.get_edge_attributes(G, 'weight')

    nx.draw(G,pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    plt.title("Árbol de Expansión Mínima (Prim)")
    plt.show()

mostrar_mst(mst)