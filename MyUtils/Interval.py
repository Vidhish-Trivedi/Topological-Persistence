# Class to represent an Interval.

class Interval:
    def __init__(self, dimension, start, end):
        self.dimension = dimension
        self.start = start
        self.end = end
        self.isFinite = True
        if end == None:
            self.isFinite = False

    def __str__(self) -> str:
        if self.isFinite:
            return f"'dimension': {self.dimension}, 'Birth': {self.start}, 'Death': {self.end}"
        else:
            return f"'dimension': {self.dimension}, 'Birth': {self.start}, 'Death': inf"
