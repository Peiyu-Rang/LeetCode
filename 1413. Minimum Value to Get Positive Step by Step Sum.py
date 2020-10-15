# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 07:38:07 2020

@author: Caven
"""


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minVal = nums[0]
        currVal = nums[0]
        n = len(nums)
        for i in range(1,n):
            currVal += nums[i]
            if currVal < minVal:
                minVal = currVal
            
        return max(1 - minVal,1)