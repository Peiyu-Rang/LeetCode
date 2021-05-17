# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:21:12 2020

@author: Caven
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        i = 0
        while i + m <= n:
            if haystack[i:i+m] == needle:
                return i
            
            else:
                i +=1
                
        return -1
        