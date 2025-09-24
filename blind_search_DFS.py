
def blind_search_DFS(graph, start):
    visited = set()   # creat a set to store visited nodes 
    stack = [start]    # craet a stack for DFs traversal and add the starting node
    while stack:
        vertex = stack.pop() # pop a node from the stack
        if vertex not in visited:
            visited.add(vertex) # mark the current vertex as visited
            print(vertex, end='') # print the vertex 
            #add all adjacent vertices of the current vertex to the stack 
            stack.extend(reversed(graph[vertex]))
    return visited


def blind_search_DFS_Limit(graph, start, depth_limit):
    visited = set()
    stack = [(start, 0)] # stack of tuples (node, depth)
    while stack:
        vertex, depth = stack.pop()
        if depth < depth_limit:
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=' ')
                for v in reversed(graph[vertex]):
                    stack.append([(v, depth + 1)])
    return visited




# Example usage:
graph = {
  'A': ['B','C'],
  'B': ['D'],
  'C': ['E','F'],
  'D': [],
  'E': [],
  'F': []
}
blind_search_DFS(graph, 'A')

