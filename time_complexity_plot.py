from matplotlib import pyplot


def graph_series(list_of_execution_time):
    values = {}

    for element in list_of_execution_time:
        if element[0] not in values:
            values[element[0]] = [(element[2] - element[1])]
        else:
            values[element[0]].append(element[2] - element[1])
    for key, value in values.items():
        pyplot.plot(value, markersize=20, label=key)

    pyplot.legend()
    pyplot.show()


myList = [
    ['algorithm_1', 1, 2], ['algorithm_1', 1, 5],
    ['algorithm_2', 1, 3], ['algorithm_2', 1, 6],
]

graph_series(myList)
