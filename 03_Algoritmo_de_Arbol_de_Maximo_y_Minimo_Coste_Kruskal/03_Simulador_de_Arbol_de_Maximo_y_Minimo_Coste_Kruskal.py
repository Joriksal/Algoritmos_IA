import matplotlib.pyplot as plt     # Importar matplotlib para graficar
import networkx as nx               # Importar NetworkX para trabajar con grafos
import time                         # Importar time para simular el paso del tiempo en la visualización

# Creamos una clase para simular el algoritmo de Kruskal
class KruskalSimulator: 
    def __init__(self):
        # Inicializamos el grafo y los pasos
        self.graph = {  
            'nodes': [],        # Lista de nodos
            'edges': []         # Lista de aristas (edges) con sus pesos
        }
        self.steps = []         # Lista para almacenar los pasos del algoritmo
        self.G = nx.Graph()     # Grafo de NetworkX para visualización
    
    # Función para agregar un nodo al grafo
    def add_node(self, node):
        if node not in self.graph['nodes']:     # Verificamos si el nodo ya existe
            self.graph['nodes'].append(node)    # Agregamos el nodo a la lista de nodos
            self.G.add_node(node)               # Agregamos el nodo al grafo de NetworkX
    
     # Función para agregar una arista (conexión) entre dos nodos, con un peso (coste)
    def add_edge(self, node1, node2, weight):
        self.graph['edges'].append((node1, node2, weight))  # Agregamos la arista con su peso a la lista de aristas
        self.G.add_edge(node1, node2, weight=weight)        # Agregamos la arista al grafo de NetworkX
    
    # Función para encontrar el "representante" de un nodo en el conjunto disjunto
    def find_parent(self, parent, node):
        if parent[node] == node:       # Si el nodo es su propio padre, lo retornamos      
            return node
        return self.find_parent(parent, parent[node])   # Si no, buscamos un ancestro mas arriba
    
    # Implementación del algoritmo de Kruskal (puede encontrar árbol de mínimo o máximo coste)
    def kruskal(self, max_spanning=False):
        # Ordenamos las aristas por su peso: de menor a mayor (o de mayor a menor si max_spanning=True)
        edges = sorted(self.graph['edges'], key=lambda item: item[2], reverse=max_spanning)

        parent = {}     # Diccionario para almacenar el padre de cada nodo
        rank = {}       # Diccionario para almacenar el rango de cada nodo (para optimizar la unión de conjuntos)
        
        # Inicializamos cada nodo como su propio padre y su rango en 0
        for node in self.graph['nodes']:
            parent[node] = node
            rank[node] = 0
        
        mst = []        # Lista para almacenar el árbol de expansión mínima (o máxima)
        step_count = 1  # Contador de pasos para el seguimiento del algoritmo
        
         # Recorremos todas las aristas ordenadas
        for edge in edges:
            node1, node2, weight = edge
            root1 = self.find_parent(parent, node1) # Encontramos el padre del primer nodo
            root2 = self.find_parent(parent, node2) # Encontramos el padre del segundo nodo
            
             # Creamos un diccionario para guardar la información de este paso
            step_info = {
                'step': step_count,         # Número del paso actual
                'edge': edge,               # Arista considerada en este paso
                'action': None,             # Acción tomada en este paso (AGREGAR u OMITIR)
                'mst': mst.copy(),          # Copia del árbol de expansión actual
                'parent': parent.copy(),    # Copia del estado de los padres
                'rank': rank.copy()         # Copia del estado de los rangos
            }
            
             # Si los nodos no están en el mismo conjunto, podemos unirlos
            if root1 != root2:
                mst.append(edge)                    # Agregamos la arista al árbol de expansión
                step_info['action'] = "AGREGAR"     # Actualizamos la acción a AGREGAR
                
                # Unimos los conjuntos con menor rango al de mayor rango
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1    # Aumentamos el rango del nuevo padre si ambos tenían el mismo rango
            else:
                step_info['action'] = "OMITIR (FORMARÍA CICLO)" # Si ya están en el mismo conjunto, omitimos la arista
            
            self.steps.append(step_info)    # Agregamos la información del paso a la lista de pasos
            step_count += 1                 # Incrementamos el contador de pasos
        
        return mst    # Retornamos el árbol de expansión mínimo (o máximo) encontrado
    
    # Función para mostrar todos los pasos que hizo el algoritmo, uno por uno
    def print_step_by_step(self, max_spanning=False):
        print("\n=== SIMULADOR DE ALGORITMO DE KRUSKAL ===")
        print(f"=== {'MÁXIMO' if max_spanning else 'MÍNIMO'} COSTE ===\n")
        
        print("Grafo original:")
        print("Nodos:", self.graph['nodes'])
        print("Aristas:", self.graph['edges'])
        print("\nIniciando algoritmo...\n")
        
        self.kruskal(max_spanning)  # Ejecutamos el algoritmo de Kruskal
        
        # Mostramos cada paso guardado
        for step in self.steps:
            print(f"\n--- Paso {step['step']} ---")
            print(f"Arista considerada: {step['edge']}")
            print(f"Acción: {step['action']}")
            print("Parent:", step['parent'])    # Estado de los padres
            print("Rank:", step['rank'])        # Estado de los rangos
            print("MST actual:", step['mst'])   # Árbol de expansión actual
            time.sleep(1.5) # Simulamos un pequeño retraso para visualizar los pasos
        
        # Mostramos el resultado final
        print("\n=== RESULTADO FINAL ===")
        print("Árbol de expansión encontrado:")
        final_mst = self.steps[-1]['mst'] if self.steps else []
        total_cost = sum(edge[2] for edge in final_mst)
        for edge in final_mst:
            print(f"{edge[0]} -- {edge[1]} (peso: {edge[2]})")
        print(f"Costo total: {total_cost}")
    
     # Dibuja el grafo original usando NetworkX
    def draw_graph(self, title="Grafo Original"):
        pos = nx.spring_layout(self.G)  # Posiciones de los nodos para el grafo
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(self.G, pos, node_size=700)  # Dibujamos los nodos
        nx.draw_networkx_edges(self.G, pos, width=1.5)      # Dibujamos las aristas
        nx.draw_networkx_labels(self.G, pos, font_size=12, font_family="sans-serif")    # Etiquetas de los nodos
        edge_labels = nx.get_edge_attributes(self.G, 'weight')  # Obtenemos los pesos de las aristas
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        plt.title(title)
        plt.axis("off") # Desactivamos los ejes
        plt.show()
    
    # Dibuja el árbol de expansión resultante (MST)
    def draw_mst(self, max_spanning=False):
        mst = self.steps[-1]['mst'] if self.steps else []
        H = nx.Graph()  # Creamos un nuevo grafo para el MST
        
        # Agregamos los nodos al grafo del MST
        for node in self.graph['nodes']:
            H.add_node(node)
        
        # Agregamos las aristas del MST al grafo
        for edge in mst:
            H.add_edge(edge[0], edge[1], weight=edge[2])
        
        pos = nx.spring_layout(H)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(H, pos, node_size=700)
        nx.draw_networkx_edges(H, pos, width=1.5, edge_color='r')   # Dibujamos las aristas del MST en rojo
        nx.draw_networkx_labels(H, pos, font_size=12, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(H, 'weight')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)
        title = f"Árbol de Expansión {'Máxima' if max_spanning else 'Mínima'}"
        plt.title(title)
        plt.axis("off")
        plt.show()

