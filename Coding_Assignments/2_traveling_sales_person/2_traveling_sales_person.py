import sys
import time
import os

from point import Point
from tour import Tour
from typing import Union

import plotly.graph_objects as go
import ast
from plotly.graph_objs import Figure

"""
additional requirements:
- a folder "tsp_test_data" containing the test files
- tour.py must be in the same directory as this file
- point.py must be in the same directory as this file

pip install plotly

"""


# todo: check performance of (reverse + pop last) vs (pop first)
# todo: implement test_case_validation / def load_verification_data


class Stopwatch:
    # create a stop watch
    def __init__(self) -> None:
        self.__start_time: None | int = None

    # start the stop watch
    def start(self) -> None:
        self.__start_time = time.perf_counter_ns()

    def restart(self) -> None:
        self.start()

    # returns elapsed time since stopwatch was started
    def elapsed_time(self) -> None | int:
        """:return: elapsed time (nanoseconds) since stopwatch was started"""
        if self.__start_time is None:
            raise Exception("Stopwatch was never started.")
        return time.perf_counter_ns() - self.__start_time


class TestData:
    def __init__(self, name: str, bounds: tuple[float, float], data: list[tuple[float, float]]):
        self.test_name = name
        self.test_data = data
        self.plot_bounds = bounds

    def __str__(self):
        return f"{self.test_data}"


