from typing import Callable, Hashable, Iterable, List, Optional, Tuple

Node = Hashable

def hill_climb(
    start: Node,
    is_goal: Callable[[Node], bool],
    neighbors: Callable[[Node], Iterable[Node]],
    h: Callable[[Node], float],
) -> Optional[List[Node]]:
   
    visited = set()
    L: List[Tuple[Node, List[Node]]] = [(start, [])]
    
    L.sort(key=lambda kp: h(kp[0]), reverse=True)

    while L:
        (k, path), R = L[0], L[1:]
        if is_goal(k):
            return path + [k]
        if k in visited:
            L = R
            continue
        visited.add(k)

        
        kids = []
        for nb in neighbors(k):
            if nb not in visited:
                kids.append((nb, path + [k]))

       
        kids.sort(key=lambda kp: h(kp[0]), reverse=True)

        
        L = kids + R

    return None


# =============== 

from math import inf

W, H = 5, 5
start = (0, 0)
goal  = (4, 4)
walls = {(1,1), (1,2), (3,1), (3,2), (2,3)}  

def in_bounds(x, y): return 0 <= x < W and 0 <= y < H
def passable(x, y): return (x, y) not in walls

def grid_neighbors(p):
    x, y = p
    nxt = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]  
    return [q for q in nxt if in_bounds(*q) and passable(*q)]

def is_goal(p): return p == goal

def manhattan(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])


def h(p): return -manhattan(p, goal)

path = hill_climb(start, is_goal, grid_neighbors, h)
print("Gefundener Pfad:", path)
