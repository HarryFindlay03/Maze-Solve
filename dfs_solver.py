"""
Python file for depth first search on supplied mazes for ECM2423 coursework.
"""
from typing import List


def dfs(arr: List[List[str]], start: tuple, goal: tuple, visited=set()):
    # possible moves
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    visited.add(start)

    # base case
    if start == goal:
        return True

    # leaf node
    if arr[start[0]][start[1]] == "#" or start[0] < 0:
        return False

    neighbours = []
    for move in moves:
        neighbours.append((start[0] + move[0], start[1] + move[1]))

    for neighbour in neighbours:
        if neighbour not in visited:
            if dfs(arr, neighbour, goal, visited):
                return visited
            else:
                visited.remove(neighbour)
