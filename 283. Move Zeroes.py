# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:14:28 2020

@author: Caven
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non0 = 0
        p = 0
        while (p < n):
            if nums[p] != 0:
                nums[p], nums[non0] = nums[non0], nums[p]
                non0 +=1
            
            p +=1