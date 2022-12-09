from __future__ import annotations  # testing

from point import Point


class DistPointPair:
    def __init__(self,
                 dist: float,
                 pt_one: None | Point,
                 pt_two: None | Point) -> None:
        self.d: float = dist
        self.p1: None | Point = pt_one
        self.p2: None | Point = pt_two

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
        min_d_pair = DistPointPair(float('inf'), None, None)
        if high == low:
            return min_d_pair
        if high - low < 3:  # todo base case < 4 ??
            # get all distances
            dist_pairs: list[DistPointPair] = [min_d_pair]
            for i in range(low, high):
                for j in range(low + 1, high + 1):
                    if i != j:
                        pnt_1 = self.points[i]
                        pnt_2 = self.points[j]
                        dist = pnt_1.distance_to(pnt_2)
                        dis_pair = DistPointPair(dist, pnt_1, pnt_2)
                        dist_pairs.append(dis_pair)
            # find min distance
            min_d_pair = min(dist_pairs, key=lambda p: p.d)
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
        # look at each x until exceed d<-x->d
        l_bnd = midpoint - 1
        r_bnd = midpoint + 1
        while l_bnd > low and self.points[l_bnd].x <= d_up_bnd.d:
            l_bnd -= 1
        while r_bnd < high and self.points[r_bnd + 1].x <= d_up_bnd.d:
            r_bnd += 1

        # sort y
        self.points[l_bnd:r_bnd] = sorted(self.points[l_bnd:r_bnd],
                                          key=lambda p: (p.y, p.x))
        # recurse mid
        mid_section = self._closest_split_pair(l_bnd, r_bnd)

        return min(left_half, right_half, mid_section, key=lambda x: x.d)

    def _closest_split_pair(self, low: int, high: int) -> DistPointPair:
        # get all distances
        min_d_pair = DistPointPair(float('inf'), None, None)
        dist_pairs: list[DistPointPair] = [min_d_pair]
        for i in range(low, high + 1):
            for j in range(1, 8):
                if high > (i + j) != i:  # (i + j < high) and (i != i + j)
                    pnt_1 = self.points[i]
                    pnt_2 = self.points[i + j]
                    dist_csp = pnt_1.distance_to(pnt_2)
                    dis_pair = DistPointPair(dist_csp, pnt_1, pnt_2)
                    dist_pairs.append(dis_pair)
        # get min distance
        min_d_pair = min(dist_pairs, key=lambda p: p.d)
        return min_d_pair

    def __str__(self) -> str:
        return str(self.points)
