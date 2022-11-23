import time


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

