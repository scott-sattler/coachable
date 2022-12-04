class Point:

    # Initializes 2D point with x,y coordinate
    def __init__(self, x: float, y: float):
        raise NotImplementedError

    # Strings representations of the Point class.
    def __repr__(self) -> str:
        raise NotImplementedError
        return str(self)

    def __str__(self) -> str:
        raise NotImplementedError

    # Built in comparators for sorting Points by y-coordinate first and using x-coordinate for ties.
    # Here greater than or less than refer to y-coordinate.

    # Returns True if self has the same (x,y) coordinates as other.
    def __eq__(self, other: 'Point') -> bool:
        raise NotImplementedError

    # Returns True if self is "less than" the point as other
    def __lt__(self, other: 'Point') -> bool:
        raise NotImplementedError

    # Returns True if self is "greater than" the point as other
    def __gt__(self, other: 'Point') -> bool:
        raise NotImplementedError

    # Returns the Euclidean distance between self and other
    def distance_to(self, other: 'Point') -> float:
        raise NotImplementedError

    # Hash function for Points.
    # Hint: You can use the hash function for tuples.
    def __hash__(self):
        raise NotImplementedError
    