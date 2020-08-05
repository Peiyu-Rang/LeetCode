# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:46:16 2020

@author: Caven
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        
        for i in range(1,n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(nums[i], maxSum)
            
        return maxSum