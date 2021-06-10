# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 22:52:26 2021

@author: Caven
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i + 1, curr)

                curr.pop()
        
        
        res = []
        backtrack()
        return res