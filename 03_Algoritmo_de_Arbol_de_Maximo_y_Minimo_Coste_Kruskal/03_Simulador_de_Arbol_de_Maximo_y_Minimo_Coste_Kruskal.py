import matplotlib.pyplot as plt
import networkx as nx
import time

class KruskalSimulator:
    def __init__(self):
        self.graph = {
            'nodes': [],
            'edges': []
        }
        self.steps = []
        self.G = nx.Graph()
    
    def add_node(self, node):
        if node not in self.graph['nodes']:
            self.graph['nodes'].append(node)
            self.G.add_node(node)
    
    def add_edge(self, node1, node2, weight):
        self.graph['edges'].append((node1, node2, weight))
        self.G.add_edge(node1, node2, weight=weight)
    
    def find_parent(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])
    
    def kruskal(self, max_spanning=False):
        edges = sorted(self.graph['edges'], key=lambda item: item[2], reverse=max_spanning)
        parent = {}
        rank = {}
        
        for node in self.graph['nodes']:
            parent[node] = node
            rank[node] = 0
        
        mst = []
        step_count = 1
        
        for edge in edges:
            node1, node2, weight = edge
            root1 = self.find_parent(parent, node1)
            root2 = self.find_parent(parent, node2)
            
            step_info = {
                'step': step_count,
                'edge': edge,
                'action': None,
                'mst': mst.copy(),
                'parent': parent.copy(),
                'rank': rank.copy()
            }
            
            if root1 != root2:
                mst.append(edge)
                step_info['action'] = "AGREGAR"
                
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
            else:
                step_info['action'] = "OMITIR (FORMARÍA CICLO)"
            
            self.steps.append(step_info)
            step_count += 1
        
        return mst
    
    def print_step_by_step(self, max_spanning=False):
        print("\n=== SIMULADOR DE ALGORITMO DE KRUSKAL ===")
        print(f"=== {'MÁXIMO' if max_spanning else 'MÍNIMO'} COSTE ===\n")
        
        print("Grafo original:")
        print("Nodos:", self.graph['nodes'])
        print("Aristas:", self.graph['edges'])
        print("\nIniciando algoritmo...\n")
        
        self.kruskal(max_spanning)
        
        for step in self.steps:
            print(f"\n--- Paso {step['step']} ---")
            print(f"Arista considerada: {step['edge']}")
            print(f"Acción: {step['action']}")
            print("Parent:", step['parent'])
            print("Rank:", step['rank'])
            print("MST actual:", step['mst'])
            time.sleep(1.5)
        
        print("\n=== RESULTADO FINAL ===")
        print("Árbol de expansión encontrado:")
        final_mst = self.steps[-1]['mst'] if self.steps else []
        total_cost = sum(edge[2] for edge in final_mst)
        for edge in final_mst:
            print(f"{edge[0]} -- {edge[1]} (peso: {edge[2]})")
        print(f"Costo total: {total_cost}")
    
    def draw_graph(self, title="Grafo Original"):
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(self.G, pos, node_size=700)
        nx.draw_networkx_edges(self.G, pos, width=1.5)
        nx.draw_networkx_labels(self.G, pos, font_size=12, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)
        plt.title(title)
        plt.axis("off")
        plt.show()
    
    def draw_mst(self, max_spanning=False):
        mst = self.steps[-1]['mst'] if self.steps else []
        H = nx.Graph()
        
        for node in self.graph['nodes']:
            H.add_node(node)
        
        for edge in mst:
            H.add_edge(edge[0], edge[1], weight=edge[2])
        
        pos = nx.spring_layout(H)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(H, pos, node_size=700)
        nx.draw_networkx_edges(H, pos, width=1.5, edge_color='r')
        nx.draw_networkx_labels(H, pos, font_size=12, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(H, 'weight')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels)
        title = f"Árbol de Expansión {'Máxima' if max_spanning else 'Mínima'}"
        plt.title(title)
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    simulator = KruskalSimulator()

    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        simulator.add_node(node)

    edges = [
        ('A', 'B', 4), ('A', 'C', 4),
        ('B', 'C', 2), ('C', 'D', 3),
        ('C', 'E', 2), ('C', 'F', 4),
        ('D', 'F', 3), ('E', 'F', 3)
    ]

    for edge in edges:
        simulator.add_edge(edge[0], edge[1], edge[2])

    simulator.draw_graph()

    print("\n" + "=" * 50)
    print("Arbol de expansion de minimo coste")
    print("=" * 50)
    simulator.print_step_by_step(max_spanning=False)
    simulator.draw_mst(max_spanning=False)

    simulator.steps = []

    print("\n" + "=" * 50)
    print("Arbol de expansion de maximo coste")
    print("=" * 50)
    simulator.print_step_by_step(max_spanning=True)
    simulator.draw_mst(max_spanning=True)