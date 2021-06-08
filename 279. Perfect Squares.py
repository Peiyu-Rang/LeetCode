# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:54:48 2021

@author: Caven
"""


class Solution:
    def numSquares(self, n: int) -> int:
        sq_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
        
        dp = [float('inf')] * (n+1)
        
        dp[0] = 0
        
        for i in range(1, n+1):
            for sq in sq_nums:
                if i < sq:
                    break
                dp[i] = min(dp[i], dp[i-sq] + 1)
                
        return dp[-1]
        i