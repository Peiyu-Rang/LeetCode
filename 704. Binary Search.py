# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:12:39 2021

@author: Caven
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        left = 0
        right = n-1
        
        mid = (left + right) // 2
        
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
            
            mid = (left + right) //2
            
        return -1