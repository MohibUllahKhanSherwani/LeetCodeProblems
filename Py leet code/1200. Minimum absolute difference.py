# Given an array of distinct integers arr, 
# find all pairs of elements with
# the minimum absolute difference of any two elements.

# Return a list of pairs 
# in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the 
# minimum absolute difference of any two elements in arr
 

# Example 1:

# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1.
#  List all pairs with difference equal to 1 in ascending order.
# Example 2:

# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# Example 3:

# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]

# Most Optimal approach: 
# 1. Initialize a res empty list
# 2. Sort the array
# 3. Initialize mindiff = abs(arr[0] - arr[1])
# 4. Run a for loop from in range(len(arr) - 1)
# 5. If found an equal difference i.e abs(arr [i] - arr[i + 1]) == mindiff), 
# store it in res
# 6. If found a smaller difference, clear res, update mindiff, and store
# the new pair
# 7. Return res
from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        res = []
        arr.sort()
        mindiff = abs(arr[0] - arr[1])
        for i in range(len(arr) - 1):
            # If found an equal difference, store it in res
            if abs(arr[i] - arr[i + 1]) == mindiff:
                res.append([arr[i], arr[i + 1]])
            # If found a smaller difference, clear res, update mindiff, and store
            # the new pair
            elif abs(arr[i] - arr[i + 1]) < mindiff:
                res.clear()
                mindiff = abs(arr[i] - arr[i + 1])
                res.append([arr[i], arr[i + 1]])
        return res
s = Solution()
arr = [4,2,1,3]
print(s.minimumAbsDifference(arr))

arr = [1,3,6,10,15]
print(s.minimumAbsDifference(arr))

arr = [3,8,-10,23,19,-4,-14,27]
print(s.minimumAbsDifference(arr))


# Basic approach, fails on larger inputs
# mindiff  abs(arr[0] - arr[1]) 
# then run a for loop for i in range(len(arr))
# then run another for loop for j in range(i + 1, len(arr))
# then i have taken the minimum of the current min and abs(arr[i] - arr[j])
# Then sort the array, again traverse it 
# if abs(arr[i + 1] - arr[i]) == mindiff
# then append it to the ans list and return it
# But this approach fails on larger inputs
        # ans = []
        # mindiff = abs(arr[0] - arr[1])
        # for i in range(len(arr)):
        #     for j in range(i +  1, len(arr)):
        #         mindiff = min(mindiff, abs(arr[i] - arr[j]))
        # arr = sorted(arr)
        # for i in range(len(arr) - 1):
        #     if (abs(arr[i + 1] - arr[i]) == mindiff):
        #         ans.append([arr[i], arr[i + 1]])
        # return ans
# OPTIMAL 1:
# Optimal 1: approach is to sort the list, initialize res as empty list
# initialize mindiff as abs(arr[0] - arr[1])
# then run a for loop for i in range(len(arr) - 1)
# then take the minimum of mindiff and abs(arr[i] - arr[i + 1])
# and store to mindiff(sorting helped us here as in the sorted array
# as we only have to check consecutive elements)
# then run a for loop for i in range(len(arr) - 1)
# if abs(arr[i] - arr[i + 1]) == mindiff
# then append [arr[i], arr[i + 1]] to res and return it
# res = []
        # # Sort the array
        # arr.sort()
        # mindiff = abs(arr[0] - arr[1])
        # # Find the minimum absolute diff in the sorted array 
        # for i in range(len(arr) - 1):
        #     mindiff = min(mindiff, abs(arr[i] - arr[i + 1]))
        # print(mindiff)
        # # Store all the pairs whose difference is mindiff
        # for i in range(len(arr) - 1):
        #     if abs(arr[i] - arr[i + 1]) == mindiff:
        #         res.append([arr[i], arr[i + 1]])

        # return res