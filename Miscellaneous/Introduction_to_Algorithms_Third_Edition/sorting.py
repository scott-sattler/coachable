# no imports
import math
import random

from stopwatch import Stopwatch


class Sort:

    @staticmethod
    def insertion_sort(arr: list) -> list:
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j > -1 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            if arr[0] == "AMTR" and arr[3] == "HELP":
                print(arr)

        return arr

    @staticmethod
    def selection_sort(arr: list) -> list:
        n = len(arr)
        for i in range(0, n):
            min_index = i
            j = i + 1
            while j < n:
                if arr[j] < arr[min_index]:
                    min_index = j
                j += 1
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

    @staticmethod
    def merge_sort(arr: list) -> list:
        # divide and conquer
            # create subproblems 2/n
            # until 'bottoming out'
        pass

    @staticmethod
    def _old_shell_sort(arr: list, gaps: list = (701, 301, 132, 57, 23, 10, 4, 1)):  # using Ciura gap sequence
        n = len(arr)
        for gap in gaps:
            if gap > n:
                continue

            # increment each gap
            for i in range(0, n - gap):
                # only look between gaps
                for j in range(i, n - gap, gap):
                    # merge sort
                    while j > -1 and arr[j] > arr[j + gap]:
                        arr[j], arr[j + gap] = arr[j + gap], arr[j]
                        j -= gap

        return arr

    # @staticmethod
    # def shell_sort(arr: list, gaps: list = (701, 301, 132, 57, 23, 10, 4, 1)):  # using Ciura gap sequence
    #     n = len(arr)
    #     for gap in gaps:
    #         if gap > n:
    #             continue
    #
    #
    #         for i in range(0, n):
    #             j = i
    #             while j < (n - gap) and arr[j]
    #
    #         # increment each gap
    #         for i in range(0, n - gap):
    #             # only look between gaps
    #             for j in range(i, n - gap, gap):
    #                 # merge sort
    #                 while j > -1 and arr[j] > arr[j + gap]:
    #                     arr[j], arr[j + gap] = arr[j + gap], arr[j]
    #                     j -= gap
    #
    #     return arr
    # # Knuth's Formula
    # # h = h * 3 + 1
    # # where −
    # #    h is interval with initial value 1

    @ staticmethod
    def shellsort(arr):
        N = len(arr)

        # We find the shell size to start with.
        # This assumes we use the sequence
        # 1,4,13,40,... 3n + 1,...
        h = 1
        while h < N // 3:
            h = 3 * h + 1

        # Now for each shell size h, we h-sort the array.
        while h > 0:
            for i in range(h, N):
                j = i
                # Swap the adjacent elements in the shell as needed.
                while j >= h and arr[j] < arr[j - h]:
                    arr[j], arr[j - h] = arr[j - h], arr[j]
                    j -= h
            h = h // 3
        return arr

# sorted_arr = Sort().shell_sort([62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28], gaps=[5, 3, 1])
# print(sorted_arr)

times_1 = []
times_2 = []
tests = 1000
rerun_tests = 100
for i in range(rerun_tests):
    # rand_array = [random.randint(0, 1000) for i in range(random.randint(0, 1000))]
    # print(rand_array)

    rand_array = [62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28]

    timer1 = Stopwatch()
    for x in range(tests):
        sorted_arr = Sort().shellsort(rand_array)
    timer1 = timer1.elapsed_time()
    times_1.append(timer1)

    timer2 = Stopwatch()
    for y in range(tests):
        sorted_arr = Sort().shell_sort(rand_array)
    timer2 = timer2.elapsed_time()
    times_2.append(timer2)

    print(timer1, timer2)

avg_1 = sum(times_1)/len(times_1)
avg_2 = sum(times_2)/len(times_2)
print(avg_1, avg_2)
for i in range(len(times_1)):
    print(times_1 > times_2)


