# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:42:36 2021

@author: Caven
"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        even = 0
        p = 0
        while p < n:
            if A[p] % 2 != 1:
                A[even], A[p] = A[p], A[even]
                even += 1
            p +=1
            
        return A