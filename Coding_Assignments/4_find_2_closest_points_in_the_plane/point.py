from __future__ import annotations  # coachable testing


class Point:

    # Initializes 2D point with x,y coordinate
    def __init__(self, x: float, y: float):
        self.point: tuple[float, float] = (x, y)

    @property
    def x(self) -> float:
        return self.point[0]

    @x.setter
    def x(self, value: float) -> None:
        self.point = (value, self.y)

    @property
    def y(self) -> float:
        return self.point[1]

    @y.setter
    def y(self, value: float) -> None:
        self.point = (self.x, value)

    # Strings representations of the Point class.
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.point)

    # # Built in comparators for sorting Points by y-coordinate first and using
    # # x-coordinate for ties.
    # # Here greater than or less than refer to y-coordinate.

    # Returns True if self has the same (x, y) coordinates as other.
    def __eq__(self, other: 'Point') -> bool:  # type: ignore
        # return self.x == other.x and self.y == other.y
        # return hash(self.point) == hash(other)
        # if not isinstance(other, Point):
        #     return NotImplemented
        return self.point == other

    # # Returns True if self is "less than" the point as other
    # def __lt__(self, other: 'Point') -> bool:
    #     return self.y < other.y
    #
    # # Returns True if self is "greater than" the point as other
    # def __gt__(self, other: 'Point') -> bool:
    #     return self.y > other.y

    # Returns the Euclidean distance between self and other
    def distance_to(self, other: 'Point') -> float:
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** (1/2)

    # Hash function for Points.
    # Hint: You can use the hash function for tuples.
    def __hash__(self) -> int:
        return hash(self.point)
