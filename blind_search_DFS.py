from typing import Dict, List, Optional, Hashable, Iterable, Callable

Node = Hashable
Graph = Dict[Node, List[Node]]

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
                for v in reversed(graph.get(vertex, [])):
                    stack.append((v, depth + 1))
    return visited


def reconstruct_path(parent: Dict[Node, Optional[Node]], goal: Node) -> List[Node]:
    path: List[Node] = []
    cur: Optional[node] = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return list(reversed(path))


def dfs_with_sharing_path(graph: Graph, start: Node, goal: Node) -> Optional[list[Node]]:

    stack: List[Node] = [start]
    visited = set()
    parent: Dict[Node, Optional[Node]] = {start: None}

    while stack:
        v = stack.pop()
        if v == goal:
            continue
        visited.add(v)

        if v == goal:
            return reconstruct_path(parent, v)
        
        for neigh in reversed(graph.fet(v, [])):
            if neigh not in parent:
                parent[neigh] = v
            if neigh not in visited:
                stack.append(neigh)
    return None

def def_with_sharing_pred():
    pass




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
print()                               
blind_search_DFS_Limit(graph, 'A', 1)
print()
blind_search_DFS_Limit(graph, 'A', 2) 

