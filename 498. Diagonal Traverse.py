# -*- coding: utf-8 -*-
"""
Created on Fri May 14 16:59:41 2021

@author: Caven
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        
        for i in range(m+n-1):
            if i % 2 == 0: #even
                for j in range(min(i,m-1), max(-1, i-n), -1):
                        res.append(mat[j][i-j])
            else: # odd
                for j in range(max(0, i-n+1), min(m,i+1)):
                        res.append(mat[j][i-j])
                    
                
        return res