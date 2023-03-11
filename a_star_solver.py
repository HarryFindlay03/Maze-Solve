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
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


def get_neighbours(arr: List[List[str]], node: Node, visited: set[Node]) -> List[tuple]:
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbours = []

    for move in moves:
        # if possible move is already in visited don't add it to valid neighbours.
        if Node(pos=(node.pos[0] + move[0], node.pos[1] + move[1])) in visited:
            continue
        if arr[node.pos[0] + move[0]][node.pos[1] + move[1]] == "-":
            neighbours.append((node.pos[0] + move[0], node.pos[1] + move[1]))

    return neighbours


def reconstruct_path(start: Node) -> List[tuple]:
    """
    Take a set of nodes and go backwards adding all the parents to a visited list,
    until start is reached, then return the reverse of this list.

    Args:
        start (Node): The start node to reconstruct the path from, this will be the finish node
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
    yet_to_visit.put((manhattan_distance(start, goal), Node(pos=start)))
    path_length = 0
    nodes_visited = 0

    while not yet_to_visit.empty():
        # get valid neighbours of best item in the priority queue
        h, curr_node = yet_to_visit.get()
        visited.add(curr_node)
        nodes_visited += 1
        
        # get the path_length for the current node
        path_length = h - manhattan_distance(curr_node.pos, goal)

        if curr_node.pos == goal:
            return (reconstruct_path(curr_node), nodes_visited)

        neighbours = get_neighbours(arr, curr_node, visited)
        
        # if there are no valid neighbours, then get the next value from yet_to_visit
        if len(neighbours) == 0:
            continue
        
        # increase the path_length by one as we have now found the neighbours
        path_length += 1

        for neighbour in neighbours:
            yet_to_visit.put((manhattan_distance(neighbour, goal) + path_length, Node(pos=neighbour, parent=curr_node)))

    # No path found
    return (None, nodes_visited)
