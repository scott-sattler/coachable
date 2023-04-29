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

        compute closed forms todo

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
        todo

    6. Compute 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32.
        todo

    7. If you keep adding more terms to the geometric series, what does it look like you get closer to? I.e., what does
    the series 1 + 1/2 + 1/4 + 1/8 + .... equal?
        todo

    8. Now assume the sum goes from 64 down to 0 like this:
        a. 64 + 32 + 16 + 8 + 4 + 2 + 1 + 1/2 + 1/4 + 1/8... What is this equal to?
            todo

    1. Compute  9 + 90 + 900 + 9000 as a power of 10 minus an additional term.
        todo

    1. What does 9000 + 900 + 90 + 9 + 9/10 + 9/100 + ... approach?
        todo

    1. Compute 54 + 27 + 9 + 3 + 1.
        todo

    1. Generalizing a sum of powers of 3, estimate 1 + 3 + 9 + ... + 3^n.
        a. What is the sum in terms of big O notation?
            todo

        b. Try to get an exact answer in terms of n
            todo


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
        TODO: verify
        multiply them

    5. Give an example of an algorithm or write a function with O(1) runtime.
        def square(n: int):
            return n ** 2

    6. Given a table of code runtime (input size/runtime), can you determine what order of growth these functions have?
    Hint: Applying the doubling principle.
        TODO: verify
        N (input)           100     200     300     400     500     600
        Code A Runtime      52      110     160     198     256     308       +58   +50   +38   +58   +52  -> N*k
        Code B Runtime      1001    1012    1015    1023    1025    1026      +11   +3    +8    +3    +1   -> (log N)*k
        Code C Runtime      52      183     341     779     1245    1831      +131  +158  +438  +466  +586 -> N^2


Explain and Analyze Code

    Please answer the following for each block of code. You can assume nums is an integer array of size n

        a. Determine the function for nums = [1,1,1,1,1]

        b. Determine the function for nums = [1,2,3,4,5]

        c. Suppose nums = [i for i in range(0, n)] Approximate the number of computations required to compute func(nums)
        for n = 2, 4, 8, 16, 32.

        d. What does this function do?

        e. What is the runtime complexity? And why?

        f. What is the space complexity? And why?

    1.
        def func_one(nums) -> int:
            n = len(nums)
            all_nums = []
            for i in range(n):
                for j in range(n):
                    all_nums.append(nums[j])
            output = 0
            for value in all_nums:
                output += value
            return output

    2.
        def func_two(nums) -> int:
            n = len(nums)
            value = 0
            for i in range(n):
                for j in range(n):
                    value += nums[j]
            return value

    3.
        def func_three(nums) -> int:
            n = len(nums)
            value = 0
            while n > 0:
                value += nums[n - 1]
                n //= 2
            return value


    4.
        def func_four(nums) -> int:
            double_nums = []
            for num in nums:
                double_nums.append(num + num)
            return sum(double_nums)


    5.
        def func_five(nums) -> int:
            power_sum = 1
            for i in range(len(nums)):
                for j in range(nums[i]):
                    power_sum *= 2

            total = 0
            for i in range(power_sum)
                total += 1
            return total % 99


    6.
        def func_six(nums) -> int:
            count = 0
            for i in range(1, len(nums)-1):
                if nums[i] < nums[i-1] * 2 and nums[i] > nums[i+1] / 2:
                    count += 1
            return count


    7.
        def func_seven(nums: list[int]):
          N = len(nums)
          total = 0
          n = N
          while n > 0:
              for i in range(0, n):
                  total += nums[i]
              n = n // 2
          return total

    8.
        def func_eight(nums: list[int]):
          N = len(nums)
          total = 0
          i = 1
          while i < N:
              for j in range(0, i):
                  total += nums[j]
              i = i * 2
          return total


    9.
        def func_nine(nums: list[int]):
          N = len(nums)
          total = 0
          i = 1
          while i < N:
              for j in range(0, N):
                  total += nums[j]
              i = i * 2
          return total

    10.
        # input: an arbitrarily large array of integers of size N
        def func_10(arr: list[int]):
            arr.sort() # This line is O(n log n) runtime.
            reverse_arr = [arr[i] for i in range(len(arr)-1, -1, -1)]
            complements = []

            # zip just iterates through both arrays at the same time
            for num1, num2 in zip(arr, reverse_arr):
                complements.append(num1 + num2)

          return compliments


    11.
    For this problem, just compute the runtime of func_11:

        # This function has log(N) runtime
        # Where N is the input integer
        def helper_func(N):
              # does something that takes log(N) runtime.
              # Note that if N = 1, then the runtime is O(1)


        # input: an arbitrarily large integer N
        def func_11(N):
            helper_func()
            for i in range(N):
                helper_func(i)
                for j in range(N):
                      helper_func(j)
                helper_func(N)
            return


    12.
    These 2 code blocks look similar but have different runtimes in big O notation.
    How are they different? Why?

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


    9. Explain how you would reverse a linked list. Explain using the following example.

        a. 1 --> 4 --> 3 --> 2 --> None

    10. How do you iterate through a linked list? Describe this process in detail if you want to print every element in
    a linked list.

    11. How can we use linked lists to implement a stack?

    12. Why do you need two pointers for a queue but not required to implement a stack?

    13. When would you want to use a doubly linked list?

    14. What are the differences between stack/queue/deque? What are their core functions and runtimes?

    15. What are some challenges when iterating through a circular linked list?

    16. Why are queues better than stacks for ticket lines?

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

    2. Describe function2 and its runtime.

    3. Describe function3 and its runtime.

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