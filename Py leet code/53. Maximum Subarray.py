# Given an integer array nums, 
# find the subarray with the largest sum, and return its sum.


# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        total = 0
        for num in nums: 
            if total < 0:
                total = 0
            total += num
            res = max(total, res)
        return res


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))

# Optimal Approach: Constan Space
# 1. Initialize a res var = nums[0] (It is a non-empty list so we can
# assume there is atleast 1 element)
# 2. Initialize a total var = 0 (current_sum)
# 3. Run a for loop for i in range(len(nums))
# 4. Check if total < 0, if true set total = 0
# 5. Add nums[i] to total
# 6. assign res = max(total, res)
# 7. return res




# Basic Approach : Sliding window
# Create an array of length of nums filled with 0
# Iterate through the array and fill in the values 
# using the formula dp[i] = max(nums[i], dp[i - 1] + nums[i])
# Return the max of the array(dp)
# dp = [0] * len(nums)
#         dp[0] = nums[0]
#         for i in range(len(nums)):
#             dp[i] = max(nums[i], dp[i - 1] + nums[i])
#         return max(dp)