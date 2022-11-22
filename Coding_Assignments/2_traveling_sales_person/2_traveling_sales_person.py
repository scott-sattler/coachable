import os
import types

from tour import *
import stopwatch
import ast

from tkinter import Tk, Canvas, Frame, BOTH

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
            "custom_tsp0.txt",
            "custom_tsp6_duplicates.txt",

        ]

    test_case_validation = \
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
            return None

    # todo: check performance of (reverse + pop last) vs (pop first)
    @staticmethod
    def run_test_nearest(test_data: list[tuple[float, float]], reverse_inp: bool = True) -> tuple[float, Tour]:
        if reverse_inp:
            test_data = test_data[::-1]  # reverse list
        tour = Tour()
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_nearest(Point(node_data[0], node_data[1]))
        return tour.distance(), tour

    @staticmethod
    def run_test_smallest(test_data: list[tuple[float, float]], reverse_inp: bool = True) -> tuple[float, Tour]:
        if reverse_inp:
            test_data = test_data[::-1]
        tour = Tour()
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_smallest(Point(node_data[0], node_data[1]))
        return tour.distance(), tour


if __name__ == "__main__":
    for each_file in Test.test_file_names:
        t = Test()
        # file_selector = -1  # indexes test_file_names list
        file_selector = each_file
        # path = t.working_directory + f"/{t.test_folder_name}/" + t.test_file_names[file_selector]
        path = t.working_directory + f"/{t.test_folder_name}/" + file_selector
        data = t.read_file_test(path)
        data = data[1:]
        print("test:", data)
        result = t.run_test_nearest(data, reverse_inp=True)
        # result = t.run_test_smallest(data, reverse_inp=True)
        dec = 0  # decimal places
        dist = result[0]  # distance
        truncated = int(dist * (10 ** dec)) / (10 ** dec)
        print('\t ', result[1].__str__())
        print('\t ', truncated, result[1].length)
        print()
        # to check output length: len(ast.literal_eval(result[1].__str__()))

    # def test_duplicates():
    #     coordinates = [
    #         (0, 0),
    #         (3, 0),
    #         (0, 4),
    #         (0, 0),
    #         (0, 0),
    #         (0, 4)
    #     ]
    #
    #     tour = Tour()
    #
    #     for x, y in coordinates:
    #         p = Point(x, y)
    #         tour.insert_smallest(p)
    #
    #     print(tour.size())
    #     assert tour.size() == 6
    #     print(tour.distance())
    #     assert tour.distance() == 12.0
    #
    #
    # test_duplicates()


# heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names
# fns = {k: v for k, v in Tour.__dict__.items() if k in heuristic_fn_names}


# class Example(Frame):
#
#     def __init__(self, data):
#         super().__init__()
#         self.data = data
#         self.initUI(self.data)
#
#
#
#     def initUI(self, data):
#         # self.master.title("Graph")
#         self.pack(fill=BOTH, expand=1)
#         canvas = Canvas(self)
#
#         # x = 100
#         # y = 100
#         size = 10
#         # canvas.create_oval(x, y, x, y, width=100, fill='black')
#         # self.data = [(100, 100)]
#         for each_point in self.data:
#             x = each_point[0]
#             y = each_point[1]
#             canvas.create_rectangle([x, y, x, y], width=size, fill='black')
#
#         canvas.pack(fill=BOTH, expand=1)
#
#
#
# def main():
#
#     t = Test()
#     file_num = 2
#     data = t.read_file_test(t.working_directory + f"/{t.test_folder_name}/" + t.test_file_names[file_num])
#     data = data[1:]
#     print(data)
#     t.test_nearest(data)
#
#     root = Tk()
#     ex = Example(data)
#     root.geometry("400x250+300+300")
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()


# test_cases: list[dict[str:list[tuple]]] = \
#     [
#         {
#             "tsp2.txt":
#             [
#                 (500, 500),  # size of plane (>= bounds)
#                 (200.0, 400.0),
#                 (300.0, 100.0),
#             ]
#         },
#
#         {
#             "tsp3.txt":
#             [
#                 (500, 500),
#                 (200.0, 400.0),
#                 (300.0, 100.0),
#                 (100.0, 100.0),
#             ]
#         },
#
#         {
#             "tsp10.txt":
#             [
#                 (600, 600),
#                 (110.0, 225.0),
#                 (161.0, 280.0),
#                 (325.0, 554.0),
#                 (490.0, 285.0),
#                 (157.0, 443.0),
#                 (283.0, 379.0),
#                 (397.0, 566.0),
#                 (306.0, 360.0),
#                 (343.0, 110.0),
#                 (552.0, 199.0),
#             ]
#         },
#
#     ]
