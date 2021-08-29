# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 13:21:28 2021

@author: Caven
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]
        
        for col in range(1, len(text2)+ 1):
            for row in range(1, len(text1)+ 1):
                if text1[row-1] == text2[col-1]:
                    dp[row][col] =  dp[row-1][col-1] + 1
                    
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                    
        return dp[len(text1)][len(text2)]