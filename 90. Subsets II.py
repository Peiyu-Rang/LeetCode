# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:48:08 2021

@author: Caven
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_count = collections.Counter(nums)
        num_count = [(key, num_count[key]) for key in num_count]
        
        res = []
        
        def backtrack(idx, comb, num_count):
            if len(comb) == k:
                res.append(comb[:])
                return
            
            for i in range(idx, len(num_count)):
                num, count = num_count[i]
                
                if count <= 0:
                    continue
                
                comb.append(num)
                num_count[i] = (num, count-1)
                backtrack(i, comb, num_count)
                comb.pop()
                num_count[i] = (num, count)
                
        
        for k in range(len(nums) + 1):
            backtrack(0, [], num_count)
            
        return res