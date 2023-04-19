from __future__ import annotations

from __future__ import annotations


# (2D point data type to model points in the plane.)
class Point:
    # create the point (x, y)
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Returns a string representation of the point.
    # Should be in coordinate pair output with no spaces.
    # i.e. (x,y)
    def __str__(self) -> str:
        return f'({self.x},{self.y})'

    # return Euclidean distance between the two points
    def distance_to(self, that: Point) -> float:
        return ((that.x - self.x) ** 2 + (that.y - self.y) ** 2) ** (1 / 2)


a = Point(0, 0)
b = Point(0, 2)
ans = 2.0
print(a.distance_to(b), ans)

# from __future__ import annotations

'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.
Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''


# from point import Point


# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
    def __init__(self, point):
        # This node's point
        self.point = point
        # The next node
        self.next = None


class Tour:
    # Creates an empty tour
    # Initialize any instance variables you think are needed.
    def __init__(self):
        self.head = None
        self.nodes = 0

    # Returns string representation of the Tour.
    # Should output a list of all points on the Tour.
    def __str__(self):
        str_list = []
        pointer = self.head
        while pointer:
            str_list.append(pointer.point.__str__)
            pointer = pointer.next
        return ' '.join(str_list)

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.
    def size(self):
        return self.nodes

    # Computes and returns the distance of entire tour
    def distance(self):
        dist = 0
        p1 = self.head
        p2 = p1.next if p1 else None

        while p1 and p2:
            dist += p1.point.distance_to(p2.point)
            p1 = p1.next
            p2 = p2.next if p2.next else self.head

        return dist

    # Helper function to insert a new point p into the Tour after a previous Node prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insertNearest and insertSmallest
    # once you find the point you should insert p after.
    def _insert_at(self, p, prev: Node):
        pointer = self.head
        new_node = Node(p)
        self.nodes += 1

        if not self.head:
            self.head = new_node
            return

        while pointer is not prev:
            pointer = pointer.next

        new_node.next = pointer.next
        pointer.next = new_node

    # Insert a new Point p to the Tour using nearest neighbor heuristic
    def insert_nearest(self, p):
        # nearest neighbor: min(distance between current and all other nodes)
        pointer = self.head
        prev_node = pointer
        nearest = float('inf')

        while pointer:
            dist = abs(pointer.point.distance_to(p))
            if dist < nearest:
                nearest = dist
                prev_node = pointer
            pointer = pointer.next

        self._insert_at(p, prev_node)

    # Insert a new Point p to the Tour using smallest increase heuristic
    def insert_smallest(self, p):
        # smallest increase heuristic: min(insert node between every other node)

        # performant solution:
        # subtract distance from pointer_node to pointer_node.next
        # add distance from pointer_node to new_node
        # add distance from new_node to pointer_node.next

        p1 = self.head
        p2 = p1.next if self.head else None
        min_node = self.head
        min_diff = float('inf')

        while p1 and p2:
            diff = p1.point.distance_to(p2.point)
            add_a = p1.point.distance_to(p)
            add_b = p.distance_to(p2.point)

            if (add_a + add_b - diff) < min_diff:
                min_node = p1
                min_diff = (add_a + add_b - diff)

            p1 = p1.next
            p2 = p2.next if p2.next else self.head  # loop it

        self._insert_at(p, min_node)


# ##############################
# ########## testing ###########
# ##############################


import unittest  # noqa


# from __future__ import annotations
# from point import Point
# from tour import Tour


class TestPoint(unittest.TestCase):

    def test_string(self):
        a = Point(1, 2)  # noqa
        self.assertEqual(str(a), '(1,2)')

    def test_distance(self):
        a = Point(0, 0)  # noqa
        b = Point(0, 2)  # noqa
        self.assertEqual(a.distance_to(b), 2.0)

        c = Point(4, 5)
        d = Point(1, 1)
        self.assertEqual(c.distance_to(d), 5.0)

        e = Point(1, 7)
        f = Point(13, 2)
        self.assertEqual(e.distance_to(f), 13.0)


def read_point_file(filename: str):
    point_list = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = line.split()
            x = float(row[0])
            y = float(row[1])
            p = Point(x, y)
            point_list.append(p)
    return point_list


class TestTour(unittest.TestCase):
    file_location = './test_data'
    tsp_2 = read_point_file(file_location + '/tsp2.txt')
    tsp_3 = read_point_file(file_location + '/tsp3.txt')
    tsp_10 = read_point_file(file_location + '/tsp10.txt')
    tsp_100 = read_point_file(file_location + '/tsp100.txt')
    tsp_1000 = read_point_file(file_location + '/tsp1000.txt')

    def test_tour_simple_example(self):
        coordinates = [
            (0, 0),
            (3, 0),
            (0, 4)
        ]

        tour = Tour()

        for x, y in coordinates:
            p = Point(x, y)
            tour.insert_nearest(p)

        self.assertEqual(tour.size(), 3)
        self.assertEqual(tour.distance(), 12.0)

    def test_duplicates(self):
        coordinates = [
            (0, 0),
            (3, 0),
            (0, 4),
            (0, 0),
            (0, 0),
            (0, 4)
        ]

        tour = Tour()

        for x, y in coordinates:
            p = Point(x, y)
            tour.insert_smallest(p)

        self.assertEqual(tour.size(), 6)
        self.assertEqual(tour.distance(), 12.0)

    def test_empty_tour(self):
        tour = Tour()
        self.assertEqual(tour.size(), 0)
        self.assertEqual(tour.distance(), 0)

    def test_tsp_2_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_2:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 565.68542, places=2)
        self.assertEqual(smallest_tour.size(), 2)

    def test_tsp_3_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_3:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 832.4555320336758, places=2)
        self.assertEqual(smallest_tour.size(), 3)

    def test_tsp_10_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_10:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 1655.7461857661865, places=2)
        self.assertEqual(smallest_tour.size(), 10)

    def test_tsp_100_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_100:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 4887.219040311983, places=2)
        self.assertEqual(smallest_tour.size(), 100)

    def test_tsp_1000_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_1000:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 17265.6282, places=2)
        self.assertEqual(smallest_tour.size(), 1000)

    def test_tsp_2_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_2:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 565.68542, places=4)
        self.assertEqual(nearest_tour.size(), 2)

    def test_tsp_3_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_3:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 832.4555320336758, places=4)
        self.assertEqual(nearest_tour.size(), 3)

    def test_tsp_10_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_10:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 1566.1363051360363, places=4)
        self.assertEqual(nearest_tour.size(), 10)

    def test_tsp_100_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_100:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 7389.929676351667, places=4)
        self.assertEqual(nearest_tour.size(), 100)

    def test_tsp_1000_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_1000:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 27868.7106, places=4)
        self.assertEqual(nearest_tour.size(), 1000)


import pytest  # noqa

# do not modify this function call
retcode = pytest.main(['-v'])  # noqa
