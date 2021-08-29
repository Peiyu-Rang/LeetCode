# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:01:24 2021

@author: Caven
"""

"""
dp(i,j) = the longest length of Palindromic Subsequence of s[i:j+1]

dp(i,i) = 1
dp(i,j) = dp(i+1, j-1) + 2 if s[i] == s[j]
dp(i,j) = max(dp(i+1, j), dp(i, j-1))

iteration sequence should be (i, i + d), for 
"""
  


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for j in range(n)]
        
        for d in range(n):
            dp[d][d] = 1
            
        for d in range(1, n):
            for i in range(0, n-d):
                if s[i] == s[i + d]:
                    dp[i][i+d] = dp[i+ 1][i +d - 1] + 2
                else:
                    dp[i][i + d] = max(dp[i][i + d-1], dp[i+1][i + d])
                    
        return dp[0][n-1]