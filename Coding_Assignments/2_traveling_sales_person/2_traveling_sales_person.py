import os
from tour import *

import types
import stopwatch
import ast

import plotly.graph_objects as go

"""
requirements:
a folder "tsp_test_data" containing the test files
tour.py must be in the same directory as this file
tour.py should/must? contain point.py import
"""
# todo: check performance of (reverse + pop last) vs (pop first)
# todo: implement test_case_validation


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
    def truncate(value: float, digits: int) -> float:
        return int(value * (10 ** digits)) / (10 ** digits)

    t = Test()

    # file_selector indexes test_file_names list
    file_selector: None | int = None  # None runs all tests
    tests_to_run = t.test_file_names
    if file_selector is not None:
        tests_to_run = t.test_file_names[file_selector]

    for each_file in tests_to_run:
        file_name = each_file
        path = t.working_directory + f"/{t.test_folder_name}/" + file_name
        data = t.read_file_test(path)
        data = data[1:]  # this seems to be GUI data
        result_near = t.run_test_nearest(data, reverse_inp=True)
        result_small = t.run_test_smallest(data, reverse_inp=True)
        dist_near = truncate(result_near[0], 4)
        dist_small = truncate(result_small[0], 4)

        print("test input:", data)
        print('near out:  ', result_near[1].__str__())
        print('\t\t   ', dist_near, result_near[1].length)
        print('small out: ', result_small[1].__str__())
        print('\t\t   ', dist_small, result_small[1].length)
        print('\t\t    ' + '-' * 32)









fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30],
    lat = [10, 20,30],
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [-50, -60,40],
    lat = [30, 10, -20],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show()




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













# to check output length: len(ast.literal_eval(result[1].__str__()))


# heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names
# fns = {k: v for k, v in Tour.__dict__.items() if k in heuristic_fn_names}





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
