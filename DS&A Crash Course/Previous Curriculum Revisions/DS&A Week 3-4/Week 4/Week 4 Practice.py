"""
Strings, Sorting Algorithms

Free Response Questions

Strings

    What is a string? How is a string created in memory?
    immutable object of str type; as an interned dictionary
    in CPython they adopt C's implementation: an array of chars
    details beyond that point get hairy...

    How can we calculate the frequencies of each character in a string?
    frequency map

    What is an anagram? How can we check if 2 strings are an anagram?
    same chars and frequency

    What are 2 ways to determine if a string is a palindrome?
    compare reverse
    two pointers -> <- or <- -> (inward better?)

    What is the runtime to concatenate a string with a character?
    Python: O(len(str) + len(char)) -> O(N+M)
    array-strings: O(1)

    What is the difference between substring vs. subsequence?
    substring is contiguous, and includes empty strings
    subsequence: remove (all > x >= 0) chars from string

    Let s = 'coachable rocks'. Can you give an example of a subsequence of s that is not a substring s? What about a
    substring that is not a subsequence?
    subsequence not a substring: coc
    substring not a subsequence: ""

Sorting

    What does it mean to sort an array?
    arranging in an ordered sequence

    How does sorting work for strings?
    alphabetically (or alphanumerically)

    What do you need to do if you are sorting objects? How is it different from strings, integers, etc?
    map each object to an order-able sequence
    some objects, such as letters/integers, have an existing sequential order

    Describe how selection sort works and its runtime and space complexity
    ascending; iterative; worst-case
    iterating from left to right, find then swapping the next smallest value with the current index
    O(n^2); O(1)

    Describe how insertion sort works and its runtime and space complexity
    ascending; iterative; worst-case
    iterates from left to right, selecting the next object, and inserting it after the first object less than it
    O(n^2); O(1)

    Describe how merge sort works and its runtime and space complexity
    ascending; recursive; worst-case
    bifurcate list until size of 1, merge sorted arrays until completely sorted
    O(nlog(n)); O(n)

    Describe how quick sort works and its runtime and space complexity
    ascending; recursive; worst-case
    from a pivot, arranges elements < = >, the = element(s) are now in their final position, recurse on L/R sub-arrays
    O(n^2); O(log(n)) (call stack); note that worst case can be made very unlikely, average is O(nlog(n))

    Suppose we have applied quicksort to a list and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could
    have been the pivot element in a previous iteration?
    any elements that satisfy: < = >
    by element value: 2 & 3

    What's different between quicksort and mergesort? What are the tradeoffs between the two?
    mergesort better worst-case time complexity O(nlog(n))
    quicksort efficient for small datasets; in-place; space complexity O(log(n)) vs O(n)
    mergesort can be better for larger datasets
    quicksort good cache locality
    probability of quicksort's worst-case runtime O(n^2) can be minimized
    mergesort is stable; quicksort is unstable
    mergesort external; quicksort internal
    mergesort equally efficient for all inputs of same size
    quicksort may depends on pivot selection

    What does divide and conquer mean? Which sorting algorithms use this approach?
    to recursively divide the problem into similar, more easily solvable subproblems
    mergesort; quicksort

    What is the difference between 3-way quicksort and standard quicksort?
    3-way handles duplicate elements better; < = > vs < >

    Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster
    here?
    input with multiple duplicates; fewer swaps

    Suppose you have an array with only 5 distinct elements (only the numbers 1-5).

        What is the worst-case runtime of quicksort? Why?
        O(n^2); elements can be arranged to achieve worst case

        What is the worst-case runtime of 3-way quicksort? Why?
        O(n^2); elements can be arranged to achieve worst case

Match Sorting Algorithms

    Here is an array that we're trying to sort several different ways. We'll provide the intermediate sorting stage, and
    you'll need to determine which sorting algorithm was used. We'll give you the first one as an example.

    Make sure to explain your answer qualitatively - do not say, "I ran the code, and this was an intermediate step I
    saw in the output."

    For some of them, multiple algorithms might apply. List as many as you can.

    Initial and Sorted Input

    (initial) [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
    (sorted)  [0, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 21, 24, 27]

    Intermediate Stages To Identify

    a) [0, 2, 3, 5, 27, 21, 17, 10, 16, 7, 24, 8, 4, 6, 18, 15]
        insertion sort: rightmost elements do not appear to have been moved; leftmost consistent with selection
        leftmost exact match to final position
    b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]
        quicksort: if 7 is chosen as the pivot, left/right subarrays are consistent with less/greater than ordering
    c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]
        insertion sort: rightmost elements do not appear to have been moved; leftmost consistent with insertion
        leftmost in order, but not necessarily in final position
    d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]
        mergesort: pairs of 2 are properly ordered (bottom up)

    Example Answer

        (a) is selection sort because the array  0,2,3,5 contains the smallest elements of the array in order - they are
        in the final positions for the sorted array. The other elements are primarily untouched, except for those that
        had 0,2,3,5 in their original positions.

    Do this for each intermediate stage provided.

"""
