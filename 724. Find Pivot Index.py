# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 07:27:46 2020

@author: Caven
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        n = len(nums)
        
        left_sum = 0
        
        for i in range(n):
            if left_sum == (total - left_sum - nums[i]):
                return i
            else:
                left_sum += nums[i]
            
        return -1