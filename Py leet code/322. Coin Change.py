# You are given an integer array coins representing 
# coins of different denominations and an
# integer amount representing a total amount of money.

# Return the fewest number of coins that you
# need to make up that amount. If that amount of money 
# cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

# Optimal Solution:
# 1. Create an array of amount + 1 indices each filled with amount + 1 value
# 2. Example: coins = [1,2,5], amount = 11
# 3. dp = [12, 12 ,12 ,12 ,12, 12, 12 ,12 ,12 ,12 ,12 ,12]
# 4. idx= [0,   1, 2,   3, 4,  5,  6,  7,  8,  9,  10, 11]
# 5. Every index is basically the amount of coins needed to make that amount of money
# 6. Make the first index as 0 as we know to we need 0 coins to make 0 money
# 7. Run a for loop through range (1, amount + 1)
# 8. Run a for loop through the coins
# 9. Check if i - c >= 0 [i is 0, 12, 12, 12 ...] and c is [1, 2, 5]
# 10.Assign min of dp[i] and 1 + dp[i - c] to dp[i]
# 11. Return dp[amount] if it is not equal to amount + 1(what we assigned at the start)
# Else return 0
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) 
        dp[0] = 0
        print(dp)
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i],1 + dp[i - c])
        if dp[amount] != (amount + 1):
            return dp[amount]
        else:
            return - 1

s = Solution()
coins = [1,2,5]
amount = 11
print (s.coinChange(coins, amount))