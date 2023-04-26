class Simplex:
    def __init__(self, discoveredAt: float, dimension: int, vertices: set):
        self.discoveredAt = discoveredAt
        self.dimension = dimension
        self.vertices = vertices

    def __str__(self) -> dict:
        return str({
            "discoveredAt": self.discoveredAt,
            "dimension": self.dimension,
            "vertices": self.vertices,
        })
