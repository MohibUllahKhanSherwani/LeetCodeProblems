# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in 
# non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


# Basic approach: Take squares of the array and store in the same array
# return sorted array (Not good for larger inputs, In-efficient)
from typing import List
from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i] * nums[i]
        # return sorted(nums)

        # Optimal 1
        # res = []
        # left = 0
        # right = len(nums) - 1 
        # while (left <= right):
        #     l = abs(nums[left])
        #     r = abs(nums[right])
        #     if (r > l):
        #         res.append(r * r)
        #         right -= 1
        #     else:
        #         res.append(l * l)
        #         left += 1
        # return list(reversed(res))
        # res = []
        # left = 0
        # right = len(nums) - 1 
        # while (left <= right):
        #     l = nums[left] * nums[left]
        #     r = nums[right] * nums[right]
        #     if (r > l):
        #         res.append(r)
        #         right -= 1
        #     else:
        #         res.append(l)
        #         left += 1
        # return list(reversed(res))
        res = deque()
        left = 0
        right = len(nums) - 1 
        while (left <= right):
            l = nums[left] * nums[left]
            r = nums[right] * nums[right]
            if (r > l):
                res.appendleft(r)
                right -= 1
            else:
                res.appendleft(l)
                left += 1
        return list((res))

s = Solution()
nums = [-4,-1,0,3,10]
print(s.sortedSquares(nums))