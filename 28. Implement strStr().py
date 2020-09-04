# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:21:12 2020

@author: Caven
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if m == n:
            if haystack == needle:
                return 0
            else:
                return -1
        
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
            
        return -1