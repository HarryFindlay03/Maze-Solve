import argparse
import sys
import time

from a_star_solver import a_star
from dfs_solver import dfs, find_ordered_path
from mazes_utils import convert_to_array, find_gates, print_2d_array, print_colors


def main():
    """
    main method in dfs_solver.py that runs the code
    """
    print("===========")
    print("MAZE SOLVER")
    print("===========")

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="filename for maze file")
    parser.add_argument("algorithm", help="algorithm to run [dfs/a-star]")
    parser.add_argument("--path", action=argparse.BooleanOptionalAction, help="output path from start to goal")
    parser.add_argument("--stats", action=argparse.BooleanOptionalAction, help="output statistics about the maze")
    parser.add_argument("--prettyoutput", action=argparse.BooleanOptionalAction, help="pretty maze output")

    args = parser.parse_args()

    print(f"\n\nMaze: {args.filename}")
    print(f"Algorithm: {args.algorithm}\n\n")
    arr = convert_to_array(args.filename)

    # Needed for changing the recursion limit for large mazes, this can be set to base * height!
    sys.setrecursionlimit(len(arr[0]) * len(arr))

    gates = find_gates(arr)

    # if there are no valid start or end gates, break.
    if len(gates) != 2:
        if len(gates) > 2:
            print("MULTIPLE START OR END GATES FOUND, DISTINCT START AND END GATES ARE REQUIRED")
        else:
            print("NO VALID START OR END GATES FOUND🤔")

        print("\nMAZE SOLVING NOT POSSIBLE 😡😡")
        return
    
    start_gate, finish_gate = gates[0], gates[1]

    print(f"Start: {start_gate}\nEnd: {finish_gate}")

    # DFS
    if args.algorithm == "dfs":
        start_time = time.time()
        path, nodes_explored = dfs(arr, start_gate, finish_gate, nodes_explored=0)
        exec_time = time.time() - start_time

        
        if path is not None:
            print("STATUS: PATH FOUND🕺✨✨!")

            if args.stats:
                print("\n\n==========")
                print("STATISITCS")
                print("==========\n\n")
                print("NODES EXPLORED: ", nodes_explored)
                print("PATH LENGTH: ", len(path))
                print("TIME TAKEN: %s SECONDS" % exec_time)
            
            if args.path:
                print("\n\n=====")
                print("PATH")
                print("=====\n\n")
                print(path)

            # Print coloured route through maze on --output flag.
            if args.prettyoutput:
                print("\n\n=============")
                print("PRETTY OUTPUT")
                print("=============\n\n")
                print_colors(arr, path)
                print("\n\n")
        else:
            print("STATUS: 💤PATH NOT FOUND💤")

    # A*
    elif args.algorithm == "a-star":
        start_time = time.time()
        path, nodes_explored = a_star(arr, start_gate, finish_gate)
        exec_time = time.time() - start_time

        if path is not None:
            print("STATUS: PATH FOUND🕺✨✨!")

            if args.stats:
                print("\n\n==========")
                print("STATISITCS")
                print("==========\n\n")
                print("NODES EXPLORED: ", nodes_explored)
                print("PATH LENGTH: ", len(path))
                print("TIME TAKEN: %s SECONDS" % exec_time)

            if args.path:
                print("\n\n=====")
                print("PATH")
                print("=====\n\n")
                print(path)

            if args.prettyoutput:
                print("\n\n=============")
                print("PRETTY OUTPUT")
                print("=============\n\n")
                print_colors(arr, path)
                print("\n\n")
        else:
            print("STATUS: 💤PATH NOT FOUND💤")

    else:
        print("CHOSEN ALGORITHM IS NOT CORRECT !")


if __name__ == "__main__":
    main()