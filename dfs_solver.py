"""
Python file for depth first search on supplied mazes for ECM2423 coursework.
"""
from typing import List


def dfs(arr: List[List[str]], start: tuple, goal: tuple, nodes_explored=0, visited=set(), path=[]):
    # possible moves
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    visited.add(start)
    path.append(start)
    nodes_explored += 1

    # base case
    if start == goal:
        return (True, nodes_explored)

    # leaf node
    if arr[start[0]][start[1]] == "#" or start[0] < 0:
        return (False, nodes_explored)

    neighbours = []
    for move in moves:
        neighbours.append((start[0] + move[0], start[1] + move[1]))

    for neighbour in neighbours:
        if neighbour not in visited:
            found, nodes_explored = dfs(arr, neighbour, goal, nodes_explored, visited, path)
            if found:
                return (path, nodes_explored)
            else:
                path.pop()
                visited.remove(neighbour)

    # No path found through the maze
    return (None, nodes_explored)
