import heapq, time

class AStar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.min_edge_weight = min(min(edges.values()) for edges in graph.values())  # Smaller weight of the graph

    def heuristic(self, node):
        """ Average distance in the smaller weight of the edge possible  """
        return self.min_edge_weight * self.estimate_remaining_steps(node)

    def estimate_remaining_steps(self, node):
        return 1  

    def searching(self):
        """ A* implementation for graphs based in adjacent lists """
        open_list = []
        heapq.heappush(open_list, (0, self.start))  # (estimated_cost, node)

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
        
        return [], visited_nodes  # Return empty if doesn't find path
