# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:15:48 2021

@author: Caven
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * (n+1) for i in range(m+1)]
        
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n + 1):
                if (matrix[i-1][j-1] == '1'):
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    max_len = max(max_len, dp[i][j])
                    
        return max_len * max_len
        