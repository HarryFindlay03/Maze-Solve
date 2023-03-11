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
    parser.add_argument("--output", action=argparse.BooleanOptionalAction, help="pretty maze output")

    args = parser.parse_args()

    print(f"\n\nMaze: {args.filename}")
    print(f"Algorithm: {args.algorithm}\n\n")
    arr = convert_to_array(args.filename)

    # Needed for changing the recursion limit for large mazes, this can be set to base * height!
    sys.setrecursionlimit(len(arr[0]) * len(arr))

    gates = find_gates(arr)

    # if there are no valid start or end gates, break.
    if len(gates) < 2:
        print("NO VALID START OR END GATES FOUND🤔")
        print("MAZE SOLVING NOT POSSIBLE 😡😡")
        return
    
    start_gate, finish_gate = gates[0], gates[1]

    print(f"Start: {start_gate} . End: {finish_gate}")

    if args.algorithm == "dfs":
        start_time = time.time()
        path, nodes_explored = dfs(arr, start_gate, finish_gate, nodes_explored=0)
        exec_time = time.time() - start_time

        
        if path is not None:
            # Ordered path through the maze.
            ordered_path = find_ordered_path(start_gate, finish_gate, path)
            print("PATH FOUND🕺✨✨!")
            print("NODES EXPLORED: ", nodes_explored)
            print("PATH LENGTH: ", len(ordered_path))
            print("TIME TAKEN: %s SECONDS" % exec_time)
            
            # Print coloured route through maze on --output flag.
            if args.output:
                print("\n\n=============")
                print("PRETTY OUTPUT")
                print("=============\n\n")
                print_colors(arr, ordered_path)
                print("\n\n")
        else:
            print("ERROR💤PATH NOT FOUND💤")

    elif args.algorithm == "a-star":
        start_time = time.time()
        path, nodes_explored = a_star(arr, start_gate, finish_gate)
        exec_time = time.time() - start_time

        if path is not None:
            print("PATH FOUND🕺✨✨!")
            print("NODES EXPLORED: ", nodes_explored)
            print("PATH LENGTH: ", len(path))
            print("TIME TAKEN: %s SECONDS" % exec_time)

            if args.output:
                print("\n\n=============")
                print("PRETTY OUTPUT")
                print("=============\n\n")
                print_colors(arr, path)
                print("\n\n")
        else:
            print("ERROR💤PATH NOT FOUND💤")

    else:
        print("CHOSEN ALGORITHM IS NOT CORRECT !")


if __name__ == "__main__":
    # Running main function
    main()
