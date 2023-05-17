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
        x is the number of times the number n is multiplied by itself - orders of magnitude in base10

    3. How much larger is 2^31 than 2^28? Hint: Do not compute them each.
        3 times larger

    4. How much larger is 1 billion than 1 million?
        1,000 times larger, base 10
        log2(1_000), ~ log2(1024), so ~10

    5. How much larger is log(1 million) than log(1 billion)?
        log10(1 million) = 6
        log10(1 billion) = 9
        +3 larger

    6. If log(64) = y, write log(128) in terms of y.
        y + 1

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
        - summation from k=0 to +inf of (a * r^k)
        - a geometric series is the sum of an infinite series with a constant ratio between successive terms
        - geometric series exhibit one of three behaviors:
            a. convergence, i.e. they approach a finite value, which can be found by taking the limit of its closed
            form, iff the absolute value of the ratio between successive terms is less than one
            b. divergence, i.e. they infinitely diverge, iff the absolute value of the ratio between successive terms is
            is greater than or equal to one
            c. oscillation, i.e. they flip between two values, neither converging nor diverging, but oscillating iff the
            ratio between successive terms is exactly -1; n(-1)^n
        - note: all bounded series (i.e. contain boundaries) are finite in the absence of unbounded terms (infinities)

        examples:
        convergence: r < 1
            1. square numbers series a = 1 and r = k
                closed form: (n/2)*(n + 1)
                binomial coefficient: (n + 1) choose 2
            2. 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 + 1/2 + 1/4 + 1/8... -> 256
        divergence:
            3. r > 1 -> +inf
                1 + 2 + 4 + 8 + 16 + 32... -> +inf
        oscillation:
            4. r = -1 -> ±a in (a*(r^k))
                Grandi's Series: sum from k=0 to +inf of -1^k -> 1, -1, 1, -1, 1...
                    notice: 0 if k % 2 == 0; -1 if k % 2 != 0


    2. We say a series "converges" if you can compute the sum. What types of geometric series converge? You don't need
    to prove it - just describing it is fine. You can also use examples to explain your idea.
        - any geometric series with r < 1, in (a * r^k), will converge, with the series approaching (converging to) 0 in
        the limit
        - a*.5^1 + a*.5^2 + a*.5^3 + ... a*((1/2)^k) ... as k -> inf, a*(1/inf) -> 0; lim a*(1/inf) -> 0
        - such convergence (when r < 1) produces the closed form (a / (1 - r)) in sum from k=0 to inf of a*(r^k)

    3. Compute 1 + 2 + 4 + 8 + 16 + 32 + 64 as a power of 2 minus an additional term.
        2^(n+1) - 1

    4. Compute 64 + 32 + 16 + 8 + 4 + 2 + 1 as a power of 2 minus an additional term.
        2^(n+1) - 1

    5. Compute 1 + 1/2 + 1/4 + 1/8.
        8/8 + 4/8 + 2/8 + 1/8 = (8 + 7)/8 = 15/8

    6. Compute 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32.
        32/32 + 16/32 + 8/32 + 4/32 + 2/32 + 1/32 = (32 + 31)/32 = 63/32

    7. If you keep adding more terms to the geometric series, what does it look like you get closer to? I.e., what does
    the series 1 + 1/2 + 1/4 + 1/8 + .... equal?
        2

    8. Now assume the sum goes from 64 down to 0 like this:
        a. 64 + 32 + 16 + 8 + 4 + 2 + 1 + 1/2 + 1/4 + 1/8... What is this equal to?
            (2n - 1) + (1) = ~128

    9. Compute  9 + 90 + 900 + 9000 as a power of 10 minus an additional term.
        10^n - 1

    10. What does 9000 + 900 + 90 + 9 + 9/10 + 9/100 + ... approach?
        10,000

    11. Compute 54 + 27 + 9 + 3 + 1.
        94

    12. Generalizing a sum of powers of 3, estimate 1 + 3 + 9 + ... + 3^n.
        a. What is the sum in terms of big O notation?
            O(n): n multiply and n add operations

        b. Try to get an exact answer in terms of n
            n(n + 1)


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
            data = [0, 0]
            for _ in range(n):
                data += data[:]

        recursive
        def o_two_n(n: int) -> None:
            return o_two_n(n - 1) + o_two_n(n - 1)


    3. When we say an algorithm has O(1) runtime, what does that say about the runtime in terms of the input?
        runtime is constant - unaffected by input

    4. How can you calculate the runtime when operations are nested?
        multiply them

    5. Give an example of an algorithm or write a function with O(1) runtime.
        def square(n: int):
            return n ** 2

    6. Given a table of code runtime (input size/runtime), can you determine what order of growth these functions have?
    Hint: Applying the doubling principle.
        N (input)           100     200     300     400     500     600
        Code A Runtime      52      110     160     198     256     308       +58   +50   +38   +58   +52  -> N*k
        Code B Runtime      1001    1012    1015    1023    1025    1026      +11   +3    +8    +3    +1   -> (log N)*k
        Code C Runtime      52      183     341     779     1245    1831      +131  +158  +438  +466  +586 -> N^2


