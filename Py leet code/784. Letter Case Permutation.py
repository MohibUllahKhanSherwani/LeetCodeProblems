# Given a string s,
# you can transform every letter individually to be lowercase
# or uppercase to create another string.

# Return a list of all possible strings we could create. 
# Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Example 2:

# Input: s = "3z4"
# Output: ["3z4","3Z4"]

# Approach:
# 1.Start with a base case of [""] in the output to allow 
# the first character to build on an empty string. 
# 2.For each character:

# If it's a letter, I create two new permutations — one with the lowercase version and one with the uppercase version — for every string built so far.
# If it's a non-letter, I simply extend each current string with the character.
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Our output variable, it will contain all the permutations
        res = [""]
        # Each character in the string
        for char in s:
            temp = []
            # If the char is an alphabet(a-z, A-Z)
            if char.isalpha():
                for r in res:
                    # Append the new character's lower and upper case to all the existing res
                    temp.append(r + char.lower())
                    temp.append(r + char.upper())
            # If the char is a digit append all the res with the digit
            else:
                for r in res:
                    temp.append(r + char)
            # Update the res
            res = temp
        return res


s = Solution()
st = "a1b2"
print(s.letterCasePermutation(st))