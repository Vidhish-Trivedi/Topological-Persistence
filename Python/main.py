from MyUtils.Interval import Interval
from MyUtils.Simplex import Simplex
from operator import attrgetter

FILE_PATH = "./tests/filtration.txt"

if __name__ == "__main__":
    simplices = []
    
    # Reading the input.
    with open(FILE_PATH) as file:
        for line in file:
            line = line.rstrip().split()
            vertices = line[2:]
            vertices = list(map(lambda x: int(x), vertices))
            simplices.append(
                Simplex(
                    discoveredAt=float(line[0]),
                    dimension=int(line(1)),
                    vertices=vertices,
                )
            )

    # Sorting on time of discovery, dimension.
    simplices = sorted(simplices, key=attrgetter('discoveredAt', 'dimension'))
    

