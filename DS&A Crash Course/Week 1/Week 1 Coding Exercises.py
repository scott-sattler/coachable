from __future__ import annotations

'''
Write a function that appends the numbers or a string from 1 to n, inclusive, using the following rules:
1. If the number is a multiple of 3 and 5, append "Fizz Buzz"
2. If the number is just a multiple of 5, append "Buzz"
3. If the number is just a multiple of 3, append "Fizz"
4. If the number is neither a multiple of 3 nor 5, append then number as a string
'''
def fizz_buzz(n: int) -> list[str]:
  out = []
  for i in range(1, n + 1):
    fizz = i % 3 == 0
    buzz = i % 5 == 0
    if fizz and buzz:
      out.append('Fizz Buzz')
    elif fizz:
      out.append('Fizz')
    elif buzz:
      out.append('Buzz')
    else:
      out.append(str(i))
  return out

'''
Write a function that, given a list of integers, return the largest value in the list.
'''
def max_integer(input_list: list[int]) -> int:
  return max(input_list)

'''
Write a function that, given a list of integers, return the index of the largest integer in the list. 
If there are duplicates, return the earliest index.
'''
def max_integer_index(input_list: list[int]) -> int:
  max_index = 0
  max_value = float('-inf')
  n = len(input_list)
  for i in range(n):
    if input_list[i] > max_value:
      max_index = i
  return max_index

'''
Write a function that, given a list of tuples in the form (Student Name, Score), returns 
a dictionary where the key is the Student Name and the value is the Score for that student.

If a Student Name appears multiple times, take the score from the tuple at the largest index.
'''
def tuples_to_dictionary(input_list: list[tuple[str, int]]) -> dict[str, int]:
  return {k: v for k, v in input_list}

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a list of 
names of the students who got the highest score.
In the output, student names should be sorted alphabetically ascending. 
'''
def highest_scoring_students(input_dict: dict[str, int]) -> list[int]:
  return sorted([k for k, v in input_dict.items() if v == 100])

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of the form Score: Count. 
Suppose the input is { 'A': 100, 'B': 90, 'C': 90 }, then the output would be
{ 100: 1, 90: 2}
'''
def count_score_frequencies(input_dict: dict[str, int]) -> dict[int, int]:
  return {v: sum([1 for s in input_dict.values() if s == v]) for k, v in input_dict.items()}


'''
Write a function that, given a dictionary of the form Student Name: Score, returns the average score.
'''
def average_score(input_dict: dict[str, int]) -> float:
  return sum(input_dict.values())/len(input_dict)

'''
Write a function that, given a dictionary of the form Score: Count, returns the average score.
'''
def average_score_frequency_weighted(input_dict: dict[int, int]) -> float:
  return sum([k*v for k, v in input_dict.items()])/sum(input_dict.values())

'''
Write a function that, given a dictionary of the form Student Name: Score, returns a dictionary
of letter grades. Here, A is 90 to 100 inclusive, B is 80 to 89 inclusive, C is 70 to 79 inclusive, and anything else is an F.
'''
def convert_to_gradebook(input_dict: dict[str, int]) -> dict[str, int]:
  return [
    out := {},
    letter := lambda e: chr(99 - ((e - 70) // 10)).capitalize() if 69 < e < 99 else (letter(e - 1) if e > 69 else chr(102).capitalize()),
    [out.update({letter(v): 1}) if letter(v) not in out else out.update({letter(v): out[letter(v)] + 1}) for k, v in input_dict.items()]
  ][0]  # D:
