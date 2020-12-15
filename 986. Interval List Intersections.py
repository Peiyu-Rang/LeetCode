# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:42:10 2020

@author: Caven
"""


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        
        i = 0
        j = 0
        
        m = len(A)
        n = len(B)
        
        while i < m and j < n:
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            
            if low <= high:
                ans.append([low, high])
            
            if A[i][1] < B[j][1]:
                i +=1
            else:
                j +=1
                
        
        return ans