from MyUtils.Interval import Interval
from MyUtils.Simplex import Simplex
from MyUtils.MatrixFuncs import computeMatrix, reduceMatrix, printMatrix, generateBarCodeIntervals
from operator import attrgetter

FILE_PATH = "./tests/filtration.txt"

if __name__ == "__main__":
    simplices = []

    # Reading the input.
    print(f"Reading from {FILE_PATH}...\n")
    with open(FILE_PATH) as file:
        for line in file:
            line = line.rstrip().split()
            vertices = line[2:]
            vertices = list(map(lambda x: int(x), vertices))
            simplices.append(
                Simplex(
                    discoveredAt=float(line[0]),
                    dimension=int(line[1]),
                    vertices=vertices,
                )
            )

    # Sorting on time of discovery, dimension.
    print("Sorting the filteration...")
    simplices = sorted(simplices, key=attrgetter("discoveredAt", "dimension"))
    num_simplices = len(simplices)

    # Computing border matrix.
    print("Computing border matrix...")
    matrix = computeMatrix(size=num_simplices, simplices=simplices)
    printMatrix(matrix=matrix)

    # Reducing the matrix.
    print(f"Reducing border matrix ({num_simplices} x {num_simplices})...")
    matrix = reduceMatrix(size=num_simplices, matrix=matrix)
    printMatrix(matrix=matrix)

    # Generating bar-code.
    barCode = generateBarCodeIntervals(filteration=simplices, matrix=matrix)

    for _ in barCode:
        print(_)

