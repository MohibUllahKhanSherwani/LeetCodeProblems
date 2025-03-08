# 448. Find All Numbers Disappeared in an Array


#Basic: There are duplicates in the list, so sort the list
#then check in the loop if ((nums [i] == nums[i-1] - 1 ) or nums[i] == nums[i+1])
#then skip that iteration if not then add to the resultant list
#This solves for nums = [4,3,2,7,8,2,3,1] but error in nums = [1,1]

#Optimal way is to convert to a set and then loop through the original list
# check every 'i', if i is not in set add it to the result list
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        to_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in to_set:
                result.append(i)
        return result
    

    
        #Not working for nums = [1,1]
        # nums = sorted(nums) 
        # for i in range(0, len(nums) - 1):
        #     if ((nums[i] == nums[i + 1] - 1) or (nums[i] == nums[i + 1])):
        #         continue
        #     else:
        #         nums.insert(i + 1, nums[i] + 1)
        #         result.append(nums[i] + 1)
        # return result
s = Solution()
nums = [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))
nums = [1, 1]
print(s.findDisappearedNumbers(nums))