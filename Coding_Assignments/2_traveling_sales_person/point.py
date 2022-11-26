import ast


# (2D point data type to model points in the plane.)
class Point:
    # create the point (x, y)
    def __init__(self, x: float, y: float):
        self.position: tuple = (x, y)

    # Returns a string representation of the point.
    # Should be in coordinate pair output. I.e. (x, y)
    def __str__(self) -> str:
        return f"{self.position}"

    # def __eq__(self, other):
    #     if isinstance(other, str):
    #         try:
    #             other = ast.literal_eval(other)
    #         except:
    #             return False
    #     if other == self.position:
    #         return True
    #     return False

    # def __repr__(self):
    #     return f"{self.position}"

    # return Euclidean distance between the two points
    def distance_to(self, second_point: 'Point') -> float:
        first_point: tuple[float, float] = self.position
        second_point: tuple[float, float] = second_point.position
        # sqrt ( (x2 - x1)^2 + (y2 - y1)^2 )
        delta_x = second_point[0] - first_point[0]
        delta_y = second_point[1] - first_point[1]
        return (delta_x ** 2 + delta_y ** 2) ** (1 / 2)
