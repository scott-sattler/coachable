'''

"abcabcbb"
 ^   ^

"abcabcbb"
 ^
   ^

"abfuiopcabcbb"
 ^
        ^

        8
"abfuiopcaglo"
       ^
            ^
           10


"abfaglo"
 ^
  ^
{'a': 1}

"abfaglo"
 ^
  ^
{'a': 1, b: 1}

"abfaglo"
 ^
   ^
{'a': 1, b: 1, f: 1}

"abfaglo"
  ^
    ^
{'a': 1, b: 1, f: 1}


"cmabfaglo"
 ^
     ^
{'c': 1, 'm': 1, 'a': 1, b: 1, f: 1}

"cmabfaglo"
 ^
      ^
{'c': 1, 'm': 1, 'a': 2, b: 1, f: 1}
max = (6 - 1)

"cmabfaglo"
    ^
      ^
{'a': 1, b: 1, f: 1}
max = 5


"bbbbb"


"pwwkew"


scan until repeat
    character already scanned

O(1) lookups

two pointers with hash map

expand until


look next
increment forward/right pointer


# can also use array
# ord(char)



# if char is not in hash map
    # add to hash map
    # increment right pointer
# else: (if char is in hash map)
    # increment left pointer until:
    # value is removed or pointer is equal to right



# todo: deeper dive

'''


class Solution:
    # O(n) time
    # O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        seen = set()
        maxi = 0
        l = r = 0
        while r < len(s):
            if not (s[r] in seen):
                seen.add(s[r])
                r += 1
                maxi = max(maxi, r - l)
            else:  # s[r] in seen
                seen.remove(s[l])
                l += 1

        return maxi
