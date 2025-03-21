# Given an integer n,
# return an array ans of length n + 1
# such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


# Optimal Solution:
# 1. Initialize a list of length n + 1 with all 0s
# 2. set offset = 1
# 3. run a for loop through range 1 to n + 1
# 4. Check if we are at either 1, 2, 4, 8 (whenver i is a power of 2)using if offset * 2 == i
# 5. If true then offset = i
# 6. Finally assign ans[i] = 1 + ans[i-offset]
# 7. Return offset
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
        return ans    
            
s = Solution()

print(s.countBits(2)) # [0,1,1]

