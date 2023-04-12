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

    2. We say a series "converges" if you can compute the sum. What types of geometric series converge? You don't need
    to prove it - just describing it is fine. You can also use examples to explain your idea.

    3. Compute 1 + 2 + 4 + 8 + 16 + 32 + 64 as a power of 2 minus an additional term.

    4. Compute 64 + 32 + 16 + 8 + 4 + 2 + 1 as a power of 2 minus an additional term.

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


"""