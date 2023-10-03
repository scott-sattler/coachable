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
        todo

    4. “Memoization” can be thought of as “caching” all the recursive calls that have already happened. What might be a
    reason why I wouldn’t want to do that?
        repeated calls with the same arguments are impossible, unlikely, or are avoidable.

    5. Oftentimes, the answer  f(n) may only require the result from f(n-1) and f(n-2). What kind of space/memory
    optimization can we do if this is the case? If it helps, you can give an example of a specific problem.
        only store the results for previous calls that are going to be reused

    6. What if we had a f(r, c) that relied only on f(r-1, c) for some arbitrary c? What kind of space/memory
    optimization can we do if this is the case? If it helps, you can give an example of a specific problem.
        todo

    7. Fibonacci is one example of a 1-dimensional recurrence relation optimized with dynamic programming. Identify and
    share 3 other classes of dynamic programming problems that seem similar and describe what makes them feel similar.
        todo

    8. Is this statement true or false?
    "Dynamic programming only helps problems that have a brute-force recursive solution."
        false. todo, explain


Dynamic Programming and Recurrence Examples
    Each of the below problems can be solved with recursion. Please  answer the following for each one.
    1. Unit Tests. Identify the solution cases up to n= 4. For 2D, do all cases up to (3,3)

    2. Recurrence Relation.  Identify the recurrence relationship and base cases. Explain why they are true by giving a
    qualitative explanation in plain English.

    3. Bottom Up. Compute a small example using a bottom-up (n = 6, m = 6)

    4. Top-Down Approach. Compute a small example using a top-down approach with memorization. (n=6,m=6)

    5. Complexity Analysis. Identify the optimal runtime and space complexity.

    6. Is DP worth it? Does dynamic programming improve the runtime compared to a recursive approach?

Problems That Can Be Solved with Recursion
    1. Number of paths up a staircase of length N where you take 1 or 2 steps each time. Example provided.

    2. Computing the number of permutations of [1-n] i.e. [1,2,3,4,5,...n-1,n].

    3. Unique Paths: The number of paths from the top left corner of a grid to the bottom right corner when moving only
    down and to the right.

    4. Given a 2xN grid, how many different ways can you fill the gird with 2x1 dominoes?

    5. Given a 3xN grid, how many different ways can you fill the gird with 3x1 dominoes?

    6. Given a set A = {1,2,3,...,N} calculate the number of possible subsets of A.

    7. Given a set A = {1,2,3,...,N} calculate the number of possible subsets of A that do not contain any 2 numbers
    that are 1 apart. For example, {1,2,4}  would not be valid because 1 and 2 are 1 apart.

    8. Count the number of functions from {1,2,3,...,N} to a set of size {1,2,3,...,M}. Here is an additional
    explanation of functions.

    9. A function has a fixed point if f(x) = x for any x in the domain of f . How many functions are there from
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

    f(0) = 1, f(1) = 1, f(2) = 2
    f(3) = f(2) + f(1) = 3
    f(4) = f(3) + f(2) = 5
    f(5) = f(4) + f(3) = 8
    f(6) = f(5) + f(4) = 13

    1. This shows the call stack.
    The bottom call `f(2)` is completed first.

    f(6) = f(5) + f(4) = 13 #f(6)=13 is stored in the memoization.
    f(5) = f(4) + f(3) = 8  #f(5)=8 is stored in the memoization.
    f(4) = f(3) + f(2) = 5  #f(4)=5 is stored in the memoization.
    f(3) = f(2) + f(1) = 3  #f(3)=3 is stored in the memoization.
    f(2) = f(1) + f(0) = 2  #f(2)=2 is stored in the memoization.

    2. Runtime is O(n) and space O(1) if we only cache the previous 2 elements.

    3. Yes. If we used plain recursion, the runtime would be exponential. Dynamic programming gets us an O(n) runtime.

OPTIONAL: Recursive Challenge Problems
    The following are very tough and completely optional.
    Hint: For these, you can assume the distinct integers are 1,2,3,...,N Moreover, 8-11 are very tricky, so don't
    hesitate to utilize external references. However, make sure you understand how they arrived at those solutions.
    1. Given a 4xN grid, how many different ways can you fill the grid with 2x1 dominoes?

    2. How many binary trees can you create with N distinct integers? Assume N=2^n-1 i.e. so N is the number of elements
    in a complete binary tree.

    3. How many binary search trees can you create with N=2^n-1 distinct integers?

    4. How many distinct binary heaps can you  create with N=2^n-1 distinct integers?

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

Challenge: Now solve 8-11 without assuming N=2^n-1

"""