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


class Test:
    working_directory = os.getcwd()

    # test_folder_name = "tsp_test_data"

    # file_selector indexes test_file_names list
    file_selector: None | int = 4  # None runs all tests

    heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names

    def __init__(self, heuristic_selector: str, dataset_selector: str, test_data_dir_path: str):
        """

        :param heuristic_selector: heuristic to test
        :param dataset_selector: dataset(s) to use
        :param test_data_dir_path: path of dataset .txt files
        """
        self.test_data_dir_path = test_data_dir_path
        self.file_names = os.listdir(f'{self.test_data_dir_path}')
        self.test_data: dict[str, list[tuple[float, float]]]  # dictionary of labeled datasets

    def load_data(self):
        # self.test_data = self.read_file_test()
        # path = working_directory + f"\\{test_folder_name}\\" + file_name
        # data = t.read_file_test(path)
        # gui_bounds = data.pop(0)  # this seems to be GUI data

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

    # todo use files
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
                          reverse_inp: bool = True,) -> tuple[float, Tour, int]:
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

    @staticmethod
    def run_test(tour_instance: Tour,
                 test_function: str,
                 test_data: list[tuple[float, float]],
                 reverse_inp: bool = True,
                 ) -> tuple[float, Tour, int]:
        """
        :param tour_instance:
        :param test_function:
        :param test_data:
        :param reverse_inp: reverse input for .pop(-1) performance
        :return: distance, tour, run time
        """
        run_time: None | int  # todo check this initial value, should be None?
        run_timer = Stopwatch()
        if reverse_inp:
            test_data = test_data[::-1]
        tour_instance = tour_instance
        foo = getattr(tour_instance, test_function)
        run_timer.restart()
        while len(test_data) > 0:
            node_data = test_data.pop(-1)
            test_function(new_point=Point(node_data[0], node_data[1]))
        run_time = run_timer.elapsed_time()
        return tour_instance.distance(), tour_instance, run_time


if __name__ == "__main__":
    working_directory = os.getcwd()

    test_folder_name = "tsp_test_data"

    # file_selector indexes test_file_names list
    file_selector: None | int = 4  # None runs all tests

    heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names

    def truncate(value: float, digits: int) -> float:
        return int(value * (10 ** digits)) / (10 ** digits)


    path = working_directory + f"\\{test_folder_name}\\"
    t = Test(test_data_dir_path=path)
    test_results: dict = dict()
    tests_to_run = t.test_file_names
    if file_selector is not None:
        tests_to_run = [t.test_file_names[file_selector]]

    for file_name in tests_to_run:
        tour = Tour()
        print(tour.__class__.__dict__)
        fns = {k: v for k, v in tour.__class__.__dict__.items() if k in heuristic_fn_names}
        print(fns)
        path = working_directory + f"\\{test_folder_name}\\" + file_name
        data = t.read_file_test(path)
        gui_bounds = data.pop(0)  # this seems to be GUI data
        for each_heuristic in fns.values():
            result_near = t.run_test_nearest(data, reverse_inp=True)
            # test_results = {""}
            result_small_old = t.run_test_smallest(data, reverse_inp=True)
            result_small = t.run_test(tour, each_heuristic, data, reverse_inp=True)
            assert result_small == result_small_old
            test_results = {""}
            dist_near = truncate(result_near[0], 4)
            dist_small = truncate(result_small[0], 4)

        # print("test input:", data)
        # print('near out:  ', result_near[1].__str__())
        # print('\t\t   ', dist_near, result_near[1].length, result_near[2])
        # print('small out: ', result_small[1].__str__())
        # print('\t\t   ', dist_small, result_small[1].length, result_small[2])
        # print('\t\t    ' + '-' * 32)

    x_list = list()
    y_list = list()
    all_data = dict(near_data=[], small_data=[])

    # plot_near_data = ast.literal_eval(result_near[1].__str__())
    # plot_small_data = ast.literal_eval(result_small[1].__str__())

    plot_data = ast.literal_eval(result_small[1].__str__())

    for x, y in plot_data:
        x_list.append(x)
        y_list.append(y)
    all_data['_data'].append((x_list, y_list))

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
                    dict(label="Lines", method="restyle", args=["mode", ["lines"]]),
                    dict(label="Lines+Point", method="restyle", args=["mode", ["lines+markers"]]),
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


