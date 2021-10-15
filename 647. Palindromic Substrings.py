# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:01:33 2021

@author: Caven
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            res += self.countPalindromesAroundCenter(s, i, i)
            res += self.countPalindromesAroundCenter(s, i, i+1)
            
        return res
    
    def countPalindromesAroundCenter(self, s, i, j):
        res = 0
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            res +=1
            i -=1
            j +=1
        
        return res