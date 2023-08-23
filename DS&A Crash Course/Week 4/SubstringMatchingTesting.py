from SubstringMatchingAlgorithms import all_fns
from SubstringMatchingAlgorithms import _failure_function
from SubstringMatchingAlgorithms import _get_alphabet
from SubstringMatchingAlgorithms import _hash


from SubstringMatchingAlgorithms import *
from hf_data_classes import GenericTC, TestCase, Results
from SubstringMatchingTestCases import perfect_hash_tests
from SubstringMatchingTestCases import failure_function_tests
from SubstringMatchingTestCases import correctness_test_cases

# all_fns = SubMatchAlgo.all_fns
# _get_alphabet =


class Testing:
    cr_str = 'COACHABLEROCKS'
    cr_sorted = 'AABCCCEHKLOORS'

    # def __init__(self):
    #     super().__init__()

    @staticmethod
    def run_failure_function_tests(tests):
        # todo: refactor (implement Results() etc.)
        function = tuple(x for x in all_fns if 'failure' in x.__name__)[0]
        # results = dict()

        print(f'\nTESTING: {function.__name__.upper()}')
        failures = 0
        for ff_test in tests:
            inp = ff_test.input_data
            out = ff_test.expected
            try:
                assert [i[1] for i in function(inp)] == out
                print(ff_test, 'PASS')
            except AssertionError:
                print(ff_test, 'FAIL')
                failures += 1
        print(f'\n{function.__name__.upper()} FAILED {failures} TESTS!\n')

    @staticmethod
    def run_all_testcases_on_fn(function, tests: list[TestCase]):  # todo: function and return typing
        data = dict()                                              # todo: Callable[str, str] causes error
        fail_counter = 0

        for test in tests:
            try:
                out = function(test.pattern, test.text)
                assert out == test.match_index
                data[test] = (True, out)
            except AssertionError:
                fail_counter += 1
                data[test] = (False, out)
            except Exception as e:
                print(type(e), str(test), sep='\n')

        return fail_counter, data

    @staticmethod
    def display_results():
        pass

    def time_complexity_tests(self):
        pass

    def run_all(self):
        pass

    @staticmethod
    def run_perfect_hash_test(tests):
        data = list()
        fail_counter = 0
        lookup = _get_alphabet()

        for test in tests:
            datum = Results(test.input_data)
            datum.result = _hash(test.input_data, lookup)
            try:
                assert datum.result == test.expected
                datum.passed = True
            except AssertionError:
                fail_counter += 1
                datum.passed = False
            data.append(datum)

        return data


testing = Testing()
# testing.run_failure_function_tests()
# testing.run_substring_matching_tests()
# testing.run_all()

test_fns = tuple(f for f in all_fns if f.__name__[0] != '_' and 'NAIVE' not in f.__name__)
test_fns = tuple(f for f in test_fns if "boyer" in f.__name__)
test_cases = correctness_test_cases

red, green = 91, 92
color = lambda color, obj: str(f'\x1b[{str(color)}m' + str(obj) + '\x1b[0m')  # noqa

summary = dict()
for test_fn in test_fns:
    test_fn = test_fn
    fn_name = test_fn.__name__.upper()

    results = testing.run_all_testcases_on_fn(test_fn, test_cases)
    summary[fn_name] = results[:]
    fail_count = results[0]
    results = results[1]
    max_len = 4 + max([len(str(x)) for x in results])

    print(f'\nTESTING: {fn_name}')
    for test_case, output in tuple(results.items()):
        result = 'PASS' + str(output[1]) if output[0] else 'FAIL'
        output = color(red, output) if not output[0] else str(output)
        result += output
        print(f"{str(test_case):{max_len}}{output}")
    fail_txt = f"{color(red, 'FAIL ' + str(fail_count))}"
    pass_txt = f"{color(green, f'PASS ' + str(len(results) - fail_count))}"
    print(f"{fn_name:>{max_len - 1}} {pass_txt} | {fail_txt}")

# for i in range(101):
#     print(i, str(f'\x1b[{str(i)}m' + 'ABCDEF' + '\x1b[0m'))

# todo: include easily viewable summary

# ff_data = testing.run_failure_function_tests(failure_function_tests)
# print(ff_data)

hash_fn_data = testing.run_perfect_hash_test(perfect_hash_tests)
print(hash_fn_data)

# for fn, data_tup in summary.items():
#     print('asdf', fn)
#     if data_tup[0] > 0:
#         for data in data_tup[1].items():
#             if not data[1][0]:
#                 print(data)


# move
# if __name__ == "__main__":
