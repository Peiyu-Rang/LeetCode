# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:48:36 2020

@author: Caven
"""

# DP 
# 	Time Limit Exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[False] * n for i in range(n)]
        
        for d in range(n):
            dp[d][d] = True
            if 0 <= d < n and 0 <= d+1 < n:
                dp[d][d+1] = s[d] == s[d+1]
            
        for d in range(2, n):
            for i in range(n):
                if 0 <= i+d <= n and 0 <= i+1 <= n and 0 <= i+d-1 <= n and 0 <= i+d < n:
                    dp[i][i+d] = dp[i+1][i+d-1] and (s[i] == s[i+d])
        
        
        for diff in range(n-1, -1, -1):
            for i in range(n):
                if 0 <= i < n and 0 <= i+diff < n:
                    if dp[i][i + diff]:
                        return s[i:i + diff+1]
                    
            
    
    
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        left = 0
        right = 0
        n = len(s)
        def expandAroundCenter(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -=1
                j +=1
            return j - i -1
        for i in range(n):
            len1 = expandAroundCenter(i, i)
            len2 = expandAroundCenter(i, i+1)
            len3 = max(len1, len2)
            
            if len3 > right - left:
                left = i - (len3-1)//2
                right = i + len3 // 2
                
            
        return s[left:right+1]