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
        i = 0
        count = 0
        while(count < n):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
                
            count+=1