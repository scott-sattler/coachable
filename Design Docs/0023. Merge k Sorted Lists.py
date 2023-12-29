from typing import List, Optional
import heapq
import queue


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next_ = next_

    def __lt__(self, other): return self.val < other.val
    def __le__(self, other): return self.val <= other.val
    # def __eq__(self, other): return self.val == other.val
    # def __ne__(self, other): return self.val != other.val
    # def __gt__(self, other): return self.val > other.val
    # def __ge__(self, other): return self.val >= other.val


class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def mergeKLists_heapq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merged list
        merged_head_dummy = ListNode()
        merged_pointer = merged_head_dummy

        minheap = list()

        for head in lists:
            if head is None:  # LeetCode Imposed
                continue      # LeetCode Imposed
            minheap.append(head)
        heapq.heapify(minheap)

        while len(minheap) > 0:
            # get the next smallest element and update minheap
            if minheap[0].next_ is None:
                next_element = heapq.heappop(minheap)
            else:
                next_element = heapq.heapreplace(minheap, minheap[0].next_)

            # add next smallest element to the merged (sorted) list
            merged_pointer.next_ = next_element
            merged_pointer = merged_pointer.next_

        return merged_head_dummy.next_

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def mergeKLists_pq(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merged list
        merged_head_dummy = ListNode()
        merged_pointer = merged_head_dummy

        # data structure used to find
        # the smallest head in k lists
        pq = queue.PriorityQueue()

        # add each head to pq
        for head in lists:
            pq.put(head)

        while not pq.empty():
            # get the next smallest element
            next_element = pq.get()
            if next_element is None:
                continue

            # update the pq
            if next_element.next_:
                pq.put(next_element.next_)

            # add next smallest to the merged/sorted list
            merged_pointer.next_ = next_element
            merged_pointer = merged_pointer.next_

        return merged_head_dummy.next_


if __name__ == '__main__':
    import helper_functions as hf

    def create_ll_from_list(lst: list) -> ListNode:
        dummy_head = ListNode()
        list_pointer = dummy_head
        for el in lst:
            list_pointer.next_ = ListNode(el)
            list_pointer = list_pointer.next_
        return dummy_head.next_

    def create_list_of_ll(lst_of_lls: list[list]) -> list[ListNode]:
        ret: list[ListNode] = list()
        for each in lst_of_lls:
            ret.append(create_ll_from_list(each))
        return ret

    def create_list_from_ll(ll: ListNode) -> list:
        ret = list()
        while ll:
            ret.append(ll.val)
            ll = ll.next_
        return ret


    class TestCase:
        def __init__(self, input_: list[list], expected: list):
            self.raw_input = input_
            self.input_ = create_list_of_ll(input_)
            self.expected = expected


    class Testing(TestCase):
        tests = [
            (
                [],
                []
            ),
            (
                [[]],
                []
            ),
            (
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [i for i in range(1, 10)]
            ),
            (
                [[3, 3, 3], [2, 2, 2], [1, 1, 1]],
                [1, 1, 1, 2, 2, 2, 3, 3, 3]
            ),
            (
                [[2, 6, 8], [1, 4, 9], [3, 5, 7]],
                [i for i in range(1, 10)]
            ),
            (
                [[1, 2, 3, 4]],
                [1, 2, 3, 4]
            ),
        ]

        # noinspection PyMissingConstructor
        def __init__(self, test_fns):
            self.functions = test_fns
            self.test_cases = None

        def load_test_cases(self):
            self.test_cases = list()
            for test in self.tests:
                self.test_cases.append(TestCase(test[0], test[1]))

        def run(self):
            for fn in self.functions:
                self.load_test_cases()
                print(hf.color('yellow', f'FUNCTION TEST: {fn}'))
                for test in self.test_cases:
                    actual = self.functions[fn](self, test.input_)
                    actual_list = create_list_from_ll(actual)
                    try:
                        assert actual_list == test.expected
                        result = hf.color('green', 'PASS')
                    except (Exception,):
                        result = hf.color('red', 'FAIL')
                    print(f"test: {result}\n{test.raw_input}\n"
                          f"expected:\n{test.expected}\n"
                          f"actual:\n{actual_list}\n")


    fns = {k: v for k, v in Solution.__dict__.items() if 'mergeKLists' in k}
    print(fns)
    t = Testing(fns)
    t.run()
