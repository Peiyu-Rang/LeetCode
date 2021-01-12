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
        left = 0
        n = len(s)
        right = n-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1