class Point:

    # Initializes 2D point with x,y coordinate
    def __init__(self, x: float, y: float):
        self.point: tuple[float, float] = (x, y)

    @property
    def x(self):
        return self.point[0]

    @x.setter
    def x(self, value):
        self.point = (value, self.y)

    @property
    def y(self):
        return self.point[1]

    @y.setter
    def y(self, value):
        self.point = (self.x, value)

    # Strings representations of the Point class.
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.point)

    # # Built in comparators for sorting Points by y-coordinate first and using
    # # x-coordinate for ties.
    # # Here greater than or less than refer to y-coordinate.
    #
    # # Returns True if self has the same (x, y) coordinates as other.
    # def __eq__(self, other: 'Point') -> bool:
    #     return self.point == other.point
    #
    # # Returns True if self is "less than" the point as other
    # def __lt__(self, other: 'Point') -> bool:
    #     return self.y < other.y
    #
    # # Returns True if self is "greater than" the point as other
    # def __gt__(self, other: 'Point') -> bool:
    #     return self.y > other.y

    # Returns the Euclidean distance between self and other
    def distance_to(self, other: 'Point') -> float:
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2)

    # Hash function for Points.
    # Hint: You can use the hash function for tuples.
    def __hash__(self):
        return hash(self.point)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 3)
    print(p1.distance_to(p2))

    print(p1.__hash__())
    print(p1.__hash__())

    print(p1.__eq__(p2), p2.__eq__(p1))
    print(p1.__lt__(p2), p2.__lt__(p1))
    print(p1.__gt__(p2), p2.__gt__(p1))


