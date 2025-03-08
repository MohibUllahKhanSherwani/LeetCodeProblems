#Given an integer array nums, return true if any
#value appears at least twice in the array,
#and return false if every element is distinct.


#Solution: Simply check for duplicates in a nested loop(Ineffecient)
#Convert to a set, it does not allow duplicate values. If length of
#list and set is same means no duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        num_set = set(nums)
        if (len(num_set) == len(nums)):
            return False
        return True

nums = [1, 2, 3, 1]
s = Solution()
print(s.containsDuplicate(nums))       
