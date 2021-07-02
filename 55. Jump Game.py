# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 22:42:52 2021

@author: Caven
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        right = n-1
        if n == 1:
            return True
        left = n-2
        
        while left >= 0:
            if nums[left] >= right - left:
                right = left
        
            left -=1
            
        return right == 0