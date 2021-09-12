# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:40:28 2021

@author: Caven
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        res = [1] * n
        for i in range(n):
            res[i] = left[i]*right[i]
            
        return res