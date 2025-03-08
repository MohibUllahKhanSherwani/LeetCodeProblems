# You are given an array prices where prices[i] 
# is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day 
# to buy one stock and choosing a different day 
# in the future to sell that stock.

# Return the maximum profit you can 
# achieve from this transaction. If you cannot achieve any
# profit, return 0.


#Basic approach: Run two for loops and for each i check j where 
# starts at i + 1 and check if prices[j] - prices[i] > 0 and also 
# greater than max profit if true, change max profit value 
# to current profit and return the max profit.
# problem with this approach is test cases dont pass when input is 
# very large

# Optimal approach is to use the two pointer approach, left = 0, right = 1
# Then traverse and search for each right, if prices[left] < prices[right] is true
# then calculate the current profit which is prices[right] - prices[left]
#  and update max_profit if it is greater than current profit
# else increment and bring left to right, left = right

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Basic approach:
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         curr_profit = prices[j] - prices[i]
        #         if (curr_profit > 0 and curr_profit > max_profit):
        #             max_profit = curr_profit
        # Optimal Sol 1:
        max_profit = 0
        left = 0
        right = 1
        for right in range(len(prices)):
            if (prices[left] < prices[right]):
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right   
        return max_profit
s = Solution()
prices = [7,1,5,3,6,4]
print('Profit: ', s.maxProfit(prices))
prices = [7,6,4,3,1]
print('Profit: ', s.maxProfit(prices))
