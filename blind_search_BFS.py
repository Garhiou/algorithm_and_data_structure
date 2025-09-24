
def blind_search_BFS(graph, start):
    visited = set()   # create a set to store visited nodes 
    queue = [start]   # create a queue for BSF traversal and add the starting node 
    front = 0         # initialize the front of the queue 
    while front < len(queue):
        vertex = queue[front] # get the first item from the queue 
        front += 1
        if vertex not in visited:
            visited.add(vertex)  # mark the current vertex as visited 
            print(vertex, end=' ') # print the vertex
            # add all adjacent vertcies of the current vertex to the queue 
            queue.extend(graph.get(vertex, []))
    return visited


# Example usage
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = blind_search_BFS(graph, 'A')  
print("\nvisited:", visited)