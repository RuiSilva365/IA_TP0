import time

def measure_performance(search_function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        path, visited_nodes = search_function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        return {
            "path": path,
            "visited_nodes": visited_nodes,
            "execution_time": execution_time
        }
    return wrapper
