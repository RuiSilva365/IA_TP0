import heapq
from metrics import measure_performance


class Dijkstra:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def searching(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[self.start] = 0
        visited_nodes = []

        while open_list:
            cost, current = heapq.heappop(open_list)
            
            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1], visited_nodes

            visited_nodes.append(current)
            
            for neighbor, weight in self.graph[current].items():
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_list, (tentative_g_score, neighbor))
        
        return [], visited_nodes
