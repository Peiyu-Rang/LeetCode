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
        i = 0
        j = n-1
        while(i<j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            
            i+=1
            j-=1
            
        return s
        