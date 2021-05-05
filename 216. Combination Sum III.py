# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:26:42 2021

@author: Caven
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                res.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain - i - 1, comb, i + 1)
                comb.pop()
                
        backtrack(n, [], 0)
        return res