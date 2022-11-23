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
    def run_test_(test_function: Callable,
                  test_data: list[tuple[float, float]],
                  reverse_inp: bool = True,
                  ) -> tuple[float, Tour, int]:
        """
        :param test_function:
        :param test_data:
        :param reverse_inp: reverse input for .pop(-1) performance
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
            test_function(Point(node_data[0], node_data[1]))
        run_time = run_timer.elapsed_time()
        return tour.distance(), tour, run_time


if __name__ == "__main__":
    # file_selector indexes test_file_names list
    file_selector: None | int = 4  # None runs all tests

    def truncate(value: float, digits: int) -> float:
        return int(value * (10 ** digits)) / (10 ** digits)

    t = Test()
    tests_to_run = t.test_file_names
    if file_selector is not None:
        tests_to_run = [t.test_file_names[file_selector]]

    for file_name in tests_to_run:
        path = t.working_directory + f"\\{t.test_folder_name}\\" + file_name
        data = t.read_file_test(path)
        gui_bounds = data.pop(0)  # this seems to be GUI data
        result_near = t.run_test_nearest(data, reverse_inp=True)
        result_small = t.run_test_smallest(data, reverse_inp=True)
        dist_near = truncate(result_near[0], 4)
        dist_small = truncate(result_small[0], 4)

        print("test input:", data)
        print('near out:  ', result_near[1].__str__())
        print('\t\t   ', dist_near, result_near[1].length, result_near[2])
        print('small out: ', result_small[1].__str__())
        print('\t\t   ', dist_small, result_small[1].length, result_small[2])
        print('\t\t    ' + '-' * 32)

    x_list = list()
    y_list = list()
    all_data = dict(near_data=[], small_data=[])

    plot_near_data = ast.literal_eval(result_near[1].__str__())
    plot_small_data = ast.literal_eval(result_small[1].__str__())

    for x, y in plot_near_data:
        x_list.append(x)
        y_list.append(y)
    all_data['near_data'].append((x_list, y_list))

    x_list.clear()
    y_list.clear()
    for x, y in plot_small_data:
        x_list.append(x)
        y_list.append(y)
    all_data['small_data'].append((x_list, y_list))

    # x_list += [x_list[0], x_list[-1]]
    # y_list += [y_list[0], y_list[-1]]

    fig = go.Figure(
        go.Scatter(x=x_list, y=y_list, mode='lines'),
    )
    # connect first<->last
    fig.add_trace(
        go.Scatter(x=[x_list[0], x_list[-1]], y=[y_list[0], y_list[-1]], mode='lines'),
    )

    fig.update_layout(
        # width=gui_bounds[0] + gui_bounds[0],
        # height=gui_bounds[1] + gui_bounds[1],
        showlegend=False,
        font_family="Courier New",
        font_color="blue",
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
                    dict(
                        label="Points Off",
                        method="restyle",
                        args=["mode", ["lines"]]
                    ),
                    dict(
                        label="Points On",
                        method="restyle",
                        args=["mode", ["lines+markers"]]
                    )
                ]),
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.11,
                xanchor="center",
                y=1.1,
                yanchor="top"
            ),
        ],
    )

    config = {'displayModeBar': False,
              'scrollZoom': True,
              }
    fig.show(config=config)