Explain and Analyze Code

    Please answer the following for each block of code. You can assume nums is an integer array of size n.
        a. Determine the function for nums = [1,1,1,1,1].
        b. Determine the function for nums = [1,2,3,4,5].
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
        d. What does this function do?
        e. What is the runtime complexity? And why?
        f. What is the space complexity? And why?

    1.
        def func_one(nums) -> int:                  # T(n) where n = len(nums)
            n = len(nums)                           # 1
            all_nums = []                           # 1
            for i in range(n):                      # n + 1
                for j in range(n):                  # n * n + 1
                    all_nums.append(nums[j])        # n * n
            output = 0                              # 1
            for value in all_nums:                  # n * n + 1
                output += value                     # n * n
            return output                           # 1
                                                    # 4*n^2 + n + c

        a. Determine the function for nums = [1,1,1,1,1].
            sum([1] * 25) -> 25
        b. Determine the function for nums = [1,2,3,4,5].
            sum([1,2,3,4,5] * 5) -> 75
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            4*n^2 + n, evaluated at 2, 4, 8, 16, 32
            -> 18 68 264 1040 4128
            or n^2
            -> 4 16 64 256 1024
        d. What does this function do?
            it appends each elements of nums, to a new list, len(nums) times, then sums the new list
        e. What is the runtime complexity? And why?
            O(n^2); because we're performing n operations, n times
        f. What is the space complexity? And why?
            O(n^2); because we're creating a list of size n, n times

    2.
        def func_two(nums) -> int:                  # T(n) where n = len(nums)
            n = len(nums)                           # 1
            value = 0                               # 1
            for i in range(n):                      # n + 1
                for j in range(n):                  # n * n + 1
                    value += nums[j]                # n * n
            return value                            # 1
                                                    # 2*n^2 + n + c

        a. Determine the function for nums = [1,1,1,1,1].
            5 * 5 -> 25
        b. Determine the function for nums = [1,2,3,4,5].
            15 * 5 -> 75
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            2*n^2 + n, evaluated at 2, 4, 8, 16, 32
            -> 10 36 136 528 2080
            or n^2
            -> 4 16 64 256 1024
        d. What does this function do?
            it multiplies the sum of nums by the length of nums
        e. What is the runtime complexity? And why?
            O(n^2); to sum nums, each element must be accessed, which is then done by the length of nums (n times)
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size

    3.
        def func_three(nums) -> int:                # T(n) where n = len(nums)
            n = len(nums)                           # 1
            value = 0                               # 1
            while n > 0:                            # log(n) + 1
                value += nums[n - 1]                # log(n)
                n //= 2                             # log(n)
            return value                            # 1
                                                    # 3*log(n) + c

        a. Determine the function for nums = [1,1,1,1,1].
            nums[4] + nums[1] + nums[0] -> 3
        b. Determine the function for nums = [1,2,3,4,5].
            nums[4] + nums[1] + nums[0] -> 5 + 2 + 1 -> 8
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            3*log(n), evaluated at 2, 4, 8, 16, 32
            -> 3 6 9 12 15
            or log(n)
            -> 1 2 3 4 5
        d. What does this function do?
            inclusive of zero, decrements the nums index by half, from (len - 1), while adding the value at each index
            to a running total
        e. What is the runtime complexity? And why?
            O(log(n)); the input, an array of size n, is being accessed log(n) times
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size

    4.
        def func_four(nums) -> int:                 # T(n) where n = len(nums)
            double_nums = []                        # 1
            for num in nums:                        # n + 1
                double_nums.append(num + num)       # n
            return sum(double_nums)                 # n + 1
                                                    # 3*n + c

        a. Determine the function for nums = [1,1,1,1,1].
            2 * 5 -> 10
        b. Determine the function for nums = [1,2,3,4,5].
            (x + x) * 5 (associative) -> 15 * (2 * 5) -> 150
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            3*n, evaluated at 2, 4, 8, 16, 32
            -> 6 12 24 48 96
            or n
            -> 2 4 8 16 32
        d. What does this function do?
            sums the double of each number in the array
        e. What is the runtime complexity? And why?
            O(n); the input is an array of size n, where the algorithm performs constant time operations on each element
        f. What is the space complexity? And why?
            O(n) with O(n) auxiliary; O(n) describes the input size, n, while O(n) indicates the algorithm space
            complexity (auxiliary space) scales proportional to the input size, n

    5.
        def func_five(nums) -> int:                 # T(n, m) where n = len(nums)
                                                    #           and m = sum(nums)
            power_sum = 1                           # 1
            for i in range(len(nums)):              # n + 1
                for j in range(nums[i]):            # m * n + 1
                    power_sum *= 2                  # m * n

            total = 0                               # 1
            for i in range(power_sum)               # m * n + 1
                total += 1                          # m * n
            return total % 99                       # 1
                                                    # 4*(m * n) + n + c

        a. Determine the function for nums = [1,1,1,1,1].
            2^5 -> (0 + 1, 32 times) % 99 -> 32
        b. Determine the function for nums = [1,2,3,4,5].
            2^n where n = [1, 2, 3, 4, 5] -> 2^15 -> (0 + 1, 32,768 times) % 99 -> 98
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            4*(n * m) + n, evaluated at (2, 2), (4, 4), (8, 8), (16, 16), (32, 32)
            -> 18 68 264 1040 4128
            or n * m
            -> 4 16 64 256 1024
        d. What does this function do?
            doubles 1 for the length of the input array, by each value of each index
        e. What is the runtime complexity? And why?
            O(n * m) where n is the length of the input array, and m is the sum of every element within the array
        f. What is the space complexity? And why?
            O(n) with O(max(m)) auxiliary; O(n) describes the input size, n, while O(max(m)) indicates the algorithm
            space complexity (auxiliary space) scales with the sum of the array values

    6.
        def func_six(nums) -> int:                                              # T(n) where n = len(nums)
            count = 0                                                           # 1
            for i in range(1, len(nums)-1):                                     # n + 1 - 1
                if (nums[i] < nums[i-1] * 2) and (nums[i] > nums[i+1] / 2):     # n - 1 + 5
                    count += 1                                                  # n - 1
            return count                                                        # 1
                                                                                # 3*n + c

        a. Determine the function for nums = [1,1,1,1,1].
            0
        b. Determine the function for nums = [1,2,3,4,5].
            2
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            3*n, evaluated at 2, 4, 8, 16, 32
            -> 6 12 24 48 96
            or n
            -> 2 4 8 16 32
        d. What does this function do?
            counts the number of elements that are less than twice the previous element, and greater than half of the
            next element
        e. What is the runtime complexity? And why?
            O(n); the input is an array of size n, where the algorithm performs constant time operations on all but 2
            elements
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size

    7.
        def func_seven(nums: list[int]):            # T(n) where n = len(nums)
          N = len(nums)                             # 1
          total = 0                                 # 1
          n = N                                     # 1
          while n > 0:                              # log(n) + 1
              for i in range(0, n):                 # (n + n/2 + n/4 + n/8 ...) 2*n + 1;  n + ?  todo: fix ? = (n / (2^k))^log(n)
                  total += nums[i]                  # 2n
              n = n // 2                            # log(n)
          return total                              # 1
                                                    # 4*n + 2*log(n) + c

        a. Determine the function for nums = [1,1,1,1,1].
            5 + 2 + 1 -> 8
        b. Determine the function for nums = [1,2,3,4,5].
            15 + 3 + 1 -> 19
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            4*n + 2*log(n), evaluated at 2, 4, 8, 16, 32
            -> 10 20 38 72 138
            or n
            -> 2 4 8 16 32
        d. What does this function do?
            it repeatedly sums the array from 0 to n, halving n until reaching zero
        e. What is the runtime complexity? And why?
            O(n); we're accessing every element of an array log(n) times, while halving its size each iteration,
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size

    8.
        def func_eight(nums: list[int]):            # T(n) where n = len(nums)
          N = len(nums)                             # 1
          total = 0                                 # 1
          i = 1                                     # 1
          while i < N:                              # log(n) + 1
              for j in range(0, i):                 # 2^log(n) -> n + 1  (not 2n as i < N)
                  total += nums[j]                  # n
              i = i * 2                             # log(n)
          return total                              # 1
                                                    # 2*n + 2*log(n) + c

        a. Determine the function for nums = [1,1,1,1,1].
            1 + 2 + 4 -> 7
        b. Determine the function for nums = [1,2,3,4,5].
            1 + 3 + 10 -> 14
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            2*n + 2*log(n), evaluated at 2, 4, 8, 16, 32
            -> 6 12 22 40 74
            or n
            -> 2 4 8 16 32
        d. What does this function do?
            sums subarrays of n, doubling in size from 0 to n (exclusive)
        e. What is the runtime complexity? And why?
            O(n); we're doubling the size of an iteration, log(n) times (n^log(n) -> n)
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size


    9.
        def func_nine(nums: list[int]):             # T(n) where n = len(nums)
          N = len(nums)                             # 1
          total = 0                                 # 1
          i = 1                                     # 1
          while i < N:                              # log(n) + 1
              for j in range(0, N):                 # n * log(n) + 1
                  total += nums[j]                  # n * log(n)
              i = i * 2                             # log(n)
          return total                              # 1
                                                    # 2*n * log(n) + 2*log(n) + c

        a. Determine the function for nums = [1,1,1,1,1].
            5 + 5 + 5 -> 15
        b. Determine the function for nums = [1,2,3,4,5].
            15 + 15 + 15 -> 45
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            2*n * log(n) + 2*log(n), evaluated at 2, 4, 8, 16, 32
            -> 6 20 54 136 330
            or n * log(n)
            -> 2 8 24 64 160
        d. What does this function do?
            adds the sum of the input to a running total, log(n) times
        e. What is the runtime complexity? And why?
            O(n * log(n)); we're accessing every element the input array, log(n) times
        f. What is the space complexity? And why?
            O(n) with O(1) auxiliary; O(n) describes the input size, n, while O(1) indicates the algorithm space
            complexity (auxiliary space) does not scale with the input size


    10.
        # input: an arbitrarily large array of integers of size N
        def func_10(arr: list[int]):                                            # T(n) where n = len(arr)
            arr.sort() # This line is O(n log n) runtime.                       # n * log(n)
            reverse_arr = [arr[i] for i in range(len(arr)-1, -1, -1)]           # n
            complements = []                                                    # 1

            # zip just iterates through both arrays at the same time
            for num1, num2 in zip(arr, reverse_arr):                            # 2n
                complements.append(num1 + num2)                                 # n

          return compliments                                                    # 1
                                                                                # n * log(n) + 3*n + c

        a. Determine the function for nums = [1,1,1,1,1].
            [2] * 5
        b. Determine the function for nums = [1,2,3,4,5].
            [6] * 5
        c. Suppose nums = [i for i in range(0, n)]. Approximate the number of computations required to compute
        func(nums) for n = 2, 4, 8, 16, 32.
            n * log(n) + 3*n, evaluated at 2, 4, 8, 16, 32
            -> 8 20 48 112 256
            or n * log(n)
            -> 2 8 24 64 160
        d. What does this function do?
            creates a list that is the sum of each index with that same index in a reversed list
        e. What is the runtime complexity? And why?
            O(n * log(n)); the lower boundary of comparison sorting is O(n * log(n)), which is the largest order of
            complexity within this algorithm
        f. What is the space complexity? And why?
            O(n) with O(n) auxiliary; O(n) describes the input size, n, while O(2n) -> O(n) indicates the algorithm
            space complexity (auxiliary space) scales linearly with the input size (copy of array)


    11. For this problem, just compute the runtime of func_11:
        O(N^2 * log(N))

        # This function has log(N) runtime
        # Where N is the input integer
        def helper_func(N):
              # does something that takes log(N) runtime.
              # Note that if N = 1, then the runtime is O(1)
              return

        # input: an arbitrarily large integer N
        def func_11(N):                             #
            helper_func()                           # log(N) or 1 if helper_func(1)
            for i in range(N):                      # N + 1
                helper_func(i)                      # log(N)
                for j in range(N):                  # N * N + 1
                    helper_func(j)                  # N * N * log(N)
                helper_func(N)                      # log(N)
            return                                  # 1
                                                    # N^2 * log(N) + N^2 + 3*log(N) + C

    12.
    These 2 code blocks look similar but have different runtimes in big O notation.
    How are they different? Why?
        A: has a runtime of O(N)
        B: has a runtime of O(log N)^2)
        The inner (for) loops have different dependencies. (A) depends on the outer (while) loop, while (B) does not.
        This can produce fundamentally different behavior, here: the for loop is doubling (inner) log(n) (outer) times.
        Therefore, 2^log2(n) -> O(n)

        # Block (A)
        def fn_a(N):
          count = 0
          i = 1
          while i < N:
              for j in range(0, i):
                  count += 1
              i = i * 2
          return count

        # Block (B):
        def fn_b(N)
          count = 0
          i = 1
          while i < N:
              for j in range(0, N):
                  count += 1
              i = i * 2
          return count

