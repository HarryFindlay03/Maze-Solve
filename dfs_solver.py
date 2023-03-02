"""
Python file for depth first search on supplied mazes for ECM2423 coursework.
"""

import sys
import time
import argparse
from termcolor import colored
from typing import List


def print_2d_array(arr: List[List[str]]) -> None:
    """
    Outputs the 2D array to the terminal

    Args:
        arr (List[str]): _description_
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            print(arr[i][j], end="")
        print(arr[i][len(arr[i]) - 1])


def convert_to_array(filename: str) -> List[List[str]]:
    """
    Converts the inputted filename, for this case will be any of the mazes into 2D array

    Args:
        fn (str): filename.txt for inputted maze

    Returns:
        List[str]: The maze in a 2D array format.
    """

    with open(filename, "r") as mazefile:
        # Stripping newlines from each line in the file
        data = [x.rstrip("\n") for x in mazefile.readlines() if x.strip() != ""]

        # Removing spaces from the data
        data = [x.replace(" ", "") for x in data]

        # Declaring and placing data into 2D array to be returned
        height, width = len(data), len(data[0])
        return_arr = [["" for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                return_arr[i][j] = data[i][j]

        return return_arr


def find_gates(arr: List[List[str]]) -> List[tuple]:
    """
    Returns the coordinates of the start gate and the exit gate in the maze.

    Args:
        arr (List[str]): The inputted 2D array to find the start and exit gate for.

    Returns:
        List(tuple): A list containing two tuples, the first containing the x, y coords of the entrance,
        and the second value containing the x, y coords of the exit.
    """
    res = []
    # Find the start gate
    for i in range(len(arr[0])):
        if arr[0][i] == "-":
            res.append((0, i))

    # Find the exit gate
    # Final row in the maze
    n = len(arr) - 1
    for j in range(len(arr[n])):
        if arr[n][j] == "-":
            res.append((n, j))

    return res


def dfs(arr: List[List[str]], start: tuple, goal: tuple, visited=set()):
    # possible moves
    moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    visited.add(start)

    # base case
    if start == goal:
        return True

    # leaf node
    if arr[start[0]][start[1]] != "-" or start[0] < 0:
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


def print_colors(arr: List[List[str]], visited: List[tuple]):
    """
    Method that prints a path through the maze in a colour of your choosing.
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            if (i, j) in visited:
                print(colored(arr[i][j], "green"), end="")
            else:
                print(arr[i][j], end="")
        print(arr[i][len(arr[i]) - 1])


def find_ordered_path(start: tuple, goal: tuple, path: set(), visited=[]):
    """
    Takes a path and finds the route through the maze from start to end.
    """
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited.append(start)

    if start == goal:
        return True

    neighbours = []
    for move in moves:
        neighbours.append((start[0] + move[0], start[1] + move[1]))

    for neighbour in neighbours:
        if neighbour not in visited:
            if neighbour in path:
                if find_ordered_path(neighbour, goal, path, visited):
                    return visited


def main():
    """
    main method in dfs_solver.py that runs the code
    """
    print("DFS MAZE SOLVER")
    print("----------------")

    # TODO: ERROR CHECKING ON COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename for maze file")

    args = parser.parse_args()

    print(f"\n\nMaze: {args.filename}\n\n")
    arr = convert_to_array(args.filename)

    # Needed for changing the recursion limit for large mazes, this can be set to base * height!
    sys.setrecursionlimit(len(arr[0]) * len(arr[1]))

    gates = find_gates(arr)
    start_gate, finish_gate = gates[0], gates[1]

    print(f"Start: {start_gate} . End: {finish_gate}")
    path = dfs(arr, start_gate, finish_gate)

    # Path through the maze.
    ordered_path = find_ordered_path(start_gate, finish_gate, path)
    if ordered_path is not None:
        print("PATH FOUND🕺✨✨!")
    else:
        print("ERROR💤PATH NOT FOUND💤")


if __name__ == "__main__":
    # Timing
    start_time = time.time()
    main()
    print("EXEC TIME: %s SECONDS" % (time.time() - start_time))
