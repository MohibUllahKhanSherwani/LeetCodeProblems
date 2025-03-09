# Given an array of positive integers nums and 
# a positive integer target, 
# return the minimal length of a subarray whose sum 
# is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

 

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3]
# has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0



# APPROACH: 
# 1.Initialize a length var to infinity
# 2.Initialize a current_sum var = 0, left = 0
# 3.Run a for loop for right in range(len(nums))
# 4. add every nums[right] to current_sum (current_sum += nums[right])
# 5. Run another while loop, while current_sum >= target
# 6. update length = min(length, right - left + 1)
# 7. subtract nums[left] from current_sum (current_sum -= nums[left])
# 8. increment left (left += 1)
# 9. return length if it is infinity return 0 else return length
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        current_sum = 0
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                length = min(length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if length == float('inf'):
            return 0
        return length
target = 7
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))
target = 4
nums = [1,4,4]
print(s.minSubArrayLen(target, nums)) 