from heapq import heappush, heappop
from typing import Callable, Hashable, Iterable, Optional, Dict, List, Tuple

Node = Hashable

def best_first_search(
    start: Node,
    is_goal: Callable[[Node], bool],
    neighbors: Callable[[Node], Iterable[Node]],
    h: Callable[[Node], float],
    maximize: bool = True,  
) -> Optional[List[Node]]:
    
    def priority(n: Node) -> Tuple[float, int]:
        nonlocal _tie
        _tie += 1
        return ((-h(n) if maximize else h(n)), _tie)  

    open_heap: List[Tuple[float, int, Node]] = []
    _tie = 0
    heappush(open_heap, (*priority(start), start))

    parent: Dict[Node, Optional[Node]] = {start: None}
    visited = set()

    while open_heap:
        _, _, v = heappop(open_heap)
        if v in visited:
            continue
        visited.add(v)

        if is_goal(v):
            
            path: List[Node] = []
            cur: Optional[Node] = v
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return list(reversed(path))

        for nb in neighbors(v):
            if nb in visited:
                continue
            if nb not in parent:        
                parent[nb] = v
            heappush(open_heap, (*priority(nb), nb))

    return None



H = {"A":4, "B":7, "C":8, "D":9, "E":8, "F":4, "G":5, "H":9, "I":4, "J":5, "K":2, "L":10}
edges = {
    "A": ["B","C"],
    "B": ["D","E"], "C": ["F","G"],
    "D": ["H"],     "F": ["I","J"], "G": ["K"],
    "H": ["L"],     "E": [], "I": [], "J": [], "K": [], "L": []
}
def neighbors(u): return edges.get(u, [])
def is_goal(u):   return u == "L"
def h(u):         return H[u]

path = best_first_search("A", is_goal, neighbors, h, maximize=True)
print(path)  
