
# Given an integer array nums, return all the triplets
#  [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order 
# of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.


# Basic approach: run three for loops checking if nums[i] + nums[j]
# + nums[k] == 0 and if the current numbers already exist in the 
# resultant array dont include them

# Optimal 1: Sort nums
#  Run a for loop for i in range len(nums)
# Take j = i + 1, and k = len(nums) - 1
# Run a while loop while j < k. If nums[i] + nums[j] + nums[k] == 0:
# Check if the triplet is already existing in the resultant array
# if not then append it to res,
# If nums[i] + nums[j] + nums[k] > 0 move k inward (k -= 1)
# else move j outward j += 1

# Most Optimal:
# Take res[]
# Run a for loop for i in range len(nums)
# Check if i > 0 and nums[i] == nums[i - 1] then continue (skip duplicates)
# and i > 0 is necessary so nums[i - 1] doesnt access an 
# index out of range
# Take j = i + 1, and k = len(nums) - 1
# Run a while loop while j < k. If nums[i] + nums[j] + nums[k] == 0:
# Append the triplet to res
# To skip duplicates run a while loop while j < k
# and nums[j] == nums[j + 1] subtract 1 from j (j += 1)
# and then just outside this while loop subtract 1 from k and add 1 to j
# If nums[i] + nums[j] + nums[k] > 0, subtract 1 from k (k -= 1)
# else move j outward j += 1
# Return res
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        
        # Basic:
        # for i in range(len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if (nums[i] + nums[j] + nums[k] == 0):
        #                 new_triplet = sorted([nums[i], nums[j], nums[k]])
        #                 if new_triplet not in res:
        #                     res.append(new_triplet)

        # Optimal 1:
        # for i in range(len(nums)):
        #     j = i + 1
        #     k = len(nums) - 1
        #     while j < k:
        #         if nums[i] + nums[j] + nums[k] == 0:
        #             new_triplet = [nums[i], nums[j], nums[k]]
        #             if new_triplet not in res:
        #                 res.append(new_triplet)
        #         if nums[i] + nums[j] + nums[k] > 0:
        #             k -= 1
        #         else:
        #             j += 1
        res = []
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        if (nums[0]) > 0:
            return []
        for i in range (len(nums)):
            # Skipping duplicates
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    # Append nums[i], j and k to res
                    res.append([nums[i], nums[j], nums[k]]) 
                    # Skipping duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # Move k inward and j outward as current
                    # j and k have been used    
                    k -= 1
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
        return res
nums = [-1,0,1,2,-1,-4]
s = Solution()
print(s.threeSum(nums))