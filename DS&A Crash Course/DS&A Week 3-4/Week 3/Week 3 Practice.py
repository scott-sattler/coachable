"""
Topics: Hashmaps, Recursion
Free Response Questions

Hashmaps

    1. What does a hashmap do? What are the functions a hashmap class provides?
        hashmaps take a hashing function, and maps some input to the hashed index (hash value -> list index)
        each hash index contains a key-value pair, where some object is typically stored (linked to)
        in Python, for example, keys(), values(), items() (key-value pairs), update (add to hashmap), and get()...

    2. What is the benefit of using a hashmap over an array or linked list?
        versatility in the case of an array (e.g. ability to store an additional object), and runtime in the case of LL

    3. What are the runtimes of the get/set functions in a hashmap? Best, average, and worst-case?
        get/set: O(1); O(1); O(n) (all keys collided, with the last-most element being the get/set value)

    4. What type of input gives the worst case for hashmap? How can we prevent this from happening?
        all keys collided, with the last-most element being the get/set value

    5. Here are some hash functions: Which one(s) of them are good and why? How would you improve the bad ones?
        a. Hashing a phone number - use the area code.
            not good: massive number of collisions. input is not uncommon enough. entire number would be an improvement

        b. Hashing a social security number - use the last four digits.
            not good: same as above, although less common. since SS's are unique, the entire number could be used

        c. Hashing a string - use the sum of each of the character's ASCII codes
            decent or not bad: to reduce collisions, you could incorporate information, such as char index

        d. Hashing a Person object - using the Person's age
            not good: massive number of collisions. input is not uncommon enough. additional information such as SS
            could be used to improve

    6. How are collisions handled in linear probing? How are collisions handled in separate chaining? Describe the
    differences in detail.
        linear probing handles collisions by looking for the next free index, typically(?) to the right
        separate chaining handles collisions by creating a linked list of collision values

    7. Suppose I implement a hashmap with the hash function h(x) = x mod 10, a list of length 10, and with linear
    probing. I insert the elements 32, 47, 42, 43, 15, 19, 16, 27 in that order. Write out what the list of the hashmap
    looks like after each insert.
        3, 4, 4, 4, 1, 1, 1, 2
        32
        32 47
        32 47 42
        32 47 42 43
        15 32 47 42 43
        15 19 32 47 42 43
        15 19 32 47 42 43 16
        15 19 32 47 42 43 16 27
        0  1  2  3  4  5  6  7  8  9
           15 19 32 47 42 43 16 27

Recursion

    1. What is recursion? How do you make sure recursion does not run infinitely?
        a function that calls itself; base case

    2. How do you convert a function with iteration (e.g., a for loop) to a recursive function? For example, how can I
    loop through numbers in a list using recursion?
        make the goal emulate iteration, e.g.:
            def recursive_iteration(index, list):
                if index = len(list) - 1
                    return
                return recursive_iteration(index + 1, list)

    3. What is binary search? What is the requirement for the thing (e.g., list) that you are doing a binary search on?
        binary search bisects an ordered sequence to find a specified value
        binary search requires an ordered sequence

    4. What is the runtime and space complexity for binary search?
        computational complexity: O(log(n))
        space complexity: O(1) iterative: O(log(n)) recursive (call stack)

Runtime Analysis

    For each of the following code blocks, please answer the following and explain your answer choices.

    1. For n=2, 4, 8, 16 compute f(n).

    2. What does the code block return? (In terms of n). Explain your answer.

    3. What is the runtime of the code? Explain your answer.

    Select from the following options:
        0   1   ~n   ~2n   ~log(n)   ~nlog(n)   ~n^2   ~2^n   ~n!   inf

    Note: When describing the runtime, please describe qualitatively why the code would give that runtime. Do not use
    empirical data to justify a runtime. For examples

    f(4) = 4, f(8) = 5, f(16) = 6 so it's O(log n)

    Is not an acceptable answer. What we would be looking for is:

        The recursive call return f(n /// 2) + 1 reduces the input in half each time until the function terminates with
        a base case of n=0. Therefore the runtime is O(log n)

    Many different functions could be O(log n) - we want you to identify what types of code lead to O(log n) runtime.
    This way you won't need to calculate f(n) for several values to identify the runtime. We encourage computing a few
    cases of n manually to get intuition, but after that you should look for what about the code makes that runtime
    happen.

    < CODE BLOCKS A-G BELOW >

    Hint: If you're having trouble identifying the runtime, try the following.

    1. Think of functions you are already familiar with. Can you see any clear pattern between what you know and what is
    there? Ones you know are Fibonacci, factorial, etc.

    2. Look at how n is being reduced. Then try some sample values of n and see what happens. You may want to try
    5, 6, 7, 8... and see how it grows. Or perhaps try 2, 4, 8, 16, 32... depending on the problem.

    3. (2) will help you see the pattern. Once you see the pattern, it can be easier to try and describe it.
"""


# Code Block A
def fn_a(n: int) -> int:
    if n == 1:
        return n
    return fn_a(n - 1) + 1
# O(n): linear reduction in input


# Code Block B
def fn_b(n: int) -> int:
    if n == 1:
        return n
    return fn_b(n - 1) + fn_b(n - 1)
# O(2^n): each recursive call doubles the number of calls, for n times


# Code Block C
def fn_c(n: int) -> int:
    if n == 1:
        return n
    return fn_c(n - 1) * n
# O(n): linear reduction in input (runtime is unaffected by constant factor)

# Code Block D
def fn_d(n: int) -> int:
    if n <= 1:
        return 1
    count = 0
    for i in range(n):
        count += i
    return fn_d(n // 2) + fn_d(n // 2) + count
# O(n*log(n) + 2^log(n)) -> O(n*log(n) + n) -> O(n*log(n)):
# n operations (for loop) log(n) times (input is being reduced by half); disregard lower orders
# note: 2^log_2(n) -> n


# Code Block E
def fn_e(n: int) -> int:
    if n == 0:
        return 1
    return fn_e(n // 2) + fn_e(n // 2)
# O(2^log(n)) -> O(n): input is being reduced by half, while doubling the number of calls
# note: 2^log_2(n) -> n

# Code Block F
def fn_f(n: int) -> int:
    if n + 1 < 0:
        return n
    return fn_f(n // 2) + fn_f(n // 2)
# inf: the if statement reduces to n < -1; the floor division will (bottom out at or) never result in n < 0; hence, inf

# Code Block G
def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n // 2, m) + fn_g(n, m // 2)
# O(2^(log(n) + log(m)) -> 2^log(n*m)): as either n or m <=0 ends the recursion tree, there is a race to 0, by halves...
