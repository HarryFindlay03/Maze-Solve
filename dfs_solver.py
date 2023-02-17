from typing import List

def print2dArray(arr: List[str]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[0])-1):
            print(arr[i][j], end="")
        print(arr[i][j])

def convertToArray(fn: str) -> List[str]:
    """
    Converts the inputted filename, for this case will be any of the mazes into 2D array

    Args:
        fn (str): filename.txt for inputted maze

    Returns:
        List[str]: Output of maze in a 2D array format.
    """

    with open(fn, "r") as f:
        # Stripping newlines from each line in the file
        data = [x.rstrip("\n") for x in f.readlines() if x.strip() != '']
        
        #Removing spaces from the data
        data = [x.replace(" ", "") for x in data]

        #Declaring and placing data into 2D array to be returned
        height, width = len(data), len(data[0])
        return_arr = [["" for x in range(width)] for y in range(height)]

        for i in range(height):
            for j in range(width):
                return_arr[i][j] = data[i][j]

        return return_arr 






def main():
    print("DFS MAZE SOLVER")
    print("----------------")

    print("MAZE:\n\n")
    arr = convertToArray("maze-Small.txt")
    print2dArray(arr)
    print("\n\n")

if __name__ == "__main__":
    main()