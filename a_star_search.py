from heapq import heappush, heappop
from typing import Dict, Tuple, List, Optional


G: Dict[str, Dict[str, int]] = {
    "S": {"B": 9,  "F": 13, "A": 43, "E": 20},
    "F": {"A": 13, "B": 27},
    "B": {"C": 15, "G": 12},
    "A": {"G": 23, "E": 14},
    "C": {"G": 4,  "Z": 34},
    "G": {"D": 7,  "Z": 25},
    "E": {"D": 14},
    "D": {"Z": 15},
    "Z": {},
}


def h(n: str) -> float:
    return 0.0 # Dijkstra

# h
# H = {"S": 35, "B": 28, "F": 32, "A": 40, "E": 22, "C": 20, "G": 18, "D": 12, "Z": 0}
# def h(n: str) -> float: return H[n]

# -------- A* nach Professor-Folie --------
def a_star(
    graph: Dict[str, Dict[str, int]],
    start: str,
    goal: str,
) -> Tuple[Optional[List[str]], Optional[float]]:
    """
    Open: Min-Heap nach f = g + h
    Closed: 
    g(N): 
    Re-Open: 
    """
    INF = 10**18
    g: Dict[str, float] = {n: INF for n in graph}
    parent: Dict[str, Optional[str]] = {start: None}
    g[start] = 0.0

    
    open_heap: List[Tuple[float, float, str]] = []
    heappush(open_heap, (h(start), 0.0, start))
    best_in_open: Dict[str, float] = {start: 0.0}   

    closed = set()

    while open_heap:
        f_cur, g_cur, u = heappop(open_heap)

        
        if best_in_open.get(u, None) is None or g_cur != best_in_open[u]:
            continue
        
        best_in_open.pop(u, None)

    
        if u == goal:
            
            path = []
            x = u
            while x is not None:
                path.append(x)
                x = parent[x]
            return path[::-1], g_cur

        
        closed.add(u)

     
        for v, w in graph[u].items():
            cand_g = g[u] + w

         
            if (v in best_in_open or v in closed) and cand_g >= g.get(v, INF):
                continue

        
            g[v] = cand_g
            parent[v] = u

           
            if v in closed:
                closed.remove(v)

            f_v = cand_g + h(v)
            heappush(open_heap, (f_v, cand_g, v))
            best_in_open[v] = cand_g

    
    return None, None



if __name__ == "__main__":
    path, cost = a_star(G, "S", "Z")
    print("Pfad:", path)
    print("Kosten:", cost, "km")
