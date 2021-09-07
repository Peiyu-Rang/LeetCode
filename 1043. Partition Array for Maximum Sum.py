# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:31:56 2021

@author: Caven
"""


# For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
               
        for i in range(n):
            best, curr_max = -float('inf'), -float('inf')
            for j in range(min(k, i+1)):
                curr_max = max(curr_max, arr[i-j])
                best = max(best, dp[i-j] + curr_max*(j+1))
                
            dp[i+1] = best
            
        return dp[-1]
    
    