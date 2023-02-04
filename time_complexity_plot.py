from matplotlib import pyplot
import stopwatch as s

# usage:
# provide function below
# update test_function accordingly


# #### Provide Function Being Tested BELOW #### #

# # Code Block D
# def fn_d(n: int) -> int:
#     if n <= 1:
#         return 1
#     count = 0
#     for i in range(n):
#         count += i
#     return fn_d(n // 2) + fn_d(n // 2) + count

# # Code Block A
# def fn_a(n: int) -> int:
#     if n == 1:
#         return n
#     return fn_a(n - 1) + 1

# # Code Block B
# def fn_b(n: int) -> int:
#     if n == 1:
#         return n
#     return fn_b(n - 1) + fn_b(n - 1)

# # Code Block C
# def fn_c(n: int) -> int:
#     if n == 1:
#         return n
#     return fn_c(n - 1) * n

# # Code Block D
# def fn_d(n: int) -> int:
#     if n <= 1:
#         return 1
#     count = 0
#     for i in range(n):
#         count += i
#     return fn_d(n // 2) + fn_d(n // 2) + count

# # Code Block E
# def fn_e(n: int) -> int:
#     if n == 0:
#         return 1
#     return fn_e(n // 2) + fn_e(n // 2)

# # Code Block F
# def fn_f(n: int) -> int:
#     if n + 1 < 0:
#         return n
#     return fn_f(n // 2) + fn_f(n // 2)

# Code Block G
def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n // 2, m) + fn_g(n, m // 2)

# #### Provide Function Being Tested ABOVE #### #


def test_function(n, m):
    # return fn_d(arg)  # REPLACE with function being tested
    # return fn_a(n)
    # return fn_b(n)
    # return fn_c(n)
    # return fn_d(n)
    # return fn_e(n)
    # return fn_f(n)
    return fn_g(n, m)


iterations = 11
# iterator = range(iterations)
# iterator = [0, 0, 0, 1, 10, 100, 1_000, 10_000]
# extra_zeros = 2
# iterator = [1, 10, 100, 1_000, 10_000]
iterator = [2, 4, 8, 16]
extra_zeros = 0

time_step = []
time_duration = []
values = []

timer = s.Stopwatch()
delta_time = timer.elapsed_time(resolution=1)
for n in iterator:
    # inp = 10 ** n
    inp = n

    timer.restart()
    value = test_function(inp, inp)
    delta_time = timer.elapsed_time(resolution=1)  # /1_000_000_000
    time_duration.append(delta_time)
    time_step.append(n)
    values.append(value)

graph_data = [
    ['tested_fn'] + time_step[extra_zeros:], ['tested_fn'] + time_duration[extra_zeros:],  # noqa: mixed types
]


def graph_series(list_of_execution_time):
    values = {}

    for element in list_of_execution_time:
        if element[0] not in values:
            values[element[0]] = [(element[2] - element[1])]
        else:
            values[element[0]].append(element[2] - element[1])
    for key, value in values.items():
        pyplot.plot(value, markersize=20, label=key)

    ax = pyplot.gca()
    # ax.set_aspect('equal', adjustable='box')
    # ax.axis('scaled')
    # ax.axis('square')

    pyplot.legend()
    pyplot.show()


for i, j in enumerate(zip(time_step, time_duration)):
    print(j[0], j[1], values[i])


graph_series(graph_data)
