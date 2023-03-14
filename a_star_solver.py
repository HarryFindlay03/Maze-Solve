"""
Python file for implementing A* search on supplied mazes.
"""

from queue import PriorityQueue
from typing import List
from math import sqrt

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


def euclidean(start: tuple, goal: tuple) -> int:
    """
    Straight line distance between two points calculated by d(p, q) = sqrt((q1 - p1)**2 + (q2 - p2)**2)
    """
    return sqrt((goal[0]-start[0])**2 + (goal[1]-start[1])**2)


def get_neighbours(arr: List[List[str]], node: Node, visited: set[Node]) -> List[tuple]:
    """
    Gets all valid neighbours from a node in the maze.

    Args:
        arr (List[List[str]]): 2D array which search is being performed on
        node (Node): node to find neighbours for
        visited (set[Node]): a set of nodes that have been visited

    Returns:
        List[tuple]: A list of valid neighbours
    """
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
        start (Node): The node to start reconstructing the path from

    Returns:
        List[tuple]: List of coordinates, representing the path from the start to goal node.
    """
    path = []
    curr = start

    while curr.parent is not None:
        path.append((curr.pos))
        curr = curr.parent

    path.append((curr.pos))
    return path[::-1]


def a_star(arr: List[List[str]], start: tuple, goal: tuple) -> tuple:
    """
    Function that performs A* search on given 2D array that represents the maze.

    Args:
        arr (List[List[str]]): 2D array to perform search on
        start (tuple): start node
        goal (tuple): goal node

    Returns:
        tuple: Ordered path through the maze, and number of nodes explored.
    """
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

        # path found
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

    # No path found in maze
    return (None, nodes_visited)
