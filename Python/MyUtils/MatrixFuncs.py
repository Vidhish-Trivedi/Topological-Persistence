from .Simplex import Simplex


# Function to print a matrix.
def printMatrix(matrix: list) -> None:
    size = len(matrix)
    transposeMatrix = matrix[:][:]
    transpose(matrix, transposeMatrix, size)
    print(f"Size of matrix: {size} x {size}")
    for row in transposeMatrix:
        for val in row:
            print(val, end=" ")
        print()
    print()

# Gets the transpose of a matrix.
def transpose(A: list, B: list, N: int) -> None:
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]

# Generating border matrix.
def computeMatrix(size: int, simplices: list) -> list:
    m = size
    M = []

    for j in range(0, m):
        M.append([])
        for i in range(0, m):
            M[j].append(0)

    for j in range(0, size):  # F is sorted
        s: Simplex = simplices[j]
        nodes = list(s.vertices)
        if s.dimension >= 1:  # If simplex has dimension 0 then is border is null
            for rmv in nodes:
                s.vertices.remove(rmv)
                # Remove one of the nodes
                for i in range(0, m):  # F is sorted
                    b: Simplex = simplices[i]
                    if b.dimension == s.dimension - 1:
                        if b.vertices == s.vertices:
                            M[j][i] = 1

                s.vertices.append(rmv)

    return M


# Gets the index of the lowest non-zero value in a column.
# Pass the column as argument.
def low(j_column: list) -> int:
    i = len(j_column) - 1

    while i >= 0:
        if j_column[i] != 0:
            break

        i -= 1

    return i


# Reduction.
def reduceMatrix(size: int, matrix: list) -> list:
    # lowPosition[i] will store the index of the lowest non-zero value in i-th column of matrix.
    lowPosition = [-1 for _ in range(0, size)]

    for i in range(0, size):
        i_column = matrix[i]
        low_idx = low(i_column)

        if low_idx > -1:
            if lowPosition[low_idx] > -1:
                while low_idx > -1 and lowPosition[low_idx] > -1:
                    for j in range(0, low_idx + 1):
                        i_column[j] = (
                            i_column[j] + matrix[lowPosition[low_idx]][j]
                        ) % 2
                        ##
                        matrix[i] = i_column
                        ##
                    low_idx = low(i_column)
            if low_idx > -1:
                lowPosition[low_idx] = i

    return matrix
