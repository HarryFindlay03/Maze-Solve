from typing import List

from termcolor import colored


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


def print_colors(arr: List[List[str]], visited: List[tuple]):
    """
    Method that prints a path through the maze in green.
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            if (i, j) in visited:
                print(colored(arr[i][j], "green"), end="")
            else:
                print(arr[i][j], end="")
        print(arr[i][len(arr[i]) - 1])
