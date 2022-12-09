import random
from point import Point
from nearest_points import DistPointPair, NearestPointSet

# # point testing
# p1 = Point(0, 0)
# p2 = Point(4, 3)
# print(p1.distance_to(p2))
#
# print(p1.__hash__())
# print(p1.__hash__())
#
# print(p1.__eq__(p2), p2.__eq__(p1),)
# print(Point(3, 7).__eq__(Point(3, 7)))
# # print(p1.__lt__(p2), p2.__lt__(p1))
# # print(p1.__gt__(p2), p2.__gt__(p1))


class Test(NearestPointSet):
    # def __init__(self):
    #     super().__init__()
    #     print(super().__dict__)

    # brute force method override for correctness check
    def _find_closest(self, low: int, high: int) -> DistPointPair:
        min_d_pair = DistPointPair(float('inf'), None, None)
        dist_pairs: list[DistPointPair] = [min_d_pair]
        for i in range(low, high - 1):
            for j in range(low + 1, high):
                if i != j:
                    p1 = self.points[i]
                    p2 = self.points[j]
                    dist = p1.distance_to(p2)
                    dis_pair = DistPointPair(dist, p1, p2)
                    dist_pairs.append(dis_pair)
        # get min distance
        min_d_pair = min(dist_pairs, key=lambda p: p.d)
        return min_d_pair


inp1 = [(0, 1), (2, 3), (4, 5)]  # todo care equal distances
inp2 = [(4, 6), (2, 3), (4, 5), (0, 1)]
inp3 = [(0.0, 0.0), (1.1, 1.1), (2.42, 2.42), (3.99, 3.99), (5.85, 5.85), (8.05, 8.05), (10.62, 10.62), (13.64, 13.64),
        (17.14, 17.14), (21.22, 21.22), ]
inp = inp3
random.shuffle(inp)
print(inp)

# foo = NearestPointSet()
# for each in inp:
#     foo.insert(Point(each[0], each[1]))
# # print(foo.__str__())
# # foo.sort_x(0, )
# # print(foo.__str__())
# ans = foo.find_closest()
# print(ans)

t = Test()  # brute forces for correctness
c = NearestPointSet()
for each in inp:
    t.insert(Point(each[0], each[1]))
    c.insert(Point(each[0], each[1]))
ans_t = t.find_closest()
ans_c = c.find_closest()
print(ans_t == ans_c, ans_t, ans_c)
print(c.points)
print(t.points)


failed = Test()
failed = NearestPointSet()
a = Point(0, 0)
b = Point(0, 2)
c = Point(0, 2)
d = Point(4, 5)
e = Point(1, 1)
f = Point(2, 5)
g = Point(3, 10)
h = Point(1, 0)
points = [a, b, c, d, e, f, g, h]
for each in points:
    failed.insert(each)
print("7 ?=", len(failed.point_set), len(failed.points))
assert 7 == len(failed.point_set) == len(failed.points)


# point_set = NearestPointSet()
# print(point_set)
# assert point_set.find_closest() is None
