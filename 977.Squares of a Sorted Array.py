# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:52:37 2020

@author: Caven
"""

class Solution:
    def sortedSquared(self, A: List[int]) -> List[int]:
        n = len(A)
        i = 0
        j = n-1
        ans = []
        while i<=j:
            if A[i]**2 < A[j]**2:
                ans = [A[j]**2] + ans
                j -=1
            else:
                ans = [A[i]**2] + ans
                i +=1
        
        return ans