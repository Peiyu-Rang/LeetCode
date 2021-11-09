# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:48:35 2021

@author: Caven
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid-1] < target and nums[mid] >= target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
                
        return n if mid == right else 0
                