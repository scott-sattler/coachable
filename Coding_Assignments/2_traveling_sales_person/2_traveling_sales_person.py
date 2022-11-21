import os
from tour import *
import stopwatch
import ast


"""
requirements:
a folder "tsp_test_data" containing the test files
tour.py must be in the same directory as this file
tour.py should/must? contain point.py import
"""


class Test:
    test_folder_name = "tsp_test_data"
    working_directory = os.getcwd()

    test_file_names = \
        [
            "tsp2.txt",
            "tsp3.txt",
            "tsp10.txt",
            "tsp100.txt",
            "tsp1000.txt",
            "custom_tsp4.txt",
        ]

    nearest_validation = \
        {
            "tsp2.txt":
                [
                    (316.22776601683796, 316.22776601683796),  # correct distance pop(0) pop(-1)
                    ()  # correct tuple of point tuples
                ],
            "tsp3.txt":
                [
                    (516.2277660168379, 632.4555320336759),
                    ()
                ],
        }

    @staticmethod
    def read_file_test(directory: str) -> list[tuple[float, float]] | None:
        test_case: list[tuple[float, float]]
        try:
            with open(directory) as file:
                contents = file.readlines()  # eg ['500 500\n', '200.0 400.0\n', '300.0 100.0\n']
                points_list: list = []
                for each in contents:
                    points_list.append(tuple(map(float, each.split())))  # split() includes \n
                test_case = points_list
                return test_case
        except Exception as e:
            print("ERROR\n" + e.__str__() + "\n" + "ABORTING")
            quit()

    def test_test(self, test_data: list[tuple[float, float]]):
        first_coord = test_data[0]
        my_tour = Tour(Node(Point(first_coord[0], first_coord[1])))
        head = my_tour.head
        n = len(test_data)
        for i in range(1, n):
            coord = test_data[i]
            point = Point(coord[0], coord[1])
            my_tour._insert_at(head.point, Node(point))
        print(my_tour.__str__())
        print(my_tour.distance())
        print(my_tour.length)

    # todo: check performance of (reverse + pop last) vs (pop first)
    def test_nearest(self, test_data: list[tuple[float, float]], reverse_inp: bool = True) -> tuple[float, Tour]:
        if reverse_inp:
            test_data = test_data[::-1]  # reverse list
        node_data = test_data.pop(-1)  # default () -> (-1)
        tour = Tour(Node(Point(node_data[0], node_data[1])))
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_nearest(Point(node_data[0], node_data[1]))
        return tour.distance(), tour

    def test_smallest(self, test_data: list[tuple[float, float]], reverse_inp: bool = True) -> tuple[float, Tour]:
        if reverse_inp:
            test_data = test_data[::-1]  # reverse list
        node_data = test_data.pop(-1)  # default () -> (-1)
        tour = Tour(Node(Point(node_data[0], node_data[1])))
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_smallest(Point(node_data[0], node_data[1]))
        return tour.distance(), tour


t = Test()
file_selector = 4  # indexes test_file_names list
path = t.working_directory + f"/{t.test_folder_name}/" + t.test_file_names[file_selector]
data = t.read_file_test(path)
data = data[1:]
# print(data)
# result = t.test_nearest(data, reverse_inp=True)
result = t.test_smallest(data, reverse_inp=True)
dec = 0  # decimal places
dist = result[0]  # distance
truncated = int(dist * (10 ** dec)) / (10 ** dec)
print(truncated, result[1].length, result[1].__str__())
# to check output length: len(ast.literal_eval(result[1].__str__()))