class Test:

    def __init__(self,
                 heuristic_selector: str | list[str],
                 dataset_selector: str | list[str],
                 test_data_dir_path: str) -> None:
        """ output_data format:\n
        {heuristic name:
            {data name: {
                "distance": tour distance, \n
                "time": execution time, \n
                "TestData": TestData object, \n
                "Tour": Tour object, }}}

        :param heuristic_selector: heuristic name or list of names to test
        :param dataset_selector: dataset name or list of names to test; None = all
        :param test_data_dir_path: path of dataset .txt files
        """
        self.heuristic_selector = heuristic_selector
        self.dataset_selector = dataset_selector
        self.test_data_dir_path = test_data_dir_path
        self.working_directory = os.getcwd()
        self.file_names = os.listdir(f'{self.test_data_dir_path}')
        self.input_data: dict[str, list[tuple[float, float]]] = dict()  # dictionary of labeled tests
        self.output_data: dict[str, dict[str, dict[str, Union[float, float, TestData, Tour]]]] = dict()
        self.__dist_truncate: bool | int = False
        self.__time_truncate: bool | int = False
        self.__time_resolution: bool | int = False

        if isinstance(heuristic_selector, str):
            self.heuristic_selector = [self.heuristic_selector]

        if isinstance(self.dataset_selector, str):
            self.dataset_selector = [self.dataset_selector]
        elif isinstance(self.dataset_selector, list) and len(self.dataset_selector) == 0:
            self.dataset_selector = self.file_names

    # experimenting with Python setter/getter
    @property
    def truncated_dist(self) -> bool | int:
        return self.__dist_truncate

    @truncated_dist.setter
    def truncated_dist(self, digits: bool | int):
        self.__dist_truncate = digits

    @property
    def truncated_time(self) -> bool | int:
        return self.__dist_truncate

    @truncated_time.setter
    def truncated_time(self, digits: bool | int):
        self.__dist_truncate = digits

    @property
    def time_resolution(self) -> bool | int:
        return self.__time_resolution

    @time_resolution.setter
    def time_resolution(self, resolution: bool | int = False):
        self.__time_resolution = resolution

    @staticmethod
    def _truncate(value: float, digits: int) -> float:
        return int(value * (10 ** digits)) / (10 ** digits)

    def format_time(self, duration: int, resolution: int = 9, digits: int = 2) -> int | float:
        """ default example: 314.72 milliseconds\n
        :param duration: time to format, in nanoseconds
        :param resolution: 10^(value - 9); 0 - 9 -> sec - nanoseconds
        :param digits: number of digits right of decimal
        :return: formatted time as float (unless in nanoseconds)
        """
        if self.__time_resolution is not False:
            resolution = self.__time_resolution

        if self.__time_truncate is not False:
            digits = self.__time_truncate

        duration = duration * 10 ** (resolution - 9)
        if isinstance(duration, float):
            duration = self._truncate(duration, digits)
        return duration

    def get_tour_result(self, heuristic: str, dataset: str):
        return self.output_data[heuristic][dataset]

    def load_input_data(self) -> None:
        dir_path = self.working_directory + f"\\{test_folder_name}\\"
        tests_to_run = self.dataset_selector
        for each_test in tests_to_run:
            self.input_data.update({each_test: self.read_file_input(dir_path + each_test)})

    def load_verification_data(self):
        raise NotImplementedError

    @staticmethod
    def read_file_input(directory: str) -> list[tuple[float, float]] | None:
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
            raise SystemExit("ERROR: TERMINATING APPLICATION\n" + e.__str__())

    def run_tests(self, reverse_inp: bool = True) -> None:
        """
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
            run_timer = Stopwatch()
            for each_heuristic in self.heuristic_selector:
                test_data_copy = data[:]
                tour = Tour()
                test_function = getattr(tour, each_heuristic)

                run_timer.start()
                while len(test_data_copy) > 0:
                    node_data = test_data_copy.pop(-1)
                    test_function(new_point=Point(node_data[0], node_data[1]))
                run_time = run_timer.elapsed_time()

                distance = tour.distance()
                if self.truncated_dist is not False:
                    distance = self._truncate(distance, self.truncated_dist)

                run_time = self.format_time(run_time)

                if not self.output_data.get(each_heuristic):
                    self.output_data[each_heuristic] = {}
                self.output_data[each_heuristic].update(
                    {
                        test_data.test_name: {
                            "distance": distance,
                            "time (ms)": run_time,
                            "TestData": test_data,
                            "Tour": tour,
                        }})

    def print_output_data(self):
        for each_test in self.output_data.items():
            print(each_test[0])
            for each_dataset in each_test[1].items():
                print('\t' + each_dataset[0] + f' ({each_test[0]})')
                for each_item in each_dataset[1].items():
                    print(f'\t\t {each_item[0]}: {each_item[1]}')


class GraphDataPlotly:

    def __init__(self, test: Test, config: None | dict = None) -> None:
        self.test = test
        self.fig: Figure = Figure()
        self.configuration: None | dict = config

        if self.configuration is None:
            default_config = {
                'displayModeBar': False,
                'scrollZoom': True,
            }
            self.configuration = default_config

    def plot(self, fn_name, data_name) -> None:

        plotly_data = self.test.get_tour_result(fn_name, data_name)
        gui_bounds = plotly_data["TestData"].plot_bounds
        plot_data = ast.literal_eval(plotly_data["Tour"].__str__())

        x_list = list()
        y_list = list()
        for x, y in plot_data:
            x_list.append(x)
            y_list.append(y)

        self.fig = go.Figure(
            go.Scatter(x=x_list, y=y_list, mode='markers', name=""),
        )
        # connect first<->last
        self.fig.add_trace(
            go.Scatter(x=[x_list[0], x_list[-1]], y=[y_list[0], y_list[-1]], mode='markers', name=""),
        )

        self.fig.add_annotation(text="zoom: mouse scroll<br>pan: shift + left mouse button",
                                xref="paper", yref="paper", align="left", font=dict(size=18),
                                x=0.0, y=1.1, showarrow=False)

        self.fig.update_layout(
            xaxis_range=(0, gui_bounds[0]),
            yaxis_range=(0, gui_bounds[1]),
            showlegend=False,
            font_family="Courier New, monospace",
            font_color="black",
            yaxis=dict(scaleanchor="x", scaleratio=1),
            # dragmode=False,
            updatemenus=[
                dict(
                    type="buttons",
                    direction="left",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.02, y=1.0,  # x=0.11, y=1.1,
                    xanchor="left", yanchor="top",
                    buttons=list([
                        dict(label="Points", method="restyle", args=["mode", ["markers"]]),
                        dict(label="Lines+Point", method="restyle", args=["mode", ["lines+markers"]]),
                        dict(label="Lines", method="restyle", args=["mode", ["lines"]]),
                    ]),
                ),
            ],
        )

        self.fig.show(configuration=self.configuration)


if __name__ == "__main__":
    # file_selector
    # this is only a reference to use below
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
    # [] runs all tests
    file_selector: []

    # ######## create/run tests ######### #
    working_directory = os.getcwd()
    test_folder_name = "tsp_test_data"

    # get method names
    # heuristic_fn_names = ["insert_nearest", "insert_smallest"]  # heuristic method names
    fns = [k for k in Tour.__dict__.keys() if "smallest" in k or "nearest" in k]
    heuristic_method_names = fns

    path = working_directory + f"\\{test_folder_name}\\"
    t = Test(heuristic_method_names, [], path)
    t.load_input_data()
    t.truncated_dist = 4
    t.truncated_time = 2
    t.time_resolution = 3  # milliseconds
    t.run_tests(reverse_inp=True)
    result_near = t.get_tour_result("insert_nearest", "tsp1000.txt")
    result_small = t.get_tour_result("insert_smallest", "tsp1000.txt")

    # ############## Print ############## #
    t.print_output_data()

    # ############## Plotly ############# #
    plot_fn_name = "insert_smallest"
    plot_data_name = "tsp1000.txt"
    plot = GraphDataPlotly(t)
    plot.plot(plot_fn_name, plot_data_name)






    # print('foo')
    # watch = Stopwatch()
    # watch.start()
    # time.sleep(1)
    # dur = watch.elapsed_time()
    # dur = watch.format_time(duration=dur, resolution=0, digits=4)
    # print(dur)


    # # ######### Print ######### #
    # print("test input:", result_near["TestData"].test_data)
    #
    # print('near out:  ', result_near["Tour"].__str__())
    # print('\t\t   ', result_near["distance"], result_near["Tour"].length, result_near["time"])
    #
    # print('small out: ', result_small["Tour"].__str__())
    # print('\t\t   ', result_small["distance"], result_small["Tour"].length, result_small["time"])
    #
    # print('\t\t    ' + '-' * 32)


    # # ######### Plotly ######### #
    # plot_fn_name = "insert_smallest"
    # plot_data_name = "tsp1000.txt"
    # plotly_data = t.get_tour_result("insert_smallest", "tsp1000.txt")
    #
    # gui_bounds = plotly_data["TestData"].plot_bounds
    # plot_data = ast.literal_eval(plotly_data["Tour"].__str__())
    #
    # x_list = list()
    # y_list = list()
    # for x, y in plot_data:
    #     x_list.append(x)
    #     y_list.append(y)
    #
    # fig = go.Figure(
    #     go.Scatter(x=x_list, y=y_list, mode='markers', name=""),
    # )
    # # connect first<->last
    # fig.add_trace(
    #     go.Scatter(x=[x_list[0], x_list[-1]], y=[y_list[0], y_list[-1]], mode='markers', name=""),
    # )
    #
    # fig.add_annotation(text="zoom: mouse scroll<br>pan: shift + left mouse button",
    #                    xref="paper", yref="paper", align="left", font=dict(size=18),
    #                    x=0.0, y=1.1, showarrow=False)
    #
    # fig.update_layout(
    #     xaxis_range=(0, gui_bounds[0]),
    #     yaxis_range=(0, gui_bounds[1]),
    #     showlegend=False,
    #     font_family="Courier New, monospace",
    #     font_color="black",
    #     yaxis=dict(scaleanchor="x", scaleratio=1),
    #     # dragmode=False,
    #     updatemenus=[
    #         dict(
    #             type="buttons",
    #             direction="left",
    #             pad={"r": 10, "t": 10},
    #             showactive=True,
    #             x=0.02, y=1.0,  # x=0.11, y=1.1,
    #             xanchor="left", yanchor="top",
    #             buttons=list([
    #                 dict(label="Points", method="restyle", args=["mode", ["markers"]]),
    #                 dict(label="Lines+Point", method="restyle", args=["mode", ["lines+markers"]]),
    #                 dict(label="Lines", method="restyle", args=["mode", ["lines"]]),
    #             ]),
    #         ),
    #     ],
    # )
    #
    # config = {'displayModeBar': False,
    #           'scrollZoom': True,
    #           }
    # fig.show(config=config)
