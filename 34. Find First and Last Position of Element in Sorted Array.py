# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:37:33 2021

@author: Caven
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) -1
        res = [-1, -1]
        if right < 0:
            return res
        while left <= right:
            mid  = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] < target):
                res[0] = mid
                res[1] = mid
                break
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] == target and nums[mid-1] == target:
                right = mid -1
                
        
        left = mid + 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid + 1] > target):
                res[1] = mid
                break
            if nums[mid] > target:
                right = mid -1
            if nums[mid] == target:
                left = mid + 1
                
        return res