Linked List

    1. (a) What is a linked list? (b) How is it built? (c) What is the underlying data structure used?
        (a) a linked list is a series of nodes connected by references to the next node.
        (b) linked lists are built by connecting new nodes the last linked node (either a dummy, head, or last node)
        (c) the underlying data structure of linked lists is a node, which typically contains data (e.g. value) and a
        reference to the next node

    2. What is the runtime to insert an element to the front of a linked list?
        as we'll already have a direct reference to the element, and the remaining operations are constant, O(1)

    3. What is the runtime to search if a specific element is in a linked list?
        in the worst the sought element will be the last element, hence, n, or O(n)

    4. What is one example of when a linked list is preferred over an array of a fixed size?
        1. when the required list size is not known: linked lists are space optimal vs allocating fixed size arrays
        2. frequent insertion/deletions: insertion/deletions do not require shifting other elements
        3. ...

    5. What is one example of when an array of fixed size is preferred over a linked list?
        1. small data set
        2. where size is fixed, and unchanging
        3. maximum memory/runtime performance is sought
        4. ...

    6. Describe how you would insert an element into the front of a linked list. How is this different from inserting to
    the end of one?
        pseudo code:
            assign the new node's next_node reference to the current head node
            reassign the head node reference to the new node
        to insert a new node to the end of a linked list (append), you must first traverse the list or otherwise obtain
        a reference to the last node

    7. How would you identify if there is a cycle in a linked list?
        1. either use Floyd's cycle section algorithm (fast & slow pointers)
        2. keep track of visited nodes

    8. Please walk through your approach using the following examples, including all intermediate steps.

        Linked list with cycle (d -> a)
        a --> b --> c --> d
        ^                 |
        |                 V
        <-----------------

        1. Floyd's cycle detection:
            p1 & p2 start head
            while p2 not None and p2.next not None and p1 != p2
                p1 move 1
                p2 move 2

            p1 = p2 = a
            p1.next = b
            p2.next.next = c
            b ?= c
            p1.next = c
            p2.next.next = a
            c ?= a
            p1.next = d
            p2.next.next = c
            d ?= c
            p1.next = a
            p2.next.next = a
            a ?= a
            return True

        2. record seen:
            p1 start head
            while not None
                check for seen
                record node

           record a
           a.next = b
           seen b?
           record b
           b.next = c
           seen c?
           record c
           c.next = d
           seen d?
           record d
           d.next = a
           seen a?
           return True

         Linked list with no cycle 1 --> 4 --> 3 --> 2 --> None

        1. Floyd's cycle detection:
            p1 & p2 start head
            while not None and p1 != p2
                p1 move 1
                p2 move 2

            p1 = p2 = 1
            p1.next = 4
            p2.next.next = 3
            4 ?= 3
            p1.next = c
            p2.next.next = a
            c ?= a
            p1.next = d
            p2.next.next = c
            d ?= c
            p1.next = a
            p2.next.next = a
            a ?= a
            return True

        2. record seen:
            p1 start head
            while not None
                check for seen
                record node

            record 1
            1.next = 4
            seen 4?
            record 4
            4.next = 3
            seen 3?
            record 3
            3.next = 2
            seen 2?
            record 2
            2.next = None
            return False

    9. Explain how you would reverse a linked list. Explain using the following example.

        a. 1 --> 4 --> 3 --> 2 --> None

    10. How do you iterate through a linked list? Describe this process in detail if you want to print every element in
    a linked list.
        node = head
        while node:
            print(node.val)
            node = node.next

        starting with the head of the linked list as your inspected_node, print the value of this node (assuming it's
        not a dummy node), then assign the destination of the current next_node pointer as the inspected_node_pointer

    11. How can we use linked lists to implement a stack?
        insertions replace the head, which represents the top of the stack; O(1) time

    12. Why do you need two pointers for a queue but not required to implement a stack?
        within the context of maintaining constant runtime for insertions and removals:
            queues require two pointers; one pointer for inserting new nodes, and one pointer for removing from the
            queue whereas a stack requires only one pointer at the head (the top of the stack)

    13. When would you want to use a doubly linked list?
        when bidirectional traversal is required or otherwise advantageous

    14. What are the differences between stack/queue/deque? What are their core functions and runtimes?
        stack: LIFO; add O(1); remove O(1); space O(n)
        queue: FIFO; add inverse of remove O(1) or O(n); remove inverse of add O(n) or O(1); space O(n)
        deque: FIFO or LIFO; add O(1); remove O(1); space O(n); note: runtime optimal implementation of a queue
        insert is O(n) for all

    15. What are some challenges when iterating through a circular linked list?
        finding the relative location of cycle entry node

    16. Why are queues better than stacks for ticket lines?
        maximizes fairness (i.e. "situational independence") by minimizing temporal mode deviation between customers

