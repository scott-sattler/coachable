"""
Free Response Questions

Strings

    What is a string? How is a string created in memory?

    How can we calculate the frequencies of each character in a string?

    What is an anagram? How can we check if 2 strings are an anagram?

    What are 2 ways to determine if a string is a palindrome?

    What is the runtime to concatenate a string with a character?

    What is the difference between substring vs. subsequence?

    Let s = 'coachable rocks'. Can you give an example of a subsequence of s that is not a substring s? What about a
    substring that is not a subsequence?

Sorting

    What does it mean to sort an array?

    How does sorting work for strings?

    What do you need to do if you are sorting objects? How is it different from strings, integers, etc?

    Describe how selection sort works and its runtime and space complexity

    Describe how insertion sort works and its runtime and space complexity

    Describe how merge sort works and its runtime and space complexity

    Describe how quick sort works and its runtime and space complexity

    Suppose we have applied quicksort to a list and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could
    have been the pivot element in a previous iteration?

    What's different between quicksort and mergesort? What are the tradeoffs between the two?

    What does divide and conquer mean? Which sorting algorithms use this approach?

    What is the difference between 3-way quicksort and standard quicksort?

    Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster
    here?

    Suppose you have an array with only 5 distinct elements (only the numbers 1-5).

    What is the worst-case runtime of quicksort? Why?

    What is the worst-case runtime of 3-way quicksort? Why?

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
    b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]
    c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]
    d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]

    Example Answer

    (a) is selection sort because the array  0,2,3,5 contains the smallest elements of the array in order - they are in the final positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,5 in their original positions.

    Do this for each intermediate stage provided.
"""