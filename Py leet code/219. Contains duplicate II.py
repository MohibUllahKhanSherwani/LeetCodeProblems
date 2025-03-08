# Given an integer array nums and an integer k, 
# return true if there are two distinct indices 
# i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:


# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Basic approach is to use two loops and check for the conditions
# But this approach fails on larger inputs

# Optimal approach: Create an empty dict, run a for loop
# if the current nums[i] is not in the dict add it to the set
# else check if abs(dict[nums[i]] - i) <= k, if true return true
# else add update dict[nums[i]] = i, to the new i so that 
# the difference abs(i - j) <= k is calculated correctly

# Optimal 2: Create an empty dict, run a for loop if 
# the current nums[i] is in dict and abs(dict[nums[i]] - i) <= k
# return true else add it to the dict
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = {}
        for i in range(len(nums)):
            if nums[i] in num_set and abs(num_set[nums[i]] - i) <= k:
                return True
            num_set[nums[i]] = i
            # if nums[i] not in num_set:
            #     num_set[nums[i]] = i
            # else:
            #     if abs(num_set[nums[i]] - i) <= k:
            #         return True
            #     num_set[nums[i]] = i
        print(num_set)
        
        return False
s = Solution()       
nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))
nums = [1,0,1,1]
k = 1
print(s.containsNearbyDuplicate(nums, k))
nums = [1,2,3,1,2,3]
k = 2
print(s.containsNearbyDuplicate(nums, k))
