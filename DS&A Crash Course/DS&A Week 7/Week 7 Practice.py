"""
Dynamic Programming

Free Response Questions

    Describe dynamic programming.
        an efficient way of solving problems by identifying, solving, and storing subproblems. where subproblems can
        typically be solved similarly, and are less complex

    When should you use dynamic programming? What types of problems where you should consider dynamic programming as a
    possible solution?
        problem can be solved via overlapping subproblems (e.g. substrings, subarrays, subtrees)
        poor time complexity of recursive solution
        ...
        when solutions to subproblems can be used to solve larger problems

    What is the difference between top-down and bottom-up dynamic programming?
        bottom-up solves the base case, and increases size of subproblem
            typically requires loop
        top-down solves more 'naturally', and will, for example, check the cache/memoization to reduce computation
            typically requires recursion

    “Memoization” can be thought of as “caching” all the recursive calls that have already happened. What might be a
    reason why I wouldn’t want to do that?
        the data is not useful, or unnecessary

    Oftentimes, the answer  f(n) may only require the result from f(n-1). What kind of space/memory optimization can we
    do if this is the case? If it helps, you can give an example of a specific problem.

    What if we had a f(r, c) that relied only on f(r-1, c) for some arbitrary c? What kind of space/memory optimization
    can we do if this is the case? If it helps, you can give an example of a specific problem.

    Fibonacci is one example of a 1-dimensional recurrence relation optimized with dynamic programming. Identify and
    share 3 other classes of dynamic programming problems that seem similar and describe what makes them feel similar.


    Is this statement true or false?

        "Dynamic programming only helps problems that have a brute-force recursive solution."


"""