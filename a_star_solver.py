from typing import List

def manhattan_distance(start: tuple, goal: tuple) -> int:
    """
    Manhattan distance being |x1 - x2| + |y1 - y2|
    """
    return abs(start[0]-start[1]) + abs(goal[0]-goal[1])

def a_star(arr: List[List[str]], start: tuple, goal: tuple, visited=[]) -> List[tuple] | bool | None:
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    visited.append(start)

    # base case
    if start == goal:
       return True

    # leaf node
    if arr[start[0]][start[1]] == "#" or start[0] < 0:
        return False
    
    neighbours = []
    for move in moves:
        neighbours.append((start[0] + move[0], start[1] + move[1]))

    smallest = 1000000 #infty
    smallest_loc = -1
    for i in range(0, 4):
        if neighbours[i] in visited:
            continue
        if arr[neighbours[i][0]][neighbours[i][1]] == "#":
            continue

        temp = manhattan_distance(neighbours[i], goal)
        if temp < smallest:
            smallest = temp
            smallest_loc = i

    if smallest_loc == -1:
        # Keep popping until path is not on visited
        pass


    print(neighbours[smallest_loc])

    if a_star(arr, neighbours[smallest_loc], goal, visited):
        return visited

    
