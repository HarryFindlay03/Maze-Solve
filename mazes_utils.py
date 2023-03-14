"""
Helper functions and methods to aid in search algorithm
"""

from typing import List

from termcolor import colored


def print_2d_array(arr: List[List[str]]) -> None:
    """
    Outputs the 2D array to the terminal

    Args:
        arr (List[List[str]]): 2D array to output
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            print(arr[i][j], end="")
        print(arr[i][len(arr[i]) - 1])


def convert_to_array(filename: str) -> List[List[str]]:
    """
    Converts the inputted file, being any of the mazes-*.txt, into a 2D array.

    Args:
        filename (str): filename.txt to convert

    Returns:
        List[List[str]]: 2D array representing maze file
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
    Returns the coordinates of the start node and the exit node.

    Args:
        arr (List[List[str]]): 2D array to find start and goal node for

    Returns:
        List(tuple): A list containing two tuples, the 0th index containing the x, y coords of the start,
        and the 1st index containing the x, y coords of the goal.
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


def print_colors(arr: List[List[str]], visited: List[tuple]):
    """
    Method that outputs the maze, with a highlighted path through it.

    Args:
        arr (List[List[str]]): 2D array to output
        visited (List[tuple]): Path through the maze
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            if (i, j) in visited:
                print(colored(arr[i][j], "green"), end="")
            else:
                print(arr[i][j], end="")
        print(arr[i][len(arr[i]) - 1])
