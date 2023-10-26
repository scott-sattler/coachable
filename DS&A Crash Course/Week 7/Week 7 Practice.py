"""
Dynamic Programming
Free Response Questions
    1. Describe dynamic programming.
        an optimization technique that, when applicable, breaks a more complex problem into simpler subproblems, finds
        solutions to those simpler subproblems, which are then used to solve a larger, more complex problems.
        i.e. an optimization that utilizes optimal substructure to solve problems

    2. When should you use dynamic programming? What types of problems where you should consider dynamic programming as
    a possible solution?
        when other approaches are too inefficient
        question is asking for a total of something
        min/max sum/product
        repeatedly solving subproblem(s)

        subproblems with substrings
        subproblems of 1d/2d arrays are subarrays
        binary trees with subproblems solution to each subtree

    3. What is the difference between top-down and bottom-up dynamic programming?
        top down: assume the subproblems
        bottom up: compose the subproblems

        top down typically uses memoization with a naive recursive solution,
        while bottom up typically uses an iterative approach, with tabulation.

        bottom up solutions usually order the solutions by "size", solving the "smaller" subproblems first.
        bottom up often has a superior constant factor, from lower overhead


    4. “Memoization” can be thought of as “caching” all the recursive calls that have already happened. What might be a
    reason why I wouldn’t want to do that?
        repeated calls with the same arguments are impossible, unlikely, or are avoidable.

    5. Oftentimes, the answer  f(n) may only require the result from f(n-1) and f(n-2). What kind of space/memory
    optimization can we do if this is the case? If it helps, you can give an example of a specific problem.
        only store the results for previous calls that are going to be reused

    6. What if we had a f(r, c) that relied only on f(r-1, c) for some arbitrary c? What kind of space/memory
    optimization can we do if this is the case? If it helps, you can give an example of a specific problem.
        only cache f(r-1, c), with each new r value overwriting the previous data

    7. Fibonacci is one example of a 1-dimensional recurrence relation optimized with dynamic programming. Identify and
    share 3 other classes of dynamic programming problems that seem similar and describe what makes them feel similar.
        todo

    8. Is this statement true or false?
    "Dynamic programming only helps problems that have a brute-force recursive solution."
        false. todo, explain


Dynamic Programming and Recurrence Examples
    Each of the below problems can be solved with recursion. Please  answer the following for each one.
    1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)

    2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by giving a
    qualitative explanation in plain English.

    3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6).

    4. Top-Down Approach. Compute a small example using a top-down approach with memoization (n = 6, m = 6).

    5. Complexity Analysis. Identify the optimal runtime and space complexity.

    6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

Problems That Can Be Solved with Recursion
    1. Number of paths up a staircase of length N where you take 1 or 2 steps each time. Example provided.
        1. N -> paths: 1 -> 1, 2 -> 2, 3 -> 3, 4 -> 5
        2. f(n) = f(n - 1) + f(n - 2). We can either take 1 or 2 steps towards reaching our goal.
        3. f(n) = table[i - 1] + table[i - 2]
           f(1) = 1, f(2) = 2
           [0, 0, 0, 0, 0, 0]
           [1, 2, 0, 0, 0, 0]
           [1, 2, 3, 0, 0, 0]
           [1, 2, 3, 5, 0, 0]
           [1, 2, 3, 5, 8, 0]
           [1, 2, 3, 5, 8, 13]
        4. call stack:
           f(1) = 1                   # base case or stored in memo upon creation
           f(2) = 2                   # base case or stored in memo upon creation
           f(3) = f(2) + f(1) = 3     # f(3) stored in memo
           f(4) = f(3) + f(2) = 5     # f(4) stored in memo
           f(5) = f(4) + f(3) = 8     # f(5) stored in memo
           f(6) = f(5) + f(4) = 13    # f(6) stored in memo
        5. recursive: O(n) time; O(1) input space; O(n) memo space; O(n) call stack space
           iterative: O(n) time; O(1) input space; O(n) table space
           optimized: O(n) time; O(1) input space; O(1) space to store the previous two results
        6. Yes; Versus bottom-up optimized, the recursive approach recomputes function calls, with a call stack space of
        O(n). todo reword/fix

    2. Computing the number of permutations of [1-n] i.e. [1,2,3,4,5,...n-1,n].
        1. n -> permutations: 0 -> 1, 1 -> 1, 2 -> 2, 3 -> 6, 4 -> 24
        2. f(n) = n * f(n - 1). We can choose n objects, then (n - 1) objects, and (n - 2) objects until we can choose
        one object. Each choice is followed by (n - 1) choices (multiplication).
        3. f(0) = 1, f(1) = 1
           [1, 0, 0, 0, 0, 0]
           [1, 2, 0, 0, 0, 0]
           [1, 2, 3, 0, 0, 0]
           [1, 2, 3, 5, 0, 0]
           [1, 2, 3, 5, 8, 0]
           [1, 2, 3, 5, 8, 16]
        4. call stack:
           f(1) = 1                # base case or stored in memo upon creation
           f(2) = 2                # base case or stored in memo upon creation
           f(3) = 3 * f(2) = 3     # f(3) stored in memo
           f(4) = 4 * f(3) = 5     # f(4) stored in memo
           f(5) = 5 * f(4) = 8     # f(5) stored in memo
           f(6) = 6 * f(5) = 16    # f(6) stored in memo
        5. recursive: todo
           iterative: todo
           optimized: todo
        6. Yes.  todo

    3. Unique Paths: The number of paths from the top left corner of a grid to the bottom right corner when moving only
    down and to the right.
        1. (n, m) -> paths: (0, 0) -> 0, (1, 1) -> 2, (2, 2) -> 2, (3, 3) -> 6
        2. recurrence relation: f(n, m) = f(n - 1, m) + f(n, m - 1); base case: f(n, m) = (0, 0) (or (n, m) if starting
        from (0, 0)). We can move either right or down. From any given position, the number of paths is the number of
        paths moving right, plus the number of paths moving down.
        3. add up and left to get current
           topmost and leftmost only ever have a single path
           [0, 1, 1]
           [1, 2, 3]
           [1, 3, 6]

           [  0,  1,  1,  1,   1,   1]
           [  1,  2,  3,  4,   5,   6]
           [  1,  3,  6, 10,  15,  21]
           [  1,  4, 10, 20,  35,  56]
           [  1,  5, 15, 35,  70, 126]
           [  1,  6, 21, 56, 126, 252]
        4. call stack:
           f(1, 1) = 1
           f(1, 2) = 1
           f(1, 3) = 1
           f(2, 1) = 1
           f(2, 2) = 2
           f(2, 3) = 3
           f(3, 1) = 1
           f(3, 2) = 3
           f(3, 3) = 6

        5. recursive: O(n * m) time; O(1) input space; O(n * m) memo space; O(n + m) call stack;
           iterative: O(n * m) time; O(1) input space; O(n * m) table space;
           optimized: O(n * m) time; O(1) input space; O(m) table space, where m = [int] * rows
        6. Yes.  todo use this format elsewhere?
           Optimized runtime reduces time complexity from O(2^n) to O(n^2);
           Optimized tabulation reduces space from O(n + m) (call stack), to O(m) table space, where m = [int] * rows

    4. Given a 2xN grid, how many different ways can you fill the gird with 2x1 dominoes?
        1.
        2.
        3.
        4.
        5.
        6.

    5. Given a 3xN grid, how many different ways can you fill the gird with 3x1 dominoes?
        1.
        2.
        3.
        4.
        5.
        6.

    6. Given a set A = {1,2,3,...,N} calculate the number of possible subsets of A.
        1. A(size) -> subsets: 0 -> 1, 1 -> 2, 2 -> 4, 3 -> 8
        2. recurrence relation: f(n) = f(n - 1) + f(n - 1); base case: f(0) = 1. We can either include an element, or
        not, for every element in n elements.
        3. f(n) = table_i[2 ^ i] or f(n) = table_i[(i - 1) * 2]
           [1, 2, 4, 8, 16, 32, 64]
        4. call stack:
           f(0) = 1
           f(1) = 2
           f(2) = 4
           f(3) = 8
           f(4) = 16
           f(5) = 32
           f(6) = 64
        5. recursive: O(n) time; O(1) input space; O(n) call stack space; O(n) memo space
           iterative: O(n) time; O(1) input space; O(n) space keeping n array, O(1) space if just keeping last element
        6. Yes. A naive recursive approach takes O(2^n) time, and O(n) space.

    7. Given a set A = {1,2,3,...,N} calculate the number of possible subsets of A that do not contain any 2 numbers
    that are 1 apart. For example, {1,2,4}  would not be valid because 1 and 2 are 1 apart.
        1. A(size) -> subsets: 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 5
        2. recurrence relation: f(n) = f(n - 2) + f(n - 1); base case: f(0) = 1, f(1) = 0. We can either include an
        element, in which case we shift by two, or we can not, in which case we shift by one, for every element in n
        elements.
        3. starting with an empty set, {}, iterating over A, loop through a queue
           # nonconsecutive iterative
           def iter_sets(n):
               elements = [i for i in range(1, n + 1)]
               sets = []
               agenda = [[]]  # seed
               while agenda:
                   next_elem = agenda.pop(0)
                   if next_elem not in sets:
                       sets.append(next_elem)  # not included
                   for elem in elements:  # included
                       next_set = next_elem + [elem]
                       if len(next_elem) < 1 or elem > next_elem[-1] + 1:
                           sets.append(next_set)
                           agenda.append(next_set)
               return n, len(sets), sets  # list notation tho

           {
               {},
               {1},
               {2},
               {3},
               {4},
               {5},
               {6},
               {1, 3},
               {1, 4},
               {1, 5},
               {1, 6},
               {2, 4},
               {2, 5},
               {2, 6},
               {3, 5},
               {3, 6},
               {4, 6},
               {1, 3, 5},
               {1, 3, 6},
               {1, 4, 6},
               {2, 4, 6}
           }

        4. # nonconsecutive recursive
           # while this tracks the sets themselves, cardinality does not require the sets themselves
           def nc_subsets(n):
               if n < 1:
                   return n, 1, {}
               subsets = []
               _subsets(3, [1], n, subsets) + _subsets(2, [], n, subsets)
               count = len(subsets)
               subsets = ''.join(['{' if i == '[' else '}' if i == ']' else i for i in str(subsets)])  # otherwise use frozensets
               return n, count, subsets

           def _subsets(index, par_set, n, subsets):
               if index > n:
                   subsets.append(par_set)
                   return 1
               return _subsets(index + 2, par_set + [index], n, subsets) + _subsets(index + 1, par_set, n, subsets)
            
           call stack:
           {
               {1, 3, 5},
               {1, 3, 6},
               {1, 3},
               {1, 4, 6},
               {1, 4},
               {1, 5},
               {1, 6},
               {1},
               {2, 4, 6},
               {2, 4},
               {2, 5},
               {2, 6},
               {2},
               {3, 5},
               {3, 6},
               {3},
               {4, 6},
               {4},
               {5},
               {6},
               {}
           }
        5. DP optimal time/space: O(n) time complexity using memoization; O(n) space complexity using memoization
        6. Yes. A naive recursive approach takes O(2^n) time, and O(n) space.

    8. Count the number of functions from {1,2,3,...,N} to a set of size {1,2,3,...,M}. Here is an additional
    explanation of functions.
        1.
        2.
        3.
        4.
        5.
        6.

    9. A function has a fixed point if f(x) = x for any x in the domain of f. How many functions are there from
    {1,2,3,...,N} to {1,2,3,...,M} without any fixed points? Hint, approach the problem in cases, then put it all
    together.
        a. Case 1: Assume that M=N

        b. Case 2: Assume that  N <= M

        c. Case 3: Assume that N > M

        d. Combine Cases 1-3 to get a general recurrence.

    10. Let's say a function is reducing if f(x) <= x for all x in the domain of f. How many reducing functions are
    there from  {1,2,3,...,N} to {1,2,3,...,M}?
        a. Case 1: Assume that M=N

        b. Case 2: Assume that  N <= M

        c. Case 3: Assume that N > M

        d. Combine Cases 1-3 to get a general recurrence.

Fibonacci Example (Problem 1):

    1. f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5

    2. f(n) = f(n-1) + f(n-2) This is because to get to step n you can get there by taking 1 step from n-1 or 2 steps
    from n-2 . Therefore, the number of paths to n is the total number of paths from n-1 plus the number of paths from
    n-2.

    3. f(0) = 1, f(1) = 1, f(2) = 2
       f(3) = f(2) + f(1) = 3
       f(4) = f(3) + f(2) = 5
       f(5) = f(4) + f(3) = 8
       f(6) = f(5) + f(4) = 13

    4. This shows the call stack.
    The bottom call `f(2)` is completed first.

    f(6) = f(5) + f(4) = 13 #f(6)=13 is stored in the memoization.
    f(5) = f(4) + f(3) = 8  #f(5)=8 is stored in the memoization.
    f(4) = f(3) + f(2) = 5  #f(4)=5 is stored in the memoization.
    f(3) = f(2) + f(1) = 3  #f(3)=3 is stored in the memoization.
    f(2) = f(1) + f(0) = 2  #f(2)=2 is stored in the memoization.

    5. Runtime is O(n) and space O(1) if we only cache the previous 2 elements.

    6. Yes. If we used plain recursion, the runtime would be exponential. Dynamic programming gets us an O(n) runtime.

OPTIONAL: Recursive Challenge Problems
    The following are very tough and completely optional.
    Hint: For these, you can assume the distinct integers are 1,2,3,...,N Moreover, 8-11 are very tricky, so don't
    hesitate to utilize external references. However, make sure you understand how they arrived at those solutions.
    1. Given a 4xN grid, how many different ways can you fill the grid with 2x1 dominoes?
        1.
        2.
        3.
        4.
        5.
        6.

    2. How many binary trees can you create with N distinct integers? Assume N=2^n-1 i.e. so N is the number of elements
    in a complete binary tree.
        1.
        2.
        3.
        4.
        5.
        6.

    3. How many binary search trees can you create with N=2^n-1 distinct integers?
        1.
        2.
        3.
        4.
        5.
        6.

    4. How many distinct binary heaps can you  create with N=2^n-1 distinct integers?
        1.
        2.
        3.
        4.
        5.
        6.

    5. We say a binary tree is level-sorted if every element is larger than every element in a lower level (even if they
    are in different subtrees).  Note all level-sorted trees are also heaps, but not all heaps are level-sorted. Notice
    that BInary Tree A below is a heap but NOT level-sorted since (6) is larger than 4 but is at a lower level in the
    tree.

    Binary Tree A
          9
         / \
        4   8
       / \ / \
      1  2 6  7

    How many binary trees can you create with N=2^n-1 distinct integers that are level sorted?
        1.
        2.
        3.
        4.
        5.
        6.

Challenge: Now solve 8-11 without assuming N=2^n-1
    todo

"""