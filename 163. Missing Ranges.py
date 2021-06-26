# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:05:13 2021

@author: Caven
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def generateRange(left, right):
            if left == right:
                return str(left)
            else:
                return str(left) + '->' + str(right)
        
        res = []
        if len(nums) == 0:
            res.append(generateRange(lower, upper))
            return res
        
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == lower:
                    continue
                elif nums[i] == lower + 1:
                    res.append(generateRange(lower, lower))
                elif nums[i] > lower + 1:
                    res.append(generateRange(lower, nums[i]-1))
            elif i < len(nums):
                if nums[i] == nums[i-1] + 1:
                    continue
                elif nums[i] >= nums[i-1] + 2:
                    res.append(generateRange(nums[i-1] + 1, nums[i] -1))
            
        if nums[-1] == upper -1:
            res.append(generateRange(upper, upper))
        elif nums[-1] < upper - 1:
            res.append(generateRange(nums[-1] + 1, upper))
                
        return res