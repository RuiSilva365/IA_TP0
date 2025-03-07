import time
from algorithms.astar import AStar  # Importa a classe do A*
from algorithms.dijkstra import Dijkstra  # Importa a classe do Dijkstra

def measure_performance(search_function, runs=1000):
    def wrapper(*args, **kwargs):
        total_time = 0
        for _ in range(runs):
            start_time = time.perf_counter_ns()
            path, visited_nodes = search_function(*args, **kwargs)
            end_time = time.perf_counter_ns()
            total_time += (end_time - start_time)

        avg_time = (total_time / runs) / 1e9  # Média em segundos
        return {
            "path": path,
            "visited_nodes": visited_nodes,
            "execution_time": avg_time
        }
    return wrapper


def run_astar(graph, start, goal):
    """Executa A* e mede o desempenho"""
    astar = AStar(graph, start, goal)
    return measure_performance(astar.searching)()

def run_dijkstra(graph, start, goal):
    """Executa Dijkstra e mede o desempenho"""
    dijkstra = Dijkstra(graph, start, goal)
    return measure_performance(dijkstra.searching)()
