"""
Python file for depth first search on supplied mazes for ECM2423 coursework.
"""

import argparse
from typing import List


def print_2d_array(arr: List[str]) -> None:
    """
    Outputs the 2D array to the terminal

    Args:
        arr (List[str]): _description_
    """
    for i in range(len(arr)):
        for j in range(len(arr[0]) - 1):
            print(arr[i][j], end="")
        print(arr[i][j])


def convert_to_array(filename: str) -> List[str]:
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

    print(f"Maze: {args.filename}\n\n")
    arr = convert_to_array(args.filename)
    print_2d_array(arr)
    print("\n\n")

#TODO: Why should I have this statement ?
if __name__ == "__main__":
    main()
