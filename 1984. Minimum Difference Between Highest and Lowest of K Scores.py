# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:30:04 2021

@author: Caven
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums = sorted(nums)
        n = len(nums)
        
        left = 0
        right = k-1
        
        res = float('inf')
        
        while right < n:
            res = min(res, nums[right] - nums[left])
            
            left += 1
            right +=1
            
        return res