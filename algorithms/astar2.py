import heapq, time

class AStarImproved:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.min_edge_weight = min(min(edges.values()) for edges in graph.values())

    def heuristic(self, node):
        return self.min_edge_weight

    def searching(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start))
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[self.start] = 0
        f_score = {node: float('inf') for node in self.graph}
        f_score[self.start] = self.heuristic(self.start)
        visited_nodes = []

        while open_list:
            time.sleep(0.0001) 
            _, current = heapq.heappop(open_list)

            if current == self.goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(self.start)
                return path[::-1], visited_nodes

            visited_nodes.append(current)

            for neighbor, cost in self.graph[current].items():
                tentative_g_score = g_score[current] + cost
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
        
        return [], visited_nodes
