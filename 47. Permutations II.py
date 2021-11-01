# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 22:32:56 2021

@author: Caven
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def backtrack(first):
            if first == n-1:
                res.append(nums[:])
                return
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
            
        backtrack(0)
        
        return list(set([tuple(x) for x in res]))
                