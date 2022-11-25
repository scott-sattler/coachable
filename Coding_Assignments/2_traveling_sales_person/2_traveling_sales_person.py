import time
import os
from point import Point
from tour import Tour
from typing import Callable

import plotly.graph_objects as go
import ast

"""
additional requirements:
- a folder "tsp_test_data" containing the test files
- tour.py must be in the same directory as this file
- point.py must be in the same directory as this file

pip install plotly
"""


# todo: check performance of (reverse + pop last) vs (pop first)
# todo: implement test_case_validation


class Stopwatch:
    # create and start a stop watch
    def __init__(self) -> None:
        self.__start_time: int = time.perf_counter_ns()

    def restart(self) -> None:
        self.__start_time = time.perf_counter_ns()

    # returns elapsed time since stopwatch was started
    def elapsed_time(self, resolution: int = 1e-9) -> int:
        """
        :param resolution: resolution down to ns; default 1e-9
        :return: elapsed time (seconds) since stopwatch was started
        """
        elapsed = time.perf_counter_ns() - self.__start_time
        return elapsed * resolution


class TestData:
    def __init__(self, name: str, bounds: tuple[float, float], data: list[tuple[float, float]]):
        self.test_name = name
        self.test_data = data
        self.plot_bounds = bounds


class Test:
    # working_directory = os.getcwd()
    #
    # # test_folder_name = "tsp_test_data"
    #
    # # file_selector indexes test_file_names list
    # file_selector: None | int = 4  # None runs all tests
    #
    # heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names

    def __init__(self,
                 heuristic_selector: str | list[str],
                 dataset_selector: None | str | list[str],
                 test_data_dir_path: str):
        """

        :param heuristic_selector: name or list of heuristic names to test
        :param dataset_selector: name or list of dataset names to test; None = all
        :param test_data_dir_path: path of dataset .txt files
        """
        self.heuristic_selector = heuristic_selector
        self.dataset_selector = dataset_selector
        self.test_data_dir_path = test_data_dir_path
        self.working_directory = os.getcwd()
        self.file_names = os.listdir(f'{self.test_data_dir_path}')
        self.input_data: dict[str, list[tuple[float, float]]] = dict()  # dictionary of labeled tests
        self.output_data: dict[str, list[tuple[float, float]]] = dict()  # dictionary of labeled results
        self.results: any = {}
        self.truncated_size = False

        if isinstance(heuristic_selector, str):
            self.heuristic_selector = [self.heuristic_selector]

        if dataset_selector is None:
            self.dataset_selector = self.file_names

    def set_format(self, digits: bool | int = False):
        self.truncated_size = digits

    # def get_tour_results(self):
    #     return

    @staticmethod
    def truncate(value: float, digits: int) -> float:
        return int(value * (10 ** digits)) / (10 ** digits)

    def load_data(self) -> None:
        path = self.working_directory + f"\\{test_folder_name}\\"
        tests_to_run = self.dataset_selector
        for each_test in tests_to_run:
            self.input_data.update({each_test: self.read_file_test(path + each_test)})

    # todo use files for this
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
                points_list: list = list()
                for each in contents:
                    points_list.append(tuple(map(float, each.split())))  # split() includes \n
                test_case = points_list
                return test_case
        except Exception as e:
            print("ERROR\n" + e.__str__() + "\n" + "ABORTING")
            return None

    @staticmethod
    def run_test_nearest(test_data: list[tuple[float, float]],
                         reverse_inp: bool = True) -> tuple[float, Tour, int]:
        """
        :param test_data:
        :param reverse_inp: reverse input for performance
        :return: distance, tour, run time
        """
        run_time: None | int = None
        run_timer = Stopwatch()
        if reverse_inp:
            test_data = test_data[::-1]  # reverse list
        tour = Tour()
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_nearest(Point(node_data[0], node_data[1]))
        run_time = run_timer.elapsed_time()
        return tour.distance(), tour, run_time

    @staticmethod
    def run_test_smallest(test_data: list[tuple[float, float]],
                          reverse_inp: bool = True, ) -> tuple[float, Tour, int]:
        """
        :param test_data:
        :param reverse_inp: reverse input for performance
        :return: distance, tour, run time
        """
        run_time: None | int = None
        run_timer = Stopwatch()
        if reverse_inp:
            test_data = test_data[::-1]
        tour = Tour()
        run_timer.restart()
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            tour.insert_smallest(Point(node_data[0], node_data[1]))
        run_time = run_timer.elapsed_time()
        return tour.distance(), tour, run_time

    def run_tests(self, reverse_inp: bool = True, truncate_result: bool | int = False) -> None:
        """
        :param truncate_result: default: False; digits
        :param reverse_inp: reverse input for .pop(-1) performance
        """
        run_time: None | int  # todo check this initial value, should be None?
        for each_test in self.input_data.items():
            test_data = TestData(
                name=each_test[0],
                data=each_test[1][1:],
                bounds=each_test[1][0]
            )
            data = test_data.test_data
            if reverse_inp:
                data = data[::-1]
            for each_heuristic in self.heuristic_selector:
                test_data_copy = data[:]
                run_timer = Stopwatch()
                tour = Tour()
                test_function = getattr(tour, each_heuristic)

                run_timer.restart()
                while len(test_data_copy) > 0:
                    node_data = test_data_copy.pop(-1)
                    test_function(new_point=Point(node_data[0], node_data[1]))
                run_time = run_timer.elapsed_time()

                distance = tour.distance()
                if truncate_result:
                    distance = self.truncate(distance, self.truncated_size)

                if not self.results.get(each_heuristic):
                    self.results[each_heuristic] = {}
                self.results[each_heuristic].update(
                    {
                        test_data.test_name:
                            [test_data, distance, run_time, tour]
                    }
                )


