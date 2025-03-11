# Given a non-empty array of integers nums, 
# every element appears twice except for one. 
# Find that single one.

# You must implement a solution with a linear 
# runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

# Optimal Approach:
# 1. Initialize a res var = nums[0] (It is a non-empty list so we can
# assume there is atleast 1 element)
# 2. Run a for loop for i in range(1, len(nums))
# 3. Add the bitwise XOR(^) of res and nums[i] to res
# 4. return res (It will be the only number that appears once)
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
        
s = Solution()
nums = [2,2,1]
print(s.singleNumber(nums))
nums = [4,1,2,1,2]
print(s.singleNumber(nums))

# Basic Approach: Brute force through the array and find,
# for each nums[i] how many nums[j] == nums[i] exist
# if count == 1 return the nums[i]
# for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#             if count == 1:
#                 return nums[i]
#         return nums[0]


# Optimal 1:
#  Sort the array
#  Iterate in steps of 2
# Check if nums[i] != nums[i+1]
# if true return nums[i]
# If loop finishes, return the last element
        # nums.sort()
        # for i in range(0, len(nums) - 1, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[-1]


# Optimal 2: Create an empty hashmap
# Iterate through the array, if the current num is in the dict
# increment its count, else add it to the dict
# Iterate through the hashmap, if the count is 1 return the key

# freq = {}
#         for num in nums:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1
#         for n in freq:
#             if freq[n] == 1:
#                 return n
