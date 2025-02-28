#graph definition
def get_graph():
    return {
        'A': {'B': 5, 'F': 3},
        'B': {'A': 5, 'C': 2, 'G': 3},
        'C': {'B': 2, 'D': 6, 'H': 10},
        'D': {'C': 6, 'E': 3},
        'E': {'D': 3, 'F': 8, 'H': 5},
        'F': {'E': 8, 'G': 7, 'A':3},
        'G': { 'B': 3, 'F': 7, 'H': 2},
        'H': { 'C': 10, 'E': 5, 'G': 2}
    }


graph = get_graph()
print(graph)
