'''
Strings, Sorting Algorithms

Free Response Questions

Strings

    What is a string? How is a string created in memory?
        a data type that consists of a sequence of characters
        in Python, strings are immutable
        todo: How is a string created in memory?

    How can we calculate the frequencies of each character in a string?
        performantly: iterate over the string, {'char': int(frequency)}

    What is an anagram? How can we check if 2 strings are an anagram?
        any word that can be made from exactly the letters of another word
        both strings have same letter frequency

    What are 2 ways to determine if a string is a palindrome?
        reverse the sting and compare to original
        compare first/last elements, move inwards (0, -1; 1, -2; ...)

    What is the runtime to concatenate a string with a character?
        depends on whether an optimization exists for the specific case
        worst case is O(n + m) where n and m are the sizes of the strings

    What is the difference between substring vs. subsequence?
        substrings are contiguous slices of a string, including an empty string
        subsequences are any properly ordered subset of a sequence

    Let s = 'coachable rocks'. Can you give an example of a subsequence of s that is not a substring s? What about a
    substring that is not a subsequence?


    How many possible substrings are there of a string of length N?
        '' + 1 * n + 2 * (n - 1)

    How many possible subsequences are there of a string of length N?


Sorting

    What does it mean to sort an array?

    How does sorting work for strings? How is different than sorting arrays?

    What do you need to do if you are sorting objects? How is it different from strings, integers, etc?

    Describe how selection sort works and its runtime and space complexity.

    Is this a stable sorting algorithm? Explain why or why not.

    Describe how insertion sort works and its runtime and space complexity.

    Is this a stable sorting algorithm? Explain why or why not.

    Describe how merge sort works and its runtime and space complexity.

    Is this a stable sorting algorithm? Explain why or why not.

    Describe how quick sort works and its runtime and space complexity.

    Is this a stable sorting algorithm? Explain why or why not.

    Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could have been the pivot element in a previous iteration?

    What's different between quicksort and mergesort? What are the tradeoffs between the two?

    What does divide and conquer mean? Which sorting algorithms use this approach?

    What is the difference between 3-way quicksort and standard quicksort?

     Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster here?

    Suppose you have an array with only 5 distinct elements (only the numbers 1-5). Note the array is still of arbitrarily large size N so it could be [1,2,3,4,1,2,3,4,4,4,4,3,2,3,2,....] with many duplicates. For an array like this.

    What is the worst-case runtime of quicksort? Why?

    What is the worst-case runtime of 3-way quicksort? Why?

Trace Sorting Algorithms

Trace out all the intermediate steps on the string "COACHABLEROCKS" for each of the following sorting algorithms. You don't need to include every swap, but you should include the most important intermediate steps.

    1. Insertion Sort

    2. Selection Sort

    3. Quicksort (No Shuffle)

    4. Quicksort 3-way (No Shuffle)

    5. Mergesort Bottom Up

    6. Mergesort Top Down

Match Sorting Algorithms

Here is an array that we're trying to sort several different ways. We'll provide the intermediate sorting stage, and you'll need to determine which sorting algorithm was used. We'll give you the first one as an example.

 Make sure to explain your answer qualitatively - do not say, "I ran the code, and this was an intermediate step I saw in the output."

For some of them, multiple algorithms might apply. List as many as you can.

Initial and Sorted Input

(initial) [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
(sorted)  [0, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 21, 24, 27]

Intermediate Stages To Identify

a) [0, 2, 3, 4, 5, 21, 17, 10, 16, 7, 24, 8, 27, 6, 18, 15]
b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]
c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]
d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]

Example Answer

(a) is selection sort because the array  0,2,3,4, 5 contains the smallest elements in order - they are in the final positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,5 in their original positions.

Do this for each intermediate stage provided.

Substring Matching Algorithms

Knuth Morris Pratt

Consider the input string S = 'ABCABDABCA' and the substring P = 'ABCA'. Walk through the steps of the Knuth-Morris-Pratt algorithm to find all occurrences of P in S. Show the intermediate values of the failure function and the table used to match the characters in P against S. Indicate the starting index of each occurrence of P in S, and explain how the algorithm identifies each occurrence.

Rabin Karp

Consider the input string S = 'ABCCABCABCA' and the substring P = 'ABC'. Walk through the steps of the Rabin-Karp algorithm to find all occurrences of P in S, using a hash function that maps each character to its ASCII code. Assume a prime base number of 101. Show the intermediate hash values for each P window in S, and explain how the algorithm identifies each occurrence. Note any false positives the algorithm might produce, and explain why they occur.

Boyer-Moore

Consider the input string S = 'ABCBACBABCA' and the substring P = 'ABC'. Walk through the steps of the Boyer-Moore algorithm to find all occurrences of P in S. Show the tables used to implement the 'bad character' and 'good suffix' rules, and indicate the starting index of each occurrence of P in S. Explain how the algorithm identifies each occurrence and how it uses the 'bad character' and 'good suffix' rules to skip unnecessary comparisons. Note any edge or corner cases the algorithm needs to handle, and explain how it handles them.


'''