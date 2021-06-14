# -*- coding: utf-8 -*-
"""
Created on Mon May  3 22:37:33 2021

@author: Caven
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        res = [-1, -1]
        
        # find lower bound
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid -1 < 0 or nums[mid -1] < target:
                    res[0] = mid
                    break
                else:
                    right = mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid - 1
            
        
        # find upper bound
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid + 1 >= n or nums[mid + 1] > target:
                    res[1] = mid
                    break
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return res