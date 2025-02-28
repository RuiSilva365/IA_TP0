import networkx as nx
import matplotlib.pyplot as plt
import time

from algorithms.astar import AStar
from algorithms.astar2 import AStarImproved
from algorithms.bidirectional import BidirectionalAStar  
from algorithms.dijkstra import Dijkstra  

def get_fixed_positions():
    return {
      'A': (1, 3),
    'B': (0, 2),
    'C': (0, 1),
    'D': (1, 0),
    'E': (2, 0),
    'F': (3, 1),
    'G': (3, 2),
    'H': (2, 2.5)
    }

def draw_graph(graph):
    G = nx.Graph()
    
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = get_fixed_positions()  
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='cyan', node_size=2000, edge_color='black', font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    selected_nodes = []


  

    def animate_search(visited_nodes, path):
        for node in visited_nodes:
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='yellow')
            plt.draw()
            time.sleep(0.5)
        
        if path:
            edges_in_path = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)
            plt.draw()
    
    def on_click(event):
        if event.xdata is None or event.ydata is None:
            return  

        clicked_node = None
        min_distance = float('inf')

        for node, (x, y) in pos.items():
            distance = (event.xdata - x) ** 2 + (event.ydata - y) ** 2
            if distance < min_distance:
                min_distance = distance
                clicked_node = node

        if clicked_node and clicked_node not in selected_nodes:
            selected_nodes.append(clicked_node)
            print(f"Nó selecionado: {clicked_node}")

            if len(selected_nodes) == 2:
                start, goal = selected_nodes
                print(f"Calculando caminhos de {start} para {goal}...")
                
                algorithms = {
                    "A*": AStar,
                    "AStarImproved": AStarImproved,
                    "Bidirectional A*": BidirectionalAStar,
                    "Dijkstra": Dijkstra
                }
                
                results = {}

                for algo_name, algo_class in algorithms.items():
                    solver = algo_class(graph, start, goal)
                    start_time = time.time()
                    path, visited_nodes = solver.searching()
                    execution_time = time.time() - start_time
                    
                    results[algo_name] = {
                        "path": path,
                        "visited_nodes": visited_nodes,
                        "execution_time": execution_time
                    }
                    
                    print(f"\n{algo_name}:")
                    print(f"  -> Caminho: {path}")
                    print(f"  -> Nós visitados: {len(visited_nodes)}")
                    print(f"  -> Tempo de execução: {execution_time:.10f} segundos")
                    
                    animate_search(visited_nodes, path)  
                    time.sleep(1)  
    
    fig.canvas.mpl_connect("button_press_event", on_click)
    plt.show()