if __name__ == "__main__":
    # test_file_names = \
    #     [
    #         "tsp2.txt",
    #         "tsp3.txt",
    #         "tsp10.txt",
    #         "tsp100.txt",
    #         "tsp1000.txt",
    #         "custom_tsp4.txt",
    #         "custom_tsp0.txt",
    #         "custom_tsp6_duplicates.txt",
    #
    #     ]

    test_file_names = [
        'custom_tsp0.txt',
        'custom_tsp4.txt',
        'custom_tsp6_duplicates.txt',
        'tsp10.txt',
        'tsp100.txt',
        'tsp1000.txt',
        'tsp2.txt',
        'tsp3.txt',
    ]

    working_directory = os.getcwd()

    test_folder_name = "tsp_test_data"

    # file_selector indexes test_file_names list
    file_selector: None | int = 4  # None runs all tests

    heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names

    method_name_contains = "smallest"
    fns = [k for k in Tour.__dict__.keys() if "smallest" in k]
    heuristic_method_names = fns

    path = working_directory + f"\\{test_folder_name}\\"
    # t = Test([heuristic_fn_names[1]], None, path)
    t = Test(heuristic_fn_names[1], ['tsp1000.txt'], path)
    t.load_data()
    t.run_tests()
    print(t.results)

    # path = working_directory + f"\\{test_folder_name}\\"
    # t = Test(test_data_dir_path=path)
    # test_results: dict = dict()
    # tests_to_run = t.test_file_names
    # if file_selector is not None:
    #     tests_to_run = [t.test_file_names[file_selector]]
    #
    # for file_name in tests_to_run:
    #     tour = Tour()
    #     print(tour.__class__.__dict__)
    #     fns = {k: v for k, v in tour.__class__.__dict__.items() if k in heuristic_fn_names}
    #     print(fns)
    #     path = working_directory + f"\\{test_folder_name}\\" + file_name
    #     data = t.read_file_test(path)
    #     gui_bounds = data.pop(0)  # this seems to be GUI data
    #     for each_heuristic in fns.values():
    #         result_near = t.run_test_nearest(data, reverse_inp=True)
    #         # test_results = {""}
    #         result_small_old = t.run_test_smallest(data, reverse_inp=True)
    #         result_small = t.run_test(tour, each_heuristic, data, reverse_inp=True)
    #         assert result_small == result_small_old
    #         test_results = {""}
    #         dist_near = truncate(result_near[0], 4)
    #         dist_small = truncate(result_small[0], 4)

    # print("test input:", data)
    # print('near out:  ', result_near[1].__str__())
    # print('\t\t   ', dist_near, result_near[1].length, result_near[2])
    # print('small out: ', result_small[1].__str__())
    # print('\t\t   ', dist_small, result_small[1].length, result_small[2])
    # print('\t\t    ' + '-' * 32)

    x_list = list()
    y_list = list()
    # all_data = dict(near_data=[], small_data=[])

    # plot_near_data = ast.literal_eval(result_near[1].__str__())
    # plot_small_data = ast.literal_eval(result_small[1].__str__())

    # plot_data = ast.literal_eval(result_small[1].__str__())
    # gui_bounds = t.results[0][0][1][0]
    plot_fn_name = "insert_smallest"
    plot_data_name = "tsp1000.txt"

    # gui_bounds = t.results.keys()[0]
    key_0d = list(t.results.keys())[0]
    key_1d = list(t.results[list(t.results.keys())[0]])[0]
    gui_bounds = t.results[key_0d][key_1d][0].plot_bounds
    # plot_data = ast.literal_eval(t.results[0][3].__str__())
    plot_data = ast.literal_eval(t.results[key_0d][key_1d][-1].__str__())

    for x, y in plot_data:
        x_list.append(x)
        y_list.append(y)
    # all_data['_data'].append((x_list, y_list))

    # for x, y in plot_near_data:
    #     x_list.append(x)
    #     y_list.append(y)
    # all_data['near_data'].append((x_list, y_list))
    #
    # x_list.clear()
    # y_list.clear()
    # for x, y in plot_small_data:
    #     x_list.append(x)
    #     y_list.append(y)
    # all_data['small_data'].append((x_list, y_list))

    # x_list += [x_list[0], x_list[-1]]
    # y_list += [y_list[0], y_list[-1]]

    fig = go.Figure(
        go.Scatter(x=x_list, y=y_list, mode='markers'),

    )
    # connect first<->last
    fig.add_trace(
        go.Scatter(x=[x_list[0], x_list[-1]], y=[y_list[0], y_list[-1]], mode='markers'),
    )

    fig.update_layout(
        xaxis_range=(0, gui_bounds[0]),
        yaxis_range=(0, gui_bounds[1]),
        showlegend=False,
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green",
        yaxis=dict(scaleanchor="x", scaleratio=1),
        dragmode=False,
        updatemenus=[
            dict(
                type="buttons",
                direction="left",
                buttons=list([
                    dict(label="Points", method="restyle", args=["mode", ["markers"]]),
                    dict(label="Lines+Point", method="restyle", args=["mode", ["lines+markers"]]),
                    dict(label="Lines", method="restyle", args=["mode", ["lines"]]),
                ]),
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.02, y=1.0,  # x=0.11, y=1.1,
                xanchor="left", yanchor="top",

            ),
        ],
    )

    config = {'displayModeBar': False,
              'scrollZoom': True,
              }
    fig.show(config=config)