Linked List Code Analysis

    Below is a LinkedList class.

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None


    class LinkedList:
        def __init__(self, node):
            # head references first node in chain of nodes
            self.head = node

        def function1(self, new_node):
            new_node.next = self.head
            self.head = new_node

        def function2(self, new_node):
            if self.head is None:
                self.head = new_node
            return

            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = new_node

        def function3(self):
            if self.head:
                self.head = self.head.next

    1. Describe function1 and its runtime.
        inserts a new node as the head of the linked list; O(n)

    2. Describe function2 and its runtime.
        inserts the provide node into an empty linked list, if the list is empty
        if not, traverses to the end of the list, and appends the provided onto the end of the list

    3. Describe function3 and its runtime.
        via traversal, reassigns the head of the linked list to the next node until the assignment is None...
        without a reference to the head node, this will effectively delete the linked list
        (self.head = None) is O(1) while function3 is O(n)


Stacks

    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.pop())

    1. What is printed when the above code is run?
        2\n4\n3\n

    2. What is the current state of the stack after the above code is run?
        stack(1, )

    3. Give one real-life example of a Stack.
        things placed on top of each other, such as plates

Queues

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.dequeue())
    print(queue.dequeue())

    1. What is printed when this code is run?
        1\n2\n3\n

    2. What is the current state of the queue after this code is run?
        queue(4, )

    3. Give one real-life example of a Queue.
        standing in a line to, e.g. buy tickets

"""