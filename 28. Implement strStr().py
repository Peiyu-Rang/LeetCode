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
        
        i = 0
        while i < n-m + 1:
            if haystack[i:i+m] == needle:
                return i
            i +=1
            
        return -1
        
        