# Bloque principal: esto se ejecuta si corres el archivo directamente
if __name__ == "__main__":
    simulator = KruskalSimulator()

    # Definimos los nodos del grafo
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        simulator.add_node(node)    # Agregamos los nodos al simulador

    # Definimos las aristas con sus pesos
    edges = [
        ('A', 'B', 4), ('A', 'C', 4),
        ('B', 'C', 2), ('C', 'D', 3),
        ('C', 'E', 2), ('C', 'F', 4),
        ('D', 'F', 3), ('E', 'F', 3)
    ]

    for edge in edges:
        simulator.add_edge(edge[0], edge[1], edge[2])   # Agregamos las aristas al simulador

    simulator.draw_graph()  # Dibujamos el grafo original

    print("\n" + "=" * 50)
    print("Arbol de expansion de minimo coste")
    print("=" * 50)
    simulator.print_step_by_step(max_spanning=False)    # Ejecutamos el algoritmo de Kruskal para mínimo coste
    simulator.draw_mst(max_spanning=False)              # Dibujamos el árbol de expansión mínimo

    simulator.steps = []    # Limpiamos los pasos para el siguiente cálculo

    print("\n" + "=" * 50)
    print("Arbol de expansion de maximo coste")
    print("=" * 50)
    simulator.print_step_by_step(max_spanning=True)     # Ejecutamos el algoritmo de Kruskal para máximo coste
    simulator.draw_mst(max_spanning=True)               # Dibujamos el árbol de expansión máximo