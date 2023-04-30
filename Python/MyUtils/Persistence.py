from MyUtils.Interval import Interval
from MyUtils.Simplex import Simplex
from operator import attrgetter

# Class for generating persistance diagram.

class Persistence:
    def __init__(self, FILE_PATH):
        self.M = []
        self.simplices = []
        # Reading the input.

        print(f"Reading from {FILE_PATH}...\n")
        with open(FILE_PATH) as file:
            for line in file:
                line = line.rstrip().split()
                vertices = line[2:]
                vertices = set(map(lambda x: int(x), vertices))
                self.simplices.append(
                    Simplex(
                        discoveredAt=float(line[0]),
                        dimension=int(line[1]),
                        vertices=vertices,
                    )
                )

        # Sorting on time of discovery, dimension.
        print("Sorting the filteration...")
        self.simplices = sorted(
            self.simplices, key=attrgetter("discoveredAt", "dimension")
        )
        self.num_simplices = len(self.simplices)
        # print(* self.simplices)

        print("Computing border matrix...")
        self.computeMatrix()

        # print("Reducing border matrix...")
        # self.reduceMatrix()
        # printMatrix(self.M)


    # Generating border matrix.
    def computeMatrix(self):
        m = self.num_simplices
        self.M = []

        for j in range(0, m):
            self.M.append([])
            for i in range(0, m):
                self.M[j].append(0)

        for j in range(0, m):
            s: Simplex = self.simplices[j]
            nodes = list(s.vertices)
            if s.dimension >= 1:  # If simplex has dimension 0 then is border is null
                for rmv in nodes:
                    s.vertices.remove(rmv)
                    # Remove one of the nodes
                    for i in range(0, m):  # F is sorted
                        b: Simplex = self.simplices[i]
                        if b.dimension == s.dimension - 1:
                            if b.vertices == s.vertices:
                                self.M[j][i] = 1

                    s.vertices.add(rmv)
        
        for i in range(0, self.num_simplices):
            for j in range(0, self.num_simplices):
                print(self.M[j][i], end=" ")
            print()
        
        print()

    # Gets the index of the lowest non-zero value in a column.
    def low(self, j: int) -> int:
        j_column = self.M[j]
        i = len(j_column) - 1

        while i >= 0:
            if j_column[i] != 0:
                break

            i -= 1

        return i

    # Reduction.
    def reduceMatrix(self):
        # lowPosition[i] will store the index of the lowest non-zero value in i-th column of matrix.
        lowPosition = []
        for i in range(0, self.num_simplices):
            lowPosition.append(-1)

        for i in range(0, self.num_simplices):
            i_column = self.M[i]
            low_idx = self.low(i)

            if low_idx > -1:
                if lowPosition[low_idx] > -1:
                    while low_idx > -1 and lowPosition[low_idx] > -1:
                        for j in range(0, low_idx + 1):
                            i_column[j] = (
                                i_column[j] + self.M[lowPosition[low_idx]][j]
                            ) % 2
                          
                        low_idx = self.low(i)
                if low_idx > -1:
                    lowPosition[low_idx] = i
        
        for i in range(0, self.num_simplices):
            for j in range(0, self.num_simplices):
                print(self.M[j][i], end=" ")
            print()
        print()

    # Generating bar-code intervals.
    def generateBarCodeIntervals(self) -> list:
        barCode = []

        whichColumn = []
        for kk in range(0, self.num_simplices):
            whichColumn.append(-1)

        for j in range(0, self.num_simplices):
            if (self.low(j) > -1):
                whichColumn[self.low(j)] = j
            

        # Going through the columns.
        for j in range(0, self.num_simplices):
            # Calculatin index of low value.
            l = self.low(j)

            # // If there is no low value -> start is infinite
            if (l < 0):
                if (whichColumn[j] == -1):
                    newInterval = Interval(self.simplices[j].dimension, self.simplices[j].discoveredAt, None)
                    barCode.append(newInterval)
                else:
                    newInterval = Interval(self.simplices[j].dimension, self.simplices[j].discoveredAt, self.simplices[whichColumn[j]].discoveredAt)
                    barCode.append(newInterval)
        
        return(barCode)

