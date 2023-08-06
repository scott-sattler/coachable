'''
Quiz 4

6. Which of the following best describes a hashmap collision?
×Two key-value pairs have equal keys, but different values.



10. What does this function do?

def f(n):
  if n == 0:
    return 0
  return f(n // 2) + f(n // 2) + n

Hint: Rather than solve this mathematically, think of other recurrence relations you know.

×NO ANSWER



28. Will this code work? Why or why not?

class Something:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y

  def __lt__(self, other: Something):
    return self.x > other.x

l = [Something(1,2), Something(3,4), Something(5,6)]
l.sort()
×No, the class Something is completely/partially missing a comparison function.



29. Suppose we wanted to implement the following sorting algorithm called radix sort.

Group all the strings with the same first character i.e. all strings starting with 'a', 'b','c',.....

[words starting with 'a'], [words starting with 'b',],....

Then for each group, recursively call radix sort but on the next character to further group the lists. Repeat this
process until the sublists are size 1.

What is the runtime of this sorting algorithm?

n = number of strings
k = average length of each string

×NO ANSWER



33. Compute f(64) for the following function.

def f(n: int) -> int:
    if n <= 4:
       return n
    return f(n // 2) + f(n // 4)
×NO ANSWER



37. What does the below code print?

def f(m: int, n : int) -> int:
  if min(m, n) <= 1:
     return 0
  return f(m // 2, n - 1) * f(m - 1, n//2) + m * n

print(f(5, 7))
×0

'''
