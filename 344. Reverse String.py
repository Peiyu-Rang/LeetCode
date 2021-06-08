# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:34:30 2020

@author: Caven
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        
        l = 0
        r = n-1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l +=1
            r -=1
            
            
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right -1)
                
        return helper(0, len(s)-1)