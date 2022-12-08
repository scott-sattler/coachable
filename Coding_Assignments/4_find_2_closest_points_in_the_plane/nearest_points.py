import random
import sys

from point import Point


class DistPointPair:
    def __init__(self, distance, first_point, second_point):
        self.d: float = distance
        self.p1: Point = first_point
        self.p2: Point = second_point

    def __str__(self):
        return f"d={self.d}, p1={self.p1}, p2={self.p2}"


# Represents a set of points and function to find distance of the closest ones.
class NearestPointSet:
    # Initializes an empty set of points.
    def __init__(self):
        self.points: list[Point] = list()
        self.min_dist: float = float('inf')

    # Returns the size of the NearestPointSet
    # Runtime should be O(1)
    def size(self) -> int:
        return len(self.points)

    # Inserts a Point p into the NearestPointSet
    # Runtime should be O(1)
    def insert(self, point: Point) -> None:
        # self.points.update({(point.x, point.y): point})
        self.points.append(point)

    def sort_x(self, low: None | int = None, high: None | int = None):
        if low is None or high is None:
            low = 0
            high = len(self.points) - 1
        points = self.points[low:high + 1]
        self.points[low:high + 1] = sorted(points, key=lambda p: (p.x, p.y))

    # Returns the closest distance between 2 points.
    # Runtime should be O(n log n) in the average case
    # If there are less than 2 points, simply return None.
    def find_closest(self) -> float:
        self.sort_x()
        # low = self.points[0].x
        # high = self.points[-1].x
        min_pair = self._find_closest(0, len(self.points) - 1)
        print("found", min_pair)
        return min_pair.d

    # @staticmethod
    def _find_closest(self, low: int, high: int) -> DistPointPair:
        # # base case(s) # #
        min_d_pair = DistPointPair(float('inf'), None, None)
        if high == low:
            return min_d_pair  # DistPointPair(float('inf'), None, None)
        if high - low < 3:  # todo base case < 4 ??
            if high - low < 1:
                print("high, low", high, low)
            # get all distances
            dist_pairs: list[DistPointPair] = [min_d_pair]  # [DistPointPair(float('inf'), None, None)]
            for i in range(low, high):
                for j in range(low + 1, high + 1):
                    if i != j:
                        p1 = self.points[i]
                        p2 = self.points[j]
                        dist = p1.distance_to(p2)
                        dis_pair = DistPointPair(dist, p1, p2)
                        dist_pairs.append(dis_pair)
            # find min distance
            min_d_pair = min(dist_pairs, key=lambda p: p.d)
            print("min_d_pair", min_d_pair)
            return min_d_pair

        # # input reduction # #
        # find midpoint
        midpoint = ((high - low) // 2) + low

        # recurse left half
        left_half = self._find_closest(low, midpoint)

        # recurse right half
        right_half = self._find_closest(midpoint + 1, high)

        # upper bound of d
        d_up_bnd = min(left_half, right_half, key=lambda p: p.d)

        # get midpoint bounds
        # look at each x until exceed 2d @ midpoint
        l_bnd = midpoint - 1
        r_bnd = midpoint + 1
        while l_bnd > low and self.points[l_bnd].x <= d_up_bnd.d:
            l_bnd -= 1
        while r_bnd < high and self.points[r_bnd + 1].x <= d_up_bnd.d:
            r_bnd += 1

        # sort y
        print("l_bnd, r_bnd", l_bnd, r_bnd)
        print('pre y sort:', self.points)
        self.points[l_bnd:r_bnd] = sorted(self.points[l_bnd:r_bnd], key=lambda p: (p.y, p.x))
        print('post y sort:', self.points)

        # recurse mid
        mid_section = self._find_closest(l_bnd, r_bnd)

        # todo mid sort < 7 er whatever

        return min(left_half, right_half, mid_section, key=lambda x: x.d)

    def __str__(self) -> str:
        return str(self.points)


if __name__ == "__main__":
    inp1 = [(0, 1), (2, 3), (4, 5)]  # todo care equal distances
    inp2 = [(4, 6), (2, 3), (4, 5), (0, 1)]
    inp3 = [(0.0, 0.0), (1.1, 1.1), (2.42, 2.42), (3.99, 3.99), (5.85, 5.85), (8.05, 8.05), (10.62, 10.62), (13.64, 13.64), (17.14, 17.14), (21.22, 21.22), ]
    inp = inp3
    random.shuffle(inp)
    print(inp)
    foo = NearestPointSet()
    for each in inp:
        foo.insert(Point(each[0], each[1]))
    # print(foo.__str__())
    # foo.sort_x(0, )
    # print(foo.__str__())
    ans = foo.find_closest()
    print(ans)


