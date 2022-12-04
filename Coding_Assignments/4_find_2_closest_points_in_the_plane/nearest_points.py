from point import Point


# Represents a set of points and function to find distance of the closest ones.
class NearestPointSet:
    # Initializes an empty set of points.
    def __init__(self):
        raise NotImplementedError

    # Returns the size of the NearestPointSet
    # Runtime should be O(1)
    def size(self) -> int:
        raise NotImplementedError

    # Inserts a Point p into the NearestPointSet
    # Runtime should be O(1)
    def insert(self, p: 'Point') -> None:
        raise NotImplementedError

    # Returns the closest distance between 2 points.
    # Runtime should be O(n log n) in the average case
    # If there are less than 2 points, simply return None.
    def find_closest(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError
