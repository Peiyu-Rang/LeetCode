# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:16:57 2021

@author: Caven
"""


class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        # if an element has anything on right that is smaller, or anything on left is larger, it would be invalid
        n = len(nums)
        
        small_from_right = [float('inf')] * n
        
        large_from_left = [-float('inf')] * n
        
        for i in range(1, n):
            large_from_left[i] = max(large_from_left[i-1], nums[i-1])
        
        for i in range(n-2, -1, -1):
            small_from_right[i] = min(small_from_right[i+1], nums[i+1])
        
        res = 0
        for i in range(n):
            if large_from_left[i] < nums[i] < small_from_right[i]:
                res += 1
        
        return res