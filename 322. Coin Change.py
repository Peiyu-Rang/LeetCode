# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:54:40 2021

@author: Caven
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x-c] + 1)
                
        return dp[amount] if dp[amount] != float('inf') else -1