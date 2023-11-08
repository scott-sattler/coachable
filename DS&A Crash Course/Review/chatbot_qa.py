def topological_sort():
    """
    Q: topological_sort
    Can you explain the process of obtaining a topological sort of a directed acyclic graph (DAG)? Please provide a brief
    explanation of how you would implement it.

    A:
    Topological sort is an order that requires predecessors (parents) come before their successors (children). Create two
    dictionaries containing each node's in-degrees and out degrees. Use either a stack or queue to track all nodes with zero
    in-degrees. While this stack/queue contains elements, decrement the respective children, and if those children end up
    with zero in-degrees, add them to the stack/queue. You will know you've obtained a Topological sort (i.e. if it's
    possible) when all elements in the out-degree dictionary are contained within the sorted list.
    """


def bfs_vs_dfs():
    """
    Q: bfs_vs_dfs
    Can you explain the fundamental differences between Breadth-First Search (BFS) and Depth-First Search (DFS) in graph
    traversal? How would you choose between them for a particular problem?

    A:
    BFS visits all children at a given level (depth, or distance from root node) before moving to deeper nodes. While DFS
    visits the children of children until no children remain, then goes to the next child of the first child.

    For problems where you want to traverse or search more near to the current node, you use BFS, and conversely, if
    distance or depth from the current node is desired, DFS.

    Recursive DFS is easier to implement than BFS.
    Data structures stored in a list are easily traversed with BFS (just increment the index).
    DFS - backtracking

    R:
    ...
    BFS is generally used when we want to find the shortest path (in terms of the number of edges) between two nodes in an
    unweighted graph, while DFS can be used in scenarios like topological sorting, detecting a cycle, path finding, etc.
    """


def dp_big_o_fibonacci():
    """
    Q: dp_big_o_fibonacci
    Can you analyze the following recursive Fibonacci function and describe the time and space complexity? Can you propose
    an optimization using dynamic programming?

    def fibonacci(n: int) -> int:
      if n == 0 or n == 1:
        return n
      return fibonacci(n-1) + fibonacci(n-2)

    A:
    O(2^n) time complexity; O(1) input space complexity; O(n) call stack space; for O(n) auxiliary space complexity.

    DO Optimization: ache the functions calls in a memo (hash map), and have each call check the hash map for previously
    computed calls. O(n) time complexity; O(2n) -> O(n) auxiliary space complexity

    O(n) time complexity; O(1) input space complexity; O(n) call stack space; O(n) for memo space; for O(2n) -> O(n)
    auxiliary space complexity.

    R:
    ...
    Optimizing with dynamic programming, as you said, involves storing previously calculated values in a memoization table
    (or simply an array) to avoid redundant calculations. This reduces the time complexity to linear, O(n), as each
    Fibonacci number is calculated only once.

    The space complexity in this case would be O(n) for the memo table plus the O(n) for the recursion stack, but if we use
    iterative dynamic programming, we can reduce the space complexity to O(1) by keeping track of only the last two
    Fibonacci numbers. This is because to get the next Fibonacci number, we only need the last two.

    Here is the code:

    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
    """


def dp_big_o_fibonacci_followup():
    """
    4. Q: dp_big_o_fibonacci_followup
    Given a function that iteratively calculates the nth Fibonacci number, explain how you can optimize the space
    complexity.

    A:
    Only keep track of the previous two results. (I knew this, but forgot. It's easy to remember when coding.)
    """


def dp_dominos_2xM():
    """
    5. Q: dp_dominos_2xM
    You are given a task to tile a 2 x M board with 1 x 2 tiles without overlap. Can you derive the recurrence relation for
    the number of ways to tile the board?

    A:
    f(n) = f(n - 1) + f(n - 2)

    This recurrence relation is obtained by understanding that for each additional space, the number of arrangements can be
    found by adding one (vertical) tile and two (horizontal) tiles to the left of existing arrangements.
    """


def big_o():
    """
    6. Q: big_o
    Please analyze the time complexity of the following code snippets:

    def fn_x(N: int):
      for i in range(N):
        for j in range(N):
          # do something

    def fn_y(N: int):
      i = 0
      while i < N:
        i *= 2
        # do something

    A:
    fn_x(N) -> O(N^2)
    fn_y(N) -> O(log N)
    """

