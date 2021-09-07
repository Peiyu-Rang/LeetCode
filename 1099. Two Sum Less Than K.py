# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:47:10 2021

@author: Caven
"""


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)        
        left = 0
        right = n-1
        res = -float('inf')
        
        while left < right:
            if nums[left] + nums[right] >=k:
                right -=1
            else:
                res = max(nums[left] + nums[right], res)
                left +=1
                
        return res if res > -float('inf') else -1
                