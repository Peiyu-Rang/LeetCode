# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 22:35:12 2021

@author: Caven
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        
        n = len(nums)
        def backtrack(first = 0, comb = []):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(first, n):
                comb.append(nums[i])
                backtrack(i +1, comb)
                
                comb.pop()
                
        for k in range(n + 1):
            backtrack()
            
        return res