def divide_and_conquer_mergesort_solving_recurrence_relations():
    """
    Q: divide_and_conquer_mergesort_solving_recurrence_relations
    Describe the divide-and-conquer approach used in the mergesort algorithm and derive the recurrence relation for its
    runtime complexity.

    A:
    Divide and conquer divides larger problems into smaller subproblems, solves those subproblems, then combines (or
    otherwise uses) these subproblems to solve the larger problem.

    In the context of mergesort, an array is divided in half until no further divisions are possible (len = 1), then takes
    two sorted subarrays (a len of 1 array is sorted), compares/sorts them, in a combined larger subarray of their combined
    size. This process is continued for every subdivision until the final comparison results in a sorted array.

    The time complexity for this process is found by understanding that each element is looked at n times, each depth level
    (each half division), which is a depth of log_2 n, for O(n * log n) time complexity.

    R:
    better explanation: https://courses.cs.duke.edu/fall17/compsci330/lecture2note.pdf
    In the merge sort algorithm, the divide step recursively breaks down the problem into two or more sub-problems until
    they become simple enough to be solved directly. In this case, it divides the array in half until we have sub-arrays of
    size 1.

    The conquer step solves the sub-problems by merging these sorted sub-arrays to give the sorted array.

    The runtime complexity of merge sort can be represented by the recurrence relation T(n) = 2T(n/2) + n. This arises
    because in each recursive call, we break our array of size n into two arrays of size n/2 and spend O(n) time to merge
    the two sorted halves into a sorted array.

    Solving this recurrence relation gives us a time complexity of O(n log n), which is optimal for a comparison-based
    sorting algorithm.
    """


def bad_question_sorting_stability():
    """
    Q: bad_question_sorting_stability
    You are given a list of pairs (value, label) and are required to sort the pairs only by value using a comparison-based
    sorting algorithm. If there are two pairs with the same value, their relative order is undefined. Can you implement such
    a sort, and what algorithm would be best suited for this task?

    A:
    Yes. Any in-place O(N log N) sorting algorithm. The selection of the sort isn't as important as pointing the comparison
    to the value. ... ?

    R:
    However, in this case, where the relative order of equal items does not matter (i.e., stability is not required), you
    could use an unstable sorting algorithm like heapsort or quicksort. These algorithms offer a good average-case
    performance of O(n log n).

    """


def count_pairs_that_sum():
    """
    Q: count_pairs_that_sum
    Given an array of integers, write a function that returns the number of pairs that sum to a target value. Which
    algorithm will achieve the best time complexity?

    A. O(n log n) by sorting the array
    B. O(n^2) by using nested loops
    C. O(n) by using a hash set
    D. O(log n) by using binary search

    A:
    C.
    [overly complicated algo]

    R:
    Yes, you're correct! Using a hash set or hash map is indeed the optimal solution to this problem, achieving a time
    complexity of O(n), as it allows us to find the complement of a given number in constant time.

    However, the solution provided seems a bit complicated. You could simplify it as follows:

    def count_pairs(target_sum, arr):
        count = 0
        hashmap = dict()

        for num in arr:
            diff = target_sum - num
            if diff in hashmap:
                count += 1
            hashmap[num] = True

        return count

    In this code, for each number in the array, we calculate the difference needed to reach the target sum. If that
    difference is found in our hashmap, it means we've found a pair that sums up to the target, and we increment our count.
    We then add the current number to our hashmap so it can be paired up with future elements in the array.

    This approach works because each pair is only counted once. When we find a pair that sums to the target, we increment
    the count immediately, but we don't remove the elements from our hashmap, so they can still form valid pairs with other
    elements later in the array.
    """


def heap_min():
    """
    Q: heap_min
    If you insert the elements [15, 12, 18, 5, 10] into an empty min-heap, what will be the list representation of the heap?

    A:
    [5, 10, 18, 15, 12]
    """


def big_o_time_and_space_fibonacci():
    """
    Q: big_o_time_and_space_fibonacci
    Consider the following recursive algorithm that computes the nth Fibonacci number:

    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    What is the time and space complexity of this code?

    A:
    O(2^n) time complexity, with O(n) call stack space complexity

    """



'''
def ():
"""
Q: 
Given the following binary tree, perform an Inorder traversal and provide the sequence of values:

     A
   /   \
  B     C
 / \   /
D   E F

A:

"""


def ():
"""
Q:

A:

"""


def ():
"""
Q:

A:

"""


def ():
"""
Q:

A:

"""


def ():
"""
Q:

A:

"""


def ():
"""
Q:

A:

"""


def ():
"""
Q:

A:

"""





'''