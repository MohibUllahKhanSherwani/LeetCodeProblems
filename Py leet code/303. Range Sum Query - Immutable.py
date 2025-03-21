# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left 
# and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

# Optimal Approach:
# 1. Create a prefix sum array of length len(nums) + 1
# 2. Assign self.prefix_sum = [0] * (len(nums) + 1)
# 3. Run a for loop for i in range(1, len(nums) + 1)
# 4. Assign self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1] (Every index i basically stores the sum of nums[0] upto nums[i-1])
# 5. Inside the subRange function return the prefix_sum of right + 1 - prefix_sum of left

from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
nmArray = NumArray([-2, 0, 3, -5, 2, -1])
print(nmArray.sumRange(0, 2)) #[0, 2]
# Basic solution: 
# Assign self.nums = nums
# Take a var sum = 0
# Run a loop through range(left, right + 1)
# Add nums[i] to sum
# Return sum