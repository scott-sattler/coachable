"""
Dynamic Programming

Free Response Questions

    1. Describe dynamic programming.
        an efficient way of solving problems by identifying, solving, and storing subproblems. where subproblems can
        typically be solved similarly, and are less complex

    2. When should you use dynamic programming? What types of problems where you should consider dynamic programming as
    a possible solution?
        problem can be solved via overlapping subproblems (e.g. substrings, subarrays, subtrees)
        poor time complexity of recursive solution
        ...
        when solutions to subproblems can be used to solve larger problems
        optimal substructure (optimal solution can be constructed from optimal solutions to subproblems)

    3. What is the difference between top-down and bottom-up dynamic programming?
        bottom-up solves the base case, and increases size of subproblem
            typically requires iteration
        top-down solves more 'naturally', and decreases size of subproblem
            typically requires recursion

    4. “Memoization” can be thought of as “caching” all the recursive calls that have already happened. What might be a
    reason why I wouldn’t want to do that?
        the data is not useful, or unnecessary
        no subproblem overlap or optimal substructure
        i.e. subprolbems are not useful in solving larger problems

    5. Oftentimes, the answer  f(n) may only require the result from f(n-1). What kind of space/memory optimization can
    we do if this is the case? If it helps, you can give an example of a specific problem.
        * no response to inquiry *
        memoization/tabulation

    6. What if we had a f(r, c) that relied only on f(r-1, c) for some arbitrary c? What kind of space/memory
    optimization can we do if this is the case? If it helps, you can give an example of a specific problem.
        * no response to inquiry *
        memoization/tabulation

    7. Fibonacci is one example of a 1-dimensional recurrence relation optimized with dynamic programming. Identify and
    share 3 other classes of dynamic programming problems that seem similar and describe what makes them feel similar.
        strings: (e.g.) min/max subsequences
        matrices: (e.g.) min/max paths; 2D combinations
        counting: (e.g.) knapsack problem; coin change problem

        optimization min/max graphs
        optimization min/max strings
        target combination/permutation

    8. Is this statement true or false?
    "Dynamic programming only helps problems that have a brute-force recursive solution."
        false

Dynamic Programming and Recurrence Examples
    Each of the below problems can be solved with recursion. Please answer the following for each one.
    1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
    2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by giving a
    qualitative explanation in plain English.
    3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
    4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
    5. Complexity Analysis. Identify the optimal runtime and space complexity.
    6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

Problems That Can Be Solved with Recursion

    1. Number of paths up a staircase of length N where you take 1 or 2 steps each time. Example provided.
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
            0 stairs 0 solutions; 1 1; 2 2; 3 3

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.
            value: F(n) = F(n - 1) + F(n - 2); if remaining_stairs == 0: return 1
                base case with boundary control: if n < 1: return 1 * (n + 1))
            recurrence: at each step, you can choose either 1 or two steps. the recursive stack acts as tree nodes
            base case: when no choices can be made (no stairs remain), you count a unique outcome

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
            13; algorithm at bottom below
            [[2, 2, 1, 1], [2, 2, 2], [2, 1, 2, 1], [2, 1, 1, 1, 1], [2, 1, 1, 2],
            [1, 2, 2, 1], [1, 2, 1, 1, 1], [1, 2, 1, 2], [1, 1, 2, 1, 1], [1, 1, 2, 2],
            [1, 1, 1, 2, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2]]

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
            13; algorithm at bottom below
            the memo is still created in a 'bottom up' fashion
                the callstack contains a stack of references with the base case at the top, hence, 'bottom up'

        5. Complexity Analysis. Identify the optimal runtime and space complexity.
            optimal run/space, Ω(n), is the closed form with Ω(n) time-complexity and Ω(1) auxiliary space
            DP: O(n) runtime; O(n + n) -> O(n) aux space (callstack + memo)
            naive recursive: O(2^n) runtime; O(n) aux space (callstack)

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?
            yes; yes. DP incurs a space penalty vs naive recursion

    2. Computing the number of permutations of [1-n] i.e. [1,2,3,4,5,...n-1,n]
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
            there are n! permutations of n elements
            0 -> 1; 1 1; 2 2; 3 6; 4 24

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.
            value: F(n) = n * F(n - 1); if n == 0: return 1
            recurrence: the 1st element can be in (n - 0) positions, the 2nd element (n - 1) positions, 3rd (n - 2)...
                        each element can take each position, the number of ways all other elements can be dif. ordered
                        while it is in that position
                        [1, 2, 3, 4], [1, 3, 2, 4], ...
            base case: factorials cannot be negative (cannot have negative orderings); 0 elements contain 1 ordering

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
            720; [1, 1, 2, 6... ]; algorithm at bottom below

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
            720; [6, 30, 120, 360, ...]; algorithm at bottom below

        5. Complexity Analysis. Identify the optimal runtime and space complexity.
            optimal run/space, Ω(n), is the closed form n! with (Ω(1) or Ω(n)) time-complexity and Ω(1) auxiliary space
                Ω(1) vs Ω(n) depends on multiplication implementation
            DP memo: O(n) runtime; O(n + n) -> O(n) aux space (callstack + memo)
            DP table: O(n) runtime; O(1) -> O(1) aux space (optimized table; O(n) unoptimized table)
            naive recursive: O(n); O(n)

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?
            not really (?), optimized tabulation saves space; asymptotically identical, practically, probably worse (?)

    3. Unique Paths: The number of paths from the top left corner of a grid to the bottom right corner when moving only
    down and to the right.
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
            using [n - 1][m - 1] grid:
            0 0, 0; 1 1, 1; 2 2, 2; 3 3, 6

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.
            value: F(n, m) = F(n - 1, m) + F(n, m - 1); if (n, m) == (0, 0): return 1
            recurrence: each square (n, m) is the sum of paths that lead to it, with a choice of down or right
            base case: reaching the square (0, 0) indicates a unique path has been found

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
            using [n - 1][m - 1] grid:
            252; algorithm at bottom below

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
            using [n - 1][m - 1] grid:
            252; algorithm at bottom below

        5. Complexity Analysis. Identify the optimal runtime and space complexity.
            optimal run/space, Ω(n), is the closed form ? with Ω(?) time-complexity and Ω(?) auxiliary space
            DP memo: O(n * m) runtime; O(n * m) aux space
            DP table: O(n * m) runtime; O(n) aux space (optimized); O(n*m) (unoptimized)
            naive recursive: O(2 ^ (n + m)) runtime; O(n + m) aux space (callstack)

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?
            yes; yes.


    4. Given a 2xN grid, how many different ways can you fill the gird with 2x1 dominoes?
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)

        5. Complexity Analysis. Identify the optimal runtime and space complexity.

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

    5. Given a set A = {1,2,3,...,N} calculate the number of possible subsets of A.
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
            there are 2^n subsets within a set
            0 -> 1; 1 2; 2 4; 3 9; 4 16

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.


        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)

        5. Complexity Analysis. Identify the optimal runtime and space complexity.

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

    6. Count the number of functions from {1,2,3,...,N} to a set of size {1,2,3,...,M}. Here is an additional
    explanation of functions.
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)

        5. Complexity Analysis. Identify the optimal runtime and space complexity.

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

    7. Extension of problem 6. A function has a fixed point if f(x) = x for any x in the domain of f . How many
    functions are there from {1,2,3,...,N} to {1,2,3,...,M} without any fixed points?
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)

        5. Complexity Analysis. Identify the optimal runtime and space complexity.

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

    8. Given a 4xN grid, how many different ways can you fill the grid with 2x1 dominoes?
        1. Unit Tests. Identify the solution cases up to n = 4. For 2D, do all cases up to (3,3)
            0 1; 1 1; 2 5; 3 11; 4 36

        2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by
        giving a qualitative explanation in plain English.

        3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

        4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)

        5. Complexity Analysis. Identify the optimal runtime and space complexity.

        6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?


OPTIONAL: Binary Tree Recursive Challenge Problems

    Hint: For these, you can assume the distinct integers are 1,2,3,...,N Moreover, 8-11 are very tricky, so don't
    hesitate to Google more references for those ones. However, make sure you understand how they arrived at those
    solutions.
    
    These ones are very tough and completely optional.
    
    1. How many binary trees can you create with N distinct integers? Assume N=2^n-1 i.e. so N is the number of elements
    in a complete binary tree.
    
    2. How many binary search trees can you create with N=2^n-1 distinct integers?
    
    3. How many distinct binary heaps can you  create with N=2^n-1 distinct integers?
    
    4. We say a binary tree is level-sorted if every element is larger than every element in a lower level (even if they
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
    
    Challenge: Now solve 8-11 without assuming N=2^
    
    Fibonacci Example
    
    1. f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5
    
    2. f(n) = f(n-1) + f(n-2) This is because to get to step n you can get there by taking 1 step from n-1 or 2 steps
    from n-2 . Therefore the number of paths to n is the total number of paths from n-1 plus the number of paths from
    n-2
    
    f(0) = 1, f(1) = 1, f(2) = 2
    f(3) = f(2) + f(1) = 3
    f(4) = f(3) + f(2) = 5
    f(5) = f(4) + f(3) = 8
    f(6) = f(5) + f(4) = 13
    
    1. [sic] This shows the call stack.
    The bottom call `f(2)` is completed first.
    
    f(6) = f(5) + f(4) = 13 #f(6)=13 is stored in the memoization.
    f(5) = f(4) + f(3) = 8  #f(5)=8 is stored in the memoization.
    f(4) = f(3) + f(2) = 5  #f(4)=5 is stored in the memoization.
    f(3) = f(2) + f(1) = 3  #f(3)=3 is stored in the memoization.
    f(2) = f(1) + f(0) = 2  #f(2)=2 is stored in the memoization.
    
    
    2. Runtime is O(n) and space O(1) if we only cache the previous 2 elements.
    
    3. Yes. If we used plain recursion, the runtime would be exponential. Dynamic programming gets us an O(n) runtime.


"""


