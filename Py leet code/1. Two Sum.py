# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

#Basic approach: Run two loops one for i and another for j
#If nums[i] + nums[j] == target return [i, j]

#Optimal approach: Create a dictionary/hashmap, run a loop and add to the dictionary
# {nums[i], i} meaning nums[i] as the key, and i as the value
# Check if target - nums[i] is in the dictionary, if yes return i and hash_map[target - nums[i]]
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        for i in range(0, len(nums)):
            if target - nums[i] in hash_map:
                return [i, hash_map[target - nums[i]]]
            else:
                hash_map[nums[i]] = i #Store index of nums[i]

        #Basic approach
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]

s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
nums = [3, 2, 4]
target = 6
print(s.twoSum(nums, target))
nums = [3, 3]
target = 6
print(s.twoSum(nums, target))