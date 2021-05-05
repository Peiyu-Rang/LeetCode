# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:41:43 2021

@author: Caven
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(remain, comb, new_start):
            if remain == 0:
                res.append(sorted(list(comb)))
                return
            elif remain < 0:
                return
            
            for i in range(new_start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)
                comb.pop()
                
        backtrack(target, [], 0)
        
                
        return res
        