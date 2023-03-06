from queue import PriorityQueue
from typing import List

def manhattan_distance(start: tuple, goal: tuple) -> int:
    """
    Manhattan distance being |x1 - x2| + |y1 - y2|
    """
    return abs(start[0]-goal[0]) + abs(start[1]-goal[1])


def get_neighbours(arr: List[List[str]], node: tuple, visited: set()) -> List[tuple]:
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    neighbours = []

    for move in moves:
        # if possible move is already in visited don't add it to valid neighbours.
        if (node[0] + move[0], node[1] + move[1]) in visited:
            continue
        if arr[node[0]+move[0]][node[1]+move[1]] == "-":
            neighbours.append((node[0] + move[0], node[1] + move[1]))
    
    return neighbours


def reconstruct_path(arr: List[List[str]], start: tuple, goal: tuple):
    pass


def a_star(arr: List[List[str]], start: tuple, goal: tuple):
    visited = set()

    yet_to_visit = PriorityQueue()
    yet_to_visit.put((manhattan_distance(start, goal), start))

    while not yet_to_visit.empty():
        # get valid neighbours of the best item in the priority queue
        curr = yet_to_visit.get()
        visited.add(curr[1])

        if curr[1] == goal:
            return visited
        
        neighbours = get_neighbours(arr, curr[1], visited)

        # if there are no valid neighbours get the next value from yet_to_visit
        if len(neighbours) == 0:
            continue
         
        for neighbour in neighbours:
            if neighbour not in visited:
                yet_to_visit.put((manhattan_distance(neighbour, goal), neighbour))








    