# recursive solution
def steps(n):
    if n < 1:
        return 1 * (n + 1)
    return steps(n - 1) + steps(n - 2)


ans = steps(6)
print(ans)


# steps inverse
# 6 7
# % 5 -> 1 2
# % 6 -> 0 1
def steps_inv(m, n):
    if m > n:
        return ((m % n) - 1) ** 2  # **2 <-> abs()
    return steps_inv(m + 1, n) + steps_inv(m + 2, n)


ans = steps_inv(0, 6)
print(ans)


# ##### 1. Number of paths up a staircase of length N where you take 1 or 2 steps each time. Example provided.
print('1. staircase...')


# 3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
# TODO: refactor
def steps_b_up_tab(n):
    agenda = [[]]
    solutions = 0
    # solutions = []
    while agenda:
        nxt = agenda.pop()
        if sum(nxt) + 2 == n:
            solutions += 2
            # solutions += [next + [1, 1], next + [2]]
        elif sum(nxt) + 1 == n:
            solutions += 1
            # solutions += [next + [1]]
        elif sum(nxt) + 2 < n:
            agenda.append(nxt + [1])
            agenda.append(nxt + [2])
        elif sum(nxt) + 1 < n:
            agenda.append(nxt + [1])

    return solutions


ans = steps_b_up_tab(6)
print(ans)


