# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:58:40 2021

@author: Caven
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def help(i = 0, sums = 0):
            if (i, sums) in memo:
                return memo[(i, sums)]
            if i >= len(nums):
                if sums == target:
                    res = 1
                else:
                    res = 0
                memo[(i, sums)] = res
                return res
            add = help(i + 1, sums + nums[i])
            sub = help(i + 1, sums - nums[i])
            
            memo[(i, sums)] = add + sub
            
            return memo[(i, sums)]
        
        return help()
