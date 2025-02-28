import heapq
from metrics import measure_performance


class BidirectionalAStar:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.min_edge_weight = min(min(edges.values()) for edges in graph.values())

    def heuristic(self, node):
        return self.min_edge_weight

    def searching(self):
        forward_open = []
        backward_open = []
        heapq.heappush(forward_open, (0, self.start))
        heapq.heappush(backward_open, (0, self.goal))
        
        forward_came_from = {}
        backward_came_from = {}
        
        forward_g = {node: float('inf') for node in self.graph}
        backward_g = {node: float('inf') for node in self.graph}
        
        forward_g[self.start] = 0
        backward_g[self.goal] = 0
        
        forward_visited = []
        backward_visited = []
        
        while forward_open and backward_open:
            _, forward_current = heapq.heappop(forward_open)
            _, backward_current = heapq.heappop(backward_open)
            
            if forward_current in backward_visited or backward_current in forward_visited:
                return self.reconstruct_path(forward_came_from, backward_came_from, forward_current), forward_visited + backward_visited
            
            forward_visited.append(forward_current)
            backward_visited.append(backward_current)
            
            for neighbor, cost in self.graph[forward_current].items():
                tentative_g = forward_g[forward_current] + cost
                if tentative_g < forward_g[neighbor]:
                    forward_came_from[neighbor] = forward_current
                    forward_g[neighbor] = tentative_g
                    heapq.heappush(forward_open, (tentative_g + self.heuristic(neighbor), neighbor))
            
            for neighbor, cost in self.graph[backward_current].items():
                tentative_g = backward_g[backward_current] + cost
                if tentative_g < backward_g[neighbor]:
                    backward_came_from[neighbor] = backward_current
                    backward_g[neighbor] = tentative_g
                    heapq.heappush(backward_open, (tentative_g + self.heuristic(neighbor), neighbor))
        
        return [], forward_visited + backward_visited
    
    def reconstruct_path(self, forward_came_from, backward_came_from, meeting_point):
        path = []
        current = meeting_point
        while current in forward_came_from:
            path.append(current)
            current = forward_came_from[current]
        path.append(self.start)
        path.reverse()
        
        current = meeting_point
        while current in backward_came_from:
            path.append(current)
            current = backward_came_from[current]
        path.append(self.goal)
        
        return path
