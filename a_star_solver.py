from queue import PriorityQueue
from typing import List

class Node:
    def __init__(self, pos: tuple, parent=None) -> None:
        self.parent = parent
        self.pos = pos

    def __hash__(self) -> int:
        return hash(self.pos)

    def __eq__(self, other) -> bool:
        return self.pos == other.pos
    
    def __lt__(self, other) -> bool:
        return self.pos < other.pos
    

def manhattan_distance(start: tuple, goal: tuple) -> int:
    """
    Manhattan distance being |x1 - x2| + |y1 - y2|
    """
    return abs(start[0]-goal[0]) + abs(start[1]-goal[1])


def get_neighbours(arr: List[List[str]], node: Node, visited: set[Node]) -> List[tuple]:
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbours = []

    for move in moves:
        # if possible move is already in visited don't add it to valid neighbours.
        if Node(pos=(node.pos[0] + move[0], node.pos[1] + move[1])) in visited:
            continue
        if arr[node.pos[0]+move[0]][node.pos[1]+move[1]] == "-":
            neighbours.append((node.pos[0] + move[0], node.pos[1] + move[1]))
    
    return neighbours


def reconstruct_path(start: Node):
    """
        Take a set of nodes and go backwards adding all the parents to a visited list,
    until start is reached, then return the reverse of this list.

    Args:
        start (Node): The start node to reconstruct the path from, this will be the finish gate
        goal (Node): The final node, one with no parent, this will be the start gate
        visited (set[Node]): The set of visited nodes.
    """
    path = []
    curr = start

    while curr.parent is not None:
        path.append((curr.pos))
        curr = curr.parent

    path.append((curr.pos))
    return path[::-1]


    


def a_star(arr: List[List[str]], start: tuple, goal: tuple):
    visited = set()

    yet_to_visit = PriorityQueue()
    yet_to_visit.put((manhattan_distance(start, goal), Node(start)))

    while not yet_to_visit.empty():
        # get valid neighbours of best item in the priority queue
        curr = yet_to_visit.get()
        visited.add(curr[1])

        if curr[1].pos == goal:
            return reconstruct_path(curr[1])
        
        neighbours = get_neighbours(arr, curr[1], visited)

        # if there are no valid neighbours, then get the next value from yet_to_visit
        if len(neighbours) == 0:
            continue

        for neighbour in neighbours:
            if neighbour not in visited:
                yet_to_visit.put((manhattan_distance(neighbour, goal), Node(pos=neighbour, parent=curr[1])))










    
