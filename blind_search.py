"""
Blind search is uninformed search; only the search graph is (implicitly) given, and there is no other information such as heuristics.
Input:
Set of initial nodes
Set of target nodes or unique definition of the properties of the target nodes
Successor function N
Output:
Path to the target node, if it exists
"""
import random
from typing import Callable, Dict, Hashable, List, Iterable, Optional, Tuple

Node = Hashable

def random_blind_search(
        start: Node,
        is_goal: Callable[[Node], bool],
        neighbors: Callable[[Node], Iterable[Node]],
        seed: Optional[int] = None,
        max_expansions: Optional[int] = None,
    ) -> Optional[list[Node]]:

    rng = random.Random(seed)
    L: List[Node] = [start]
    parent: Dict[Node, Optional[Node]] = {start: None}
    visited = set([start])

    expansion = 0
    while L:
        if max_expansions is not None and expansion >= max_expansions:

            return None
        
        index = rng.randrange(len(L))
        K = L.pop(index)
        if is_goal(K):
            path = []
            cur : Optional[Node] = K
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return list(reversed(path))
        for neigh in neighbors(K):
            if neigh not in visited and neigh not in L:
                visited.add(neigh)
                parent[neigh] = K
                L.append(neigh)
        expansion += 1
    return None


graph = {
    "S": ["A", "B"],
    "A": ["C", "D"],
    "B": ["E", "F"],
    "C": [],
    "D": ["G"],
    "E": [],
    "F": ["H"],
    "G": ["Z"],   
    "H": [],
    "Z": []
}

def neighbors(n):
    return graph.get(n, [])

def is_goal(n):
    return n == "Z"

path = random_blind_search("S", is_goal, neighbors, seed=42)

print("path found:", path)


    



    