# 4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
def steps_t_down_memo(n):
    memo = dict()
    return _steps_t_down_memo(n, memo)


def _steps_t_down_memo(n, memo):
    if n < 1:
        return 1 * (n + 1)

    if n not in memo:
        memo[n] = _steps_t_down_memo(n - 1, memo) + _steps_t_down_memo(n - 2, memo)

    return memo[n]


ans = steps_t_down_memo(6)
print(ans)


# ##### 2. Computing the number of permutations of [1-n] i.e. [1,2,3,4,5,...n-1,n]
print('2. permutations...')


# 3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
def perm_b_up(n):
    tab = [1] * n
    for i in range(1, n):
        tab[i] = (i + 1) * tab[i - 1]
    return tab[-1]


ans = perm_b_up(6)
print(ans)


def perm_b_up_optimized(n):
    tab = [1, 1]
    for i in range(1, n):
        tab[0] = (i + 1) * tab[1]
        tab[1] = tab[0]
    return tab[1]


ans = perm_b_up_optimized(6)
print(ans)


# 4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
def perm_t_down(n):
    memo = dict()
    return _perm_t_down(n, memo)


def _perm_t_down(n, memo):
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = n * _perm_t_down(n - 1, memo)

    return memo[n]


ans = perm_t_down(6)
print(ans)


# ##### 3. Unique Paths: The number of paths from the top left corner of a grid to the bottom right corner when moving
#                        only down and to the right.
print('3. unique paths...')


# 3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)
def paths_b_up(n, m):
    table = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = table[i][j - 1] + table[i - 1][j]

    return table[-1][-1]


ans = paths_b_up(6, 6)
print(ans)


def paths_b_up_optimized(n, m):
    table = [1 for _ in range(n)]

    for _ in range(1, n):
        for j in range(1, m):
            table[j] = table[j] + table[j - 1]

    return table[-1]


ans = paths_b_up_optimized(6, 6)
print(ans)


# 4. Top Down Approach. Compute a small example using a top-down approach with memoization. (n=6,m=6)
def paths_t_down(n, m):
    memo = dict()
    return _paths_t_down(n - 1, m - 1, memo)


def _paths_t_down(n, m, memo):
    if (n, m) == (0, 0):
        return 1
    if min(n, m) < 0:
        return 0

    if (n, m) not in memo:
        memo[(n, m)] = _paths_t_down(n - 1, m, memo) + _paths_t_down(n, m - 1, memo)

    return memo[(n, m)]


ans = paths_t_down(6, 6)
print(ans)
