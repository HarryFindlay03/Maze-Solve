import argparse
import sys
import time

from a_star_solver import a_star
from dfs_solver import dfs
from mazes_utils import (convert_to_array, find_gates, find_ordered_path,
                         print_2d_array, print_colors)


def main():
    """
    main method in dfs_solver.py that runs the code
    """
    print("MAZE SOLVER")
    print("----------------")

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename for maze file")
    parser.add_argument("algorithm", help="algorithm to run [dfs/a-star]")
    parser.add_argument("--output", action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    print(f"\n\nMaze: {args.filename}")
    print(f"Algorithm: {args.algorithm}\n\n")
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
            print("PATH LENGTH: ", len(ordered_path))
            
            # Print coloured route through maze on --output flag.
            if args.output:
                print_colors(arr, ordered_path)
        else:
            print("ERROR💤PATH NOT FOUND💤")

    elif args.algorithm == "a-star":
        path = a_star(arr, start_gate, finish_gate)

        if path[0] is not None:
            print("PATH FOUND🕺✨✨!")
            print("NODES VISITED: ", path[1])
            print("PATH LENGTH: ", len(path[0]))

            if args.output:
                print_colors(arr, path[0])
        else:
            print("ERROR💤PATH NOT FOUND💤")

    else:
        print("CHOSEN ALGORITHM IS NOT CORRECT !")


if __name__ == "__main__":
    # Timing
    start_time = time.time()
    main()
    print("EXEC TIME: %s SECONDS" % (time.time() - start_time))
