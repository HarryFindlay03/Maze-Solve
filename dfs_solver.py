"""
Python file for depth first search on supplied mazes for ECM2423 coursework.
"""

from typing import List


def dfs(arr: List[List[str]], start: tuple, goal: tuple, nodes_explored=0, visited=set(), path=[]) -> tuple:
    """
    Function that performs a depth-first search on an inputted 2D array representing a maze.

    Args:
        arr (List[List[str]]): 2D array to perform search on
        start (tuple): start node
        goal (tuple): goal node
        nodes_explored (int, optional): number of nodes explored. Defaults to 0.
        visited (set(), optional): visited set. Defaults to set().
        path (list, optional): path stack. Defaults to [].

    Returns:
        tuple: The ordered path from the start node to the goal node,
        and the number of nodes explored to compute this path
    """
    # possible moves: [DOWN, RIGHT, LEFT, UP]
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    # possible moves: [UP, LEFT, DOWN, RIGHT]
    # moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # visited set, storing current visited nodes, utilising O(1) lookup
    visited.add(start)

    # path stack, storing current ordered path
    path.append(start)

    nodes_explored += 1

    # base case
    if start == goal:
        return (True, nodes_explored)

    # leaf node
    if arr[start[0]][start[1]] == "#" or start[0] < 0:
        return (False, nodes_explored)

    # finding neighbours
    neighbours = []
    for move in moves:
        neighbours.append((start[0] + move[0], start[1] + move[1]))

    for neighbour in neighbours:
        if neighbour not in visited:
            found, nodes_explored = dfs(arr, neighbour, goal, nodes_explored, visited, path)
            if found:
                # found goal state on path
                return (path, nodes_explored)
            else:
                # hit a leaf node
                path.pop()
                visited.remove(neighbour)

    # No path found
    return (None, nodes_explored)
