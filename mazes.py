import argparse
import sys
import time

from dfs_solver import dfs
from mazes_utils import convert_to_array, find_gates, find_ordered_path, print_colors


def main():
    """
    main method in dfs_solver.py that runs the code
    """
    print("DFS MAZE SOLVER")
    print("----------------")

    # TODO: ERROR CHECKING ON COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename for maze file")
    parser.add_argument("algorithm", help="algorithm to run [dfs/a-star]")

    args = parser.parse_args()

    print(f"\n\nMaze: {args.filename}\n\n")
    arr = convert_to_array(args.filename)

    # Needed for changing the recursion limit for large mazes, this can be set to base * height!
    sys.setrecursionlimit(len(arr[0]) * len(arr))

    gates = find_gates(arr)
    start_gate, finish_gate = gates[0], gates[1]

    print(f"Start: {start_gate} . End: {finish_gate}")

    if args.algorithm == "dfs":
        path = dfs(arr, start_gate, finish_gate)

        # Path through the maze.
        ordered_path = find_ordered_path(start_gate, finish_gate, path)
        if ordered_path is not None:
            print("PATH FOUND🕺✨✨!")
        else:
            print("ERROR💤PATH NOT FOUND💤")

    elif args.algorithm == "a-star":
        print("NOT YET IMPLEMENTED 🙃")

    else:
        print("NO ALGORITHM GIVEN !")


if __name__ == "__main__":
    # Timing
    start_time = time.time()
    main()
    print("EXEC TIME: %s SECONDS" % (time.time() - start_time))
