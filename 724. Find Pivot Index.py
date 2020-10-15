# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 07:27:46 2020

@author: Caven
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return -1
        sumLeft = 0
        sumRight = sum(nums[1:])
        if sumLeft == sumRight:
            return 0
        else:
            for i in range(1, n):
                sumLeft += nums[i-1]
                sumRight -= nums[i]
                if sumLeft == sumRight:
                    return i
            return -1