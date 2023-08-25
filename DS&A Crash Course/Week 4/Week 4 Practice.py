'''
Strings, Sorting Algorithms

Free Response Questions

Strings

    1. What is a string? How is a string created in memory?
        a data type that consists of a sequence of characters
        in CPython, strings are immutable
        generally, strings are a contiguous memory mapping of characters

    2. How can we calculate the frequencies of each character in a string?
        performantly: iterate over the string, {'char': int(frequency)}

    3. What is an anagram? How can we check if 2 strings are an anagram?
        any word that can be made from exactly the letters of another word
        both strings have same letter frequency

    4. What are 2 ways to determine if a string is a palindrome?
        reverse the sting and compare to original
        compare first/last elements, move inwards (0, -1; 1, -2; ...)

    5. What is the runtime to concatenate a string with a character?
        depends on whether an optimization exists for the specific case
        worst case is O(n + m) where n and m are the sizes of the strings

    6. What is the difference between substring vs. subsequence?
        substrings are contiguous slices of a string, including an empty string
        subsequences are any properly ordered subset of a sequence

    7. Let s = 'coachable rocks'. Can you give an example of a subsequence of s that is not a substring s? What about a
    substring that is not a subsequence?
        subsequence that is not substring: 'ca'
        substring that is not a subsequence: ''

    8. How many possible substrings are there of a string of length N?
        n + (n - 1) + (n - 2) ... + 1 => (1/2 * n * (n + 1)) + 1

    9. How many possible subsequences are there of a string of length N?
        2^n as each element may be present or absent for n elements


Sorting

    1. What does it mean to sort an array?
        impose order

    2. How does sorting work for strings? How is different than sorting arrays?
        a < b < c ... z, where ord(a) = 97, ord(b) = 98...
        in Python, sorting a string should be done using a char list, ultimately joined back into a string

    3. What do you need to do if you are sorting objects? How is it different from strings, integers, etc?
        assign an orderable attribute to each object
        integers are themselves an attribute with a defined orderable
        strings have, by convention, been assigned orderable attributes (and independently have order a < b < c...)
        whereas some objects require orderable assignment, e.g.: picture(cat) < picture(dog)

    4. Describe how selection sort works and its runtime and space complexity.
        subarrays: sorted : unsorted
        looking at next leftmost, find next (smallest), swap with next leftmost
        O(n^2) time complexity; O(n) input, O(1) auxiliary space

        a. Is this a stable sorting algorithm? Explain why or why not.
            yes when selecting leftmost and inserting. this implementation preserves stability
            no when swapping. this sawp operation is inherently unstable

    5. Describe how insertion sort works and its runtime and space complexity.
        subarrays: sorted : unsorted
        looking at next leftmost, bubble down sorted subarray until inserted into correct position
        O(n^2) time complexity
        O(n) input, O(1) auxiliary space complexity

        a. Is this a stable sorting algorithm? Explain why or why not.
            yes. the leftmost unsorted elements will remain leftmost when sorted (looking left, if arr[i] <= insert)

    6. Describe how merge sort works and its runtime and space complexity.
        bisect array until subarrays of size 1, merge increasingly larger subarrays by moving the lesser of the two to
        smaller, sorted subarrays, to a larger sorted subarray
        O(n * log n) time complexity
        O(n) input, O(log n) call stack, O(n) (arrays), O(1) (linked list), auxiliary space complexity

        a. Is this a stable sorting algorithm? Explain why or why not.
            yes. stability is preserved as long as equal left elements are moved before equal right elements

    7. Describe how quick sort works and its runtime and space complexity.
        pick pivot, move all lesser than to left of pivot, greater than to right of pivot
        O(n^2) (worst), Θ(n * log n) (average) time complexity
        O(n) input, O(log n) call stack, auxiliary space complexity

        a. Is this a stable sorting algorithm? Explain why or why not.
            no. swapping can result in instability

    8. Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements
    could have been the pivot element in a previous iteration?
        2 or 3

    9. What's different between quicksort and mergesort? What are the tradeoffs between the two?
        quicksort: O(n^2) (worst), Θ(n * log n) (average) time complexity
                   O(n) input, O(log n) call stack, auxiliary space complexity
                   unstable
        mergesort: O(n * log n) time complexity
                   O(n) input, O(log n) call stack, O(n) (arrays), O(1) (linked list), auxiliary space complexity
                   stable
                   parallelizable
                   can be tuned to better handle specific input types

        note: an in-place mergesort implementation exists
              numerous variations of both algorithms exist

    10. What does divide and conquer mean? Which sorting algorithms use this approach?
        divide and conquer is applicable to problems with optimal substructure
        what this means is that an optimal solution to a sub-problem, can be utilized on increasingly larger
        sub-problems until the whole problem (in the context of sorting, the whole array) is solved

    11. What is the difference between 3-way quicksort and standard quicksort?
        3-way, specifically Djikstra's variant, not a multi-partition variant, adds an equal-to partition

    12. Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster
    here?
        any input where where many elements are the same
        the equivalent elements are more quickly shifted into their correct positions

    13. Suppose you have an array with only 5 distinct elements (only the numbers 1-5). Note the array is still of
    arbitrarily large size N so it could be [1,2,3,4,1,2,3,4,4,4,4,3,2,3,2,....] with many duplicates. For an array like
    this.

        a. What is the worst-case runtime of quicksort? Why?
            O(n^2) occurs when the collection is maximally unbalanced
            example: already sorted list with pivot on far left
            (n - 1) elements compared, (n - 2) elements compared, (n - 3) elements compared... occurring n times

        b. What is the worst-case runtime of 3-way quicksort? Why?
            Djikstra's 3-way Quicksort, not a 2 pivot quicksort, retains a worst case time complexity of O(n^2)
            examining a completely sorted array of unique elements demonstrates that adding an equal-to partition fails
            to improve the worst case

Trace Sorting Algorithms

Trace out all the intermediate steps on the string "COACHABLEROCKS" for each of the following sorting algorithms. You
don't need to include every swap, but you should include the most important intermediate steps.

    1. Insertion Sort (swap)
        COACHABLEROCKS
        CAOCHABLEROCKS
        ACOCHABLEROCKS
        ACCOHABLEROCKS
        ACCHOABLEROCKS
        ACCHAOBLEROCKS
        ACCAHOBLEROCKS
        ACACHOBLEROCKS
        AACCHOBLEROCKS
        AACCHBOLEROCKS
        AACCBHOLEROCKS
        AACBCHOLEROCKS
        AABCCHOLEROCKS
        AABCCHLOEROCKS
        AABCCHLEOROCKS
        AABCCHELOROCKS
        AABCCEHLOROCKS
        AABCCEHLOORCKS
        AABCCEHLOOCRKS
        AABCCEHLOCORKS
        AABCCEHLCOORKS
        AABCCEHCLOORKS
        AABCCECHLOORKS
        AABCCCEHLOORKS
        AABCCCEHLOOKRS
        AABCCCEHLOKORS
        AABCCCEHLKOORS
        AABCCCEHKLOORS

    2. Selection Sort
        COACHABLEROCKS
        AOCCHABLEROCKS
        AACCHOBLEROCKS
        AABCHOCLEROCKS
        AABCCOHLEROCKS
        AABCCCHLEROOKS
        AABCCCELHROOKS
        AABCCCEHLROOKS
        AABCCCEHKROOLS
        AABCCCEHKLOORS

    3. Quicksort (No Shuffle)
        leftmost pivot
        COACHABLEROCKS
        AABCHOCLEROCKS
        AABCHOCLEROCKS
        AABCCCEHOROLKS
        AABCCCEHOROLKS
        AABCCCEHKLOROS
        AABCCCEHKLOORS
        AABCCCEHKLOORS
        AABCCCEHKLOORS
        AABCCCEHKLOORS

    4. Quicksort 3-way (No Shuffle)
        todo: verify
        COACHABLEROCKS
        AABCCCHLEROOKS
        AABCCCHLEROOKS
        AABCCCHLEROOKS
        AABCCCEHKLOORS
        AABCCCEHKLOORS
        AABCCCEHKLOORS
        AABCCCEHKLOORS
        AABCCCEHKLOORS

    5. Mergesort Bottom Up
        COACHABLEROCKS
        CO
        AC
        AH
        BL
        ER
        CO
        KS
        ACCO
        ABHL
        CEOR
        KS
        AABCCHLO
        CEKORS
        AABCCCEHKLOORS

    6. Mergesort Top Down
        COACHABLEROCKS
        AO
        ACO
        CH
        AB
        ABCH
        AABCCHO
        ER
        ELR
        CO
        KS
        CKOS
        CEKLORS
        AABCCCEHKLOORS

        implemented:
        COACHABLEROCKS
        AO
        ACO
        CH
        AB
        ABCH
        AABCCHO
        ER
        ELR
        CO
        KS
        CKOS
        CEKLORS
        AABCCCEHKLOORS


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

    a) [0, 2, 3, 4, 5, 21, 17, 10, 16, 7, 24, 8, 27, 6, 18, 15]
        selection sort: having selected 5 last, elements < 5 are properly sorted while elements > 5 are unsorted. this
                        is not insertion sort as elements in the sorted subarray have been swapped with elements outside
                        the sorted subarray

    b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]
        quick sort: with pivot 7, all left elements < pivot < all right elements
        quick sort 3-way: depending on the implementation 3-way exhibits identical behavior when no elements are equal

    c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]
        merge sort (top down): having just finished merging [4] [6] (or a larger subarray), top down merge sort would
                               show left subarrays properly sorted, while the right subarrays would be some degree of
                               sorted, close to their initial positions
        insertion sort: having finished inserting (bubbling down) the 0 element, elements to the left are properly
                        sorted while elements to the right are in their initial positions.

    d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]
        quicksort


    Example Answer

    (a) is selection sort because the array  0,2,3,4, 5 contains the smallest elements in order - they are in the final
    positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,5 in
    their original positions.

    Do this for each intermediate stage provided.

Substring Matching Algorithms

    Knuth Morris Pratt

    Consider the input string S = 'ABCABDABCA' and the substring P = 'ABCA'. Walk through the steps of the
    Knuth-Morris-Pratt algorithm to find all occurrences of P in S. Show the intermediate values of the failure function
    and the table used to match the characters in P against S. Indicate the starting index of each occurrence of P in S,
    and explain how the algorithm identifies each occurrence.
        failure function:
        [0, 0, 0, 1]

        'ABCABDABCA'
        'ABCA      '
        '    ?     '
        full match, jump to 'B'

        'ABCABDABCA'
        '   ABCA   '
        '     x    '
        fail at 'D', not present, full jump

        'ABCABDABCA'
        '      ABCA'
        full match, end of string


    Rabin Karp

    Consider the input string S = 'ABCCABCABCA' and the substring P = 'ABC'. Walk through the steps of the Rabin-Karp
    algorithm to find all occurrences of P in S, using a hash function that maps each character to its ASCII code.
    Assume a prime base number of 101. Show the intermediate hash values for each P window in S, and explain how the
    algorithm identifies each occurrence. Note any false positives the algorithm might produce, and explain why they
    occur.
        this implementation at O(n*m) is of a similar, or greater,
        complexity to using a perfect hash function of O(n + m).

        'ABC'
        ord('A') -> 65
        ord('B') -> 66
        ord('C') -> 67
        'ABC' -> (65 + 66 + 67) -> 198 % 101 -> 97

        'ABCCABCABCA' -> (65 + 66 + 67) -> 198 % 101 -> 97
        'ABC        ' -> (65 + 66 + 67) -> 198 % 101 -> 97
        potential match (implementation requires verification)

        'ABCCABCABCA' -> 97 - 65 + 67 -> 99
        ' ABC       ' -> 97

        'ABCCABCABCA' -> 98
        '  ABC      ' -> 97

        'ABCCABCABCA' -> 97
        '   ABC     ' -> 97
        potential match (implementation requires verification)
        this false positive is the result of the lossy hash function being used

        'ABCCABCABCA' -> 97
        '    ABC    ' -> 97
        potential match (implementation requires verification)

        'ABCCABCABCA' -> 97
        '     ABC   ' -> 97
        potential match (implementation requires verification)
        this false positive is the result of the lossy hash function being used

        'ABCCABCABCA' -> 97
        '      ABC  ' -> 97
        potential match (implementation requires verification)
        this false positive is the result of the lossy hash function being used

        'ABCCABCABCA' -> 97
        '       ABC ' -> 97
        potential match (implementation requires verification)

        'ABCCABCABCA' -> 97
        '       ABC ' -> 97
        potential match (implementation requires verification)

        'ABCCABCABCA' -> 97
        '        ABC' -> 97
        potential match (implementation requires verification)
        this false positive is the result of the lossy hash function being used


    Boyer-Moore

    Consider the input string S = 'ABCBACBABCA' and the substring P = 'ABC'. Walk through the steps of the Boyer-Moore
    algorithm to find all occurrences of P in S. Show the tables used to implement the 'bad character' and 'good suffix'
    rules, and indicate the starting index of each occurrence of P in S. Explain how the algorithm identifies each
    occurrence and how it uses the 'bad character' and 'good suffix' rules to skip unnecessary comparisons. Note any
    edge or corner cases the algorithm needs to handle, and explain how it handles them.
        todo


'''