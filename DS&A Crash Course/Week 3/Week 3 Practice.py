"""
Topics: Hashmaps, Recursion

Free Response Questions

Hashmaps

    1. What does a hashmap do? What are the functions a hashmap class provides?
        hashmaps map a key to the index of a large array.
        in Python, hashmaps are called dictionaries, which retrieve, add, remove, and update keys, values, and key-value
        pairs. Python dictionaries contain the following methods:
            clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
            the more useful methods are: copy(), get(), items(), keys(), pop(), update(), and value()

    2. What is the benefit of using a hashmap over an array or linked list?
        hashmaps have O(1) lookup time, versus O(n) array, and O(n) linked list

    3. What are the runtimes of the get/set functions in a hashmap? Best, average, and worst-case?
        Ω(1) best, Θ(1) average, O(n) worst collision

    4. What type of input gives the worst case for hashmap? How can we prevent this from happening?
        input that collides. use a robust hashing function.

    5. Here are some hash functions: Which one(s) of them are good and why? How would you improve the bad ones? When
    identifying one is bad, point out which quality of a good hashing function is not met.
        good hash functions are: (1) fast to compute; (2) minimize collisions (duplication).

        a. Hashing a phone number - use the area code.
            (1) is fast to compute; (2) massive number of collisions (up to 10,000,000)
            quality: poor
            improvement: increase input space by using higher base symbols, e.g., letters, or more digits

        b. Hashing a social security number - use the last four digits.
            (1) is fast to compute; (2) massive number of collisions (up to 100,000)
            quality: poor
            improvement: increase input space by using higher base symbols, e.g., letters, or more digits

        c. Hashing a string - use the sum of each of the character's ASCII codes
            (1) is fast to compute; (2) low collision number on longer strings
            quality: good

        d. Hashing a Person object - using the Person's age
            (1) is fast to compute; (2) massive number of collisions (millions to 100 millions)
            quality: extremely poor
            improvement: increase input space by using, e.g., day (of 365) born, initials, and place of birth


    6. How are collisions handled in linear probing? How are collisions handled in separate chaining? Describe the
    differences in detail.
        linear probing: finds the nearest unoccupied cell, increasing index
        separate chaining: appends collisions to a linked list, with the initially occupied index as the head
        todo: detail

    7. Suppose I implement a hashmap with the hash function h(x) = x mod 10, a list of length 10, and with linear
    probing. I insert the elements 32, 47, 42, 43, 15, 19, 16, 27 in that order. Write out what the list of the hashmap
    looks like after each insert.
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [32]
        [32, 47]
        [32, 42, 47]
        [32, 42, 43, 47]
        [32, 42, 43, 15, 47]
        [32, 42, 43, 15, 47, 19]
        [32, 42, 43, 15, 16, 47, 19]
        [32, 42, 43, 15, 16, 47, 27, 19]


Recursion

    1. What is recursion? How do you make sure recursion does not run infinitely?
        recursion is a method of self reference that requires its input approach a terminating base case (which is often
        a reduction in input size)

    2. How do you convert a function with iteration (e.g., a for loop) to a recursive function? For example, how can I
    loop through numbers in a list using recursion?
        modify (approach base case) input; e.g. sum_fn = lambda x, y: y if len(x) == 0 else sum_fn(x[:-1], y + x[-1])

    3. What is binary search? What is the requirement for the thing (e.g., list) that you are doing a binary search on?
        O(log n) search that requires a sorted list to utilize the properties of bisecting a sorted array

    4. What is the runtime and space complexity for binary search?
        O(log n); O(1)

Runtime Analysis

    For each of the following code blocks, please answer the following and explain your answer choices.

        1. Compute f(n) for n = 2, 4, 8, 16. For large values with exponents or factorials, you do not need to compute
        them and can leave them in the form a^b, c!, etc. In code block G, compute for m = n, i.e. (m,n) = (2,2), (4,4),
        ... (16,16).

        2. In terms of n, what does the code block return? You may use asymptotics (big O), but we encourage you to find
        an exact answer when you can. Explain your answer.

        3. What is the runtime of the code (possibilities below)? Explain your answer.
        Select from the following:
        -        -        -         -          -             -               -           -           -          -
        0        1        ~n        ~2n        ~log n        ~n log n        ~n^2        ~2^n        ~n!        ∞ / inf

    Note: When describing the runtime, please describe qualitatively why the code would give that runtime. Do not use
    empirical data to justify a runtime. For example:

        f(4) = 4, f(8) = 5, f(16) = 6 so it's O(log n)

    Is not an acceptable answer. What we're looking for is something like:

        The recursive call return f(n /// 2) + 1 reduces the input in half each time until the function terminates with
        a base case of n=0. Therefore, the runtime is O(log n).

    Many different functions could be O(log n) - we want you to identify what types of code lead to O(log n) runtime.
    This way you won't need to calculate f(n) for several values to identify the runtime. We encourage computing a few
    cases of n manually to get intuition, but after that you should look for what about the code makes that runtime
    happen.

    # Code Block A
    def fn_a(n: int) -> int:
      if n == 1:
        return n
      return fn_a(n - 1) + 1

    # Code Block A

        1. Compute f(n) for n = 2, 4, 8, 16. For large values with exponents or factorials, you do not need to compute
        them and can leave them in the form a^b, c!, etc. In code block G, compute for m = n, i.e. (m,n) = (2,2), (4,4),
        ... (16,16).
            f(n) = n, where n = 2, 4, 8, 16 -> 2, 4, 8, 16

        2. In terms of n, what does the code block return? You may use asymptotics (big O), but we encourage you to find
        an exact answer when you can. Explain your answer.
            returns n in O(n) time using O(n) auxiliary (callstack) space

        3. What is the runtime of the code (possibilities below)? Explain your answer.
        Select from the following:
        -        -        -         -          -             -               -           -           -          -
        0        1        ~n        ~2n        ~log n        ~n log n        ~n^2        ~2^n        ~n!        ∞ / inf

        O(n)
        returns the input n by reducing input by 1 until terminating on the base case of n == 1, returning n (1), while
        adding 1 to each each recursive call. ((fn(1) + 1) + 1) + 1


    # Code Block B
    def fn_b(n: int) -> int:
      if n == 1:
        return n
      return fn_b(n - 1) + fn_b(n - 1)

    # Code Block B

        1. Compute f(n) for n = 2, 4, 8, 16. For large values with exponents or factorials, you do not need to compute
        them and can leave them in the form a^b, c!, etc. In code block G, compute for m = n, i.e. (m,n) = (2,2), (4,4),
        ... (16,16).
            f(n) = 2^(n - 1), where n = 2, 4, 8, 16 -> 2, 8, 128, 32_768

        2. In terms of n, what does the code block return? You may use asymptotics (big O), but we encourage you to find
        an exact answer when you can. Explain your answer.
            returns 2^(n - 1) in O(2^n) time using O(n) auxiliary (callstack) space (height of tree, n)

        3. What is the runtime of the code (possibilities below)? Explain your answer.
        Select from the following:
        -        -        -         -          -             -               -           -           -          -
        0        1        ~n        ~2n        ~log n        ~n log n        ~n^2        ~2^n        ~n!        ∞ / inf
            O(2^n)
            returns 2 doubled (n - 1) times by reducing input by 1 and adding the left call to the call stack until
            terminating on the base case of n == 1, then consumes the call stack as if it were traversing a tree
            structure post-order. the (n - 1) is the result of terminating (returning) at n == 1.


    # Code Block C
    def fn_c(n: int) -> int:
      if n == 1:
        return n
      return fn_c(n - 1) * n

    # Code Block C

        1. Compute f(n) for n = 2, 4, 8, 16. For large values with exponents or factorials, you do not need to compute
        them and can leave them in the form a^b, c!, etc. In code block G, compute for m = n, i.e. (m,n) = (2,2), (4,4),
        ... (16,16).
            f(n) = n!, where n = 2, 4, 8, 16 -> 2, 24, 40_320, 20_922_789_888_000


        2. In terms of n, what does the code block return? You may use asymptotics (big O), but we encourage you to find
        an exact answer when you can. Explain your answer.
            n * (n - 1) * (n - 2) * (n - 3)...
            5 * 4 * 3 * 2 * 1
            n! in O(n) time using O(n) auxiliary (callstack) space

        3. What is the runtime of the code (possibilities below)? Explain your answer.
        Select from the following:
        -        -        -         -          -             -               -           -           -          -
        0        1        ~n        ~2n        ~log n        ~n log n        ~n^2        ~2^n        ~n!        ∞ / inf
            O(n)
            returns n * f(n - 1) * f(n - 2) * f(n - 3)..., terminating at (n == 1).
            1 * (n - (n - 2)) * (n - (n - 3))...


    # Code Block D
    def fn_d(n: int) -> int:
      if n <= 1:
        return 1
      count = 0
      for x in range(n):
        count += x
      return fn_d(n // 2) + fn_d(n // 2) + count


    # Code Block D
        recurses 2*log(n) times, with (n - height) operations at depth

        1. Compute f(n) for n = 2, 4, 8, 16. For large values with exponents or factorials, you do not need to compute
        them and can leave them in the form a^b, c!, etc. In code block G, compute for m = n, i.e. (m,n) = (2,2), (4,4),
        ... (16,16).
            f(n) = , where n = 2, 4, 8, 16 ->



        2. In terms of n, what does the code block return? You may use asymptotics (big O), but we encourage you to find
        an exact answer when you can. Explain your answer.
            todo n * (n - 1) * (n - 2) * (n - 3)...
            todo 5 * 4 * 3 * 2 * 1
            todo n! in O(n) time using O(n) auxiliary (callstack) space

        3. What is the runtime of the code (possibilities below)? Explain your answer.
        Select from the following:
        -        -        -         -          -             -               -           -           -          -
        0        1        ~n        ~2n        ~log n        ~n log n        ~n^2        ~2^n        ~n!        ∞ / inf
            todo O(n)
            todo returns n * f(n - 1) * f(n - 2) * f(n - 3)..., terminating at (n == 1).
            todo 1 * (n - (n - 2)) * (n - (n - 3))...

    # Code Block E
    def fn_e(n: int) -> int:
      if n == 0:
        return 1
      return fn_e(n // 2) + fn_e(n // 2)

    # Code Block F
    def fn_f(n: int) -> int:
      if n + 1 < 0:
        return n
      return fn_f(n // 2) + fn_f(n // 2)

    # Code Block G
    def fn_g(n: int, m: int) -> int:
        if n <= 0 or m <= 0:
            return 1
        return fn_g(n // 2, m) + fn_g(n, m // 2)


    Hint: If you're having trouble identifying the runtime, try the following.

        1. Think of functions you are already familiar with. Can you see any clear pattern between what you know and
        what is there? Ones you know are Fibonacci, factorial, etc.

        2. Look at how n is being reduced. Then try some sample values of n and see what happens. You may want to try
        5,6,7,8...  and see how it grows. Or perhaps try 2,4,8,16,32,... depending on the problem.

        3. (2) will help you see the pattern. Once you see the pattern, it can be easier to try and describe it.

"""