class Interval:
    def __init__(self, dimension: int, start: float, end: float):
        self.dimension = dimension
        self.start = start
        self.end = end
        self.isFinite = True
        if end == None:
            self.isFinite = False

    def __str__(self) -> dict:
        if self.isFinite:
            return f"'dimension': {self.dimension}, 'Birth': {self.start}, 'Death': {self.end}"
        else:
            return f"'dimension': {self.dimension}, 'Birth': {self.start}, 'Death': inf"
