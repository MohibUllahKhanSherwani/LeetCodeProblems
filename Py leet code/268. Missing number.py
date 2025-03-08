#Given an array nums containing n distinct numbers in the
#range [0, n], return the only number in the range that is
#missing from the array

#Basic approach: to sort the array and compare value against index
# if missing found return it, also include optional check to see if index + 1 is missing
# such as in case of [0, 1] --> where 2 is missing

#Optimal approach: Sum the given list vs what should be the expected output, then 
#Subtract and return the number

#Most optimal way is to use the formula of sum of n natural numbers
# (n * (n + 1)) / 2 simply return int (n * (n + 1) / 2 - sum(nums)), it will handle all cases
#such as nums = [0, 1] and nums = [1] USE n = len(nums)

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:  
        # nums = sorted(nums) Not a good solution as it takes nlog(n) to sort the array
        # for index, number in enumerate(nums):
        #     if index != number:
        #         return index
        # if (index + 1) not in nums:
        #     return index + 1
        # return None
        n = len(nums)
        print(n)
        return n * (n + 1) // 2 - sum(nums)
        # return sum(range(len(nums) + 1)) - sum(nums)

s = Solution()
nums = [0, 1]
nums = [1]
print(len(nums))
print(s.missingNumber(nums))
