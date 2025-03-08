# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is,
#    for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

#Basic approach: Run a for loop, initialize a count variable 
# then run another loop to check if arr[j] < arr[i], if true
# add 1 to count variable then outside the inner loop
# store the count variable as res[i] = count

# def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums)):
    #         count = 0
    #         for j in range(len(nums)):
    #             if (nums[j] < nums[i] and j != i):
    #                 count += 1
    #         res.append(count)
    #     return res

# Optimal approach: sort the list and store it in a temp var
# Create an empty hashset
# Run a loop through the sorted list and store in the set as 
# {number:index of number in sorted list}
# then create an empty list result
# run a for loop through the either the original list
# or temp (both are same length)and append result with dict[nums[i]],
# which is basically the amount of numbers smaller than that number 
# NOTE: Necessary to check if temp[i] not in dict: bcz in the case of multiple numbers
# like 2, 2 it will first store the index of the first two and then the second one
# which won't give the result

from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #nums = [8, 1, 2 ,2 , 3]
        dict = {}
        res = []
        temp = sorted(nums) # [1, 2, 2, 3, 8]

        for i in range(len(nums)): # {(1:0), (2:1), (3:3), (8:4)}
            print(i)
            if temp[i] not in dict: 
                dict[temp[i]] =  i
        print(dict)
        for i in range(len(nums)):
            res.append(dict[nums[i]])
        return res

        
nums = [8, 1, 2, 2, 3]
s = Solution()
print(s.smallerNumbersThanCurrent(nums))

