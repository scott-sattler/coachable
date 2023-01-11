from typing import List


def fibonacci_dp(nth: int) -> int:
    solutions: List[int] = [1, 1]

    if n == 0 or n == 1:
        return 1

    for i in range(0, n-1):
        next_fib = solutions[i] + solutions[i+1]
        solutions.append(next_fib)

    return solutions[-1]


for n in range(10):
    x = fibonacci_dp(n)
    print(x)

# 1 1 2 3 5 8 13 21 34 55

