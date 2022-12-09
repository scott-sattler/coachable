from __future__ import annotations  # coachable testing

from point import Point


class DistPointPair:
    def __init__(self, d: float, p_1: None | Point, p_2: None | Point) -> None:
        """ distance between two points

        :param d: distance between p_1 and p_2
        :param p_1: point 1
        :param p_2: point 2
        """
        self.d: float = d
        self.p1: None | Point = p_1
        self.p2: None | Point = p_2

    def __str__(self) -> str:
        return f"d={self.d}, p1={self.p1}, p2={self.p2}"


# Represents a set of points and function to find distance of the closest ones.
class NearestPointSet:
    # Initializes an empty set of points.
    def __init__(self) -> None:
        self.point_set: set = set()
        self.points: list[Point] = list()
        self.min_dist: float = float('inf')

    # Returns the size of the NearestPointSet
    # Runtime should be O(1)
    def size(self) -> int:
        return len(self.points)

    # Inserts a Point p into the NearestPointSet
    # Runtime should be O(1)
    def insert(self, point: Point) -> None:
        if point not in self.point_set:
            self.points.append(point)
            self.point_set.add(point)

    def sort_x(self, low: int, high: int) -> None:
        p_to_srt = self.points[low:high + 1]
        self.points[low:high + 1] = sorted(p_to_srt, key=lambda p: (p.x, p.y))

    # Returns the closest distance between 2 points.
    # Runtime should be O(n log n) in the average case
    # If there are less than 2 points, simply return None.
    def find_closest(self) -> None | float:
        left_bound = 0
        right_bound = len(self.points) - 1
        self.sort_x(left_bound, right_bound)
        min_pair = self._find_closest(left_bound, right_bound)
        if min_pair.d == float('inf'):
            return None
        return min_pair.d

    def _find_closest(self, low: int, high: int) -> DistPointPair:
        # # base case(s) # #
        if high - low < 4:
            return self._get_dist(low, high, split=False)

        # # input reduction # #
        # find midpoint
        midpoint = ((high - low) // 2) + low

        # recurse left half
        left_half = self._find_closest(low, midpoint)

        # recurse right half
        right_half = self._find_closest(midpoint + 1, high)

        # upper bound of d
        upper_bound_d = min(left_half, right_half, key=lambda p: p.d)

        # get midpoint bounds: d<-x->d
        l_mid = midpoint - 1
        r_mid = midpoint + 1
        while l_mid > low and self.points[l_mid].x <= upper_bound_d.d:
            l_mid -= 1
        while r_mid < high and self.points[r_mid].x <= upper_bound_d.d:
            r_mid += 1

        # sort y (in place)
        self.points[l_mid:r_mid + 1] = sorted(self.points[l_mid:r_mid + 1],
                                              key=lambda p: (p.y, p.x))
        # find mid
        mid_section = self._get_dist(l_mid, r_mid, split=True)

        return min(left_half, right_half, mid_section, key=lambda x: x.d)

    def _get_dist(self, lo: int, hi: int, split: bool) -> DistPointPair:
        min_d_pair = DistPointPair(float('inf'), None, None)
        # get all distances
        for i in range(lo, hi):
            for j in range(i + 1, hi + 1):
                if split and j - (i + 1) > 6:
                    break
                pnt_1 = self.points[i]
                pnt_2 = self.points[j]
                dist = pnt_1.distance_to(pnt_2)
                # update min dist if lower
                if dist < min_d_pair.d:
                    min_d_pair = DistPointPair(dist, pnt_1, pnt_2)
        return min_d_pair

    def __str__(self) -> str:
        return str(self.points)
