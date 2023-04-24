"""
Topics: Runtime Analysis, Linked List, Stack/Queue



Note: For all questions, assume the logarithm base is 2 unless specified otherwise.

Free Response Questions
Do not use a calculator for these questions. You should be able to solve these qualitatively using the properties of
logarithms.

Logarithms and Exponents

    1. Compute all powers of 2 up to 10. I.e. write 2^0, 2^1, 2^2, ..... 2^10
        1 2 4 8 16 32 64 128 256 512 1024

    2. What does logarithm mean? If you were given log(n) = x, describe in plain English the relationship between
    n and x.
        x is the number of times a number is multiplied by itself - orders of magnitude in base10

    3. How much larger is 2^31 than 2^28? Hint: Do not compute them each.
        3 times larger

    4. How much larger is 1 billion than 1 million ?
        1,000 times larger

    5. How much larger is log(1 million) than log(1 billion) ?
        4 times larger

    6. If log(64) = y, write log(128) in terms of y.
        y*2

    7. If log(x) = 128, write 128 in terms of x without using the logarithm.
        x = 2^128

    8. If log(x / y) = 4, write a relationship between x/y without using the logarithm.
        x*(2^4) = y; x = y/(2^4)

    9. If log(x * y) = 8, write a relationship of x,y without using the logarithm.
        x * y = 2^8; x = (2^8)/y; y = (2^8)/x

    10. If the x = 2^8. Rewrite x using base 4. If x = 4^y what is y?
        log4 x

Geometric Series

    1. What is a geometric series? Give 4 examples of different geometric series. If possible, compute their sum or
    explain why you can't.
        summation from k=0 to inf of (a * r^k);
        a geometric series is the sum of an infinite series with a constant ratio between successive terms

        compute closed forms

        examples:
        convergence: r < 1
            1. square numbers series a = 1 and r = k
                closed form: (n/2)*(n + 1)
                binomial coefficient: (n + 1) choose 2
            2.
        divergence:
            3. r > 1 -> +inf
        oscillation:
            4. r = -1 -> ±a in (a*(r^k))


    2. We say a series "converges" if you can compute the sum. What types of geometric series converge? You don't need
    to prove it - just describing it is fine. You can also use examples to explain your idea.
        any geometric series with r < 1, in (a * r^k), will converge, with the series approaching (converging to) 0 in
        the limit
        a*.5^1 + a*.5^2 + a*.5^3 + ... a*((1/2)^k) ... as k -> inf, a*(1/inf) -> 0; lim a*(1/inf) -> 0
        such convergence (when r < 1) produces the closed form (a / (1 - r)) in sum from k=0 to inf of a*(r^k)

    3. Compute 1 + 2 + 4 + 8 + 16 + 32 + 64 as a power of 2 minus an additional term.
        2^(n+1) - 1

    4. Compute 64 + 32 + 16 + 8 + 4 + 2 + 1 as a power of 2 minus an additional term.
        2^(n+1) - 1

    5. Compute 1 + 1/2 + 1/4 + 1/8.


    6. Compute 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32.

    7. If you keep adding more terms to the geometric series, what does it look like you get closer to? I.e., what does
    the series 1 + 1/2 + 1/4 + 1/8 + .... equal?


    8. Now assume the sum goes from 64 down to 0 like this:

        a. 64 + 32 + 16 + 8 + 4 + 2 + 1 + 1/2 + 1/4 + 1/8... What is this equal to?

    1. Compute  9 + 90 + 900 + 9000 as a power of 10 minus an additional term.

    1. What does 9000 + 900 + 90 + 9 + 9/10 + 9/100 + ... approach?

    1. Compute 54 + 27 + 9 + 3 + 1.

    1. Generalizing a sum of powers of 3, estimate 1 + 3 + 9 + ... + 3^n.

        a. What is the sum in terms of big O notation?

        b. Try to get an exact answer in terms of n

Runtime Analysis

    1. What is the runtime to iterate through a list of size n?
        O(n)

Runtime Analysis

    1. What is the runtime to iterate through a list of size n?
        O(n)

    2. Write a function that runs in each of the following runtimes O(1), O(log n), O(n), O(n log n), O(n^2),
    O(n^2 log n), O(n (log n)^2), O(2^n).
        def o_1(n: int) -> None:
            return None

        def o_log_n(n: int) -> None:
            while n > 0:
                n //= 2

        def o_n(n: int) -> None:
            while n > 0:
                n -= n

        def o_n_log_n(n: int) -> None:
            for _ in range(n):
                m = n
                while m > 0:
                    m //= 2

        def o_n_sqr(n: int) -> None:
            for i in range(n):
                for j in range(n):
                    continue

        def o_n_sqr_log_n(n: int) -> None
            for i in range(n):
                for j in range(n):
                    m = n
                    while m > 0:
                        m //= 2

    def o_n_log_n_sqr(n: int) -> None:
        for _ in range(n):
            m = n
            while m > 0:
                p = m
                m //= 2
                while p > 0:
                    p //= 2

    def o_two_n(n: int) -> None:
        return o_two_n(n - 1) + o_two_n(n - 1)

    3. When we say an algorithm has O(1) runtime, what does that say about the runtime in terms of the input?
        runtime is constant - unaffected by input

    4. How can you calculate the runtime when operations are nested?
        TODO: multiply them

    5. Give an example of an algorithm or write a function with O(1) runtime.
        def square(n: int):
            return n ** 2

    6. Given a table of code runtime (input size/runtime), can you determine what order of growth these functions have? Hint: Applying the doubling principle.
        N (input)           100     200     300     400     500     600

        Code A Runtime      52      110     160     198     256     308

        Code B Runtime      1001    1012    1015    1023    1025    1026

        Code C Runtime      52      183     341     779     1245    1831

Explain and Analyze Code

    Please answer the following for each block of code. You can assume nums is an integer array of size. n

    Determine the function for nums = [1,1,1,1,1]

    ...

"""