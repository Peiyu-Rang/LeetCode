# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:12:39 2021

@author: Caven
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        left = 0
        right = n-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1