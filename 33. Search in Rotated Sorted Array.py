# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:48:49 2021

@author: Caven
"""


class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        mid = (left + right) // 2
        
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            mid = (left + right) // 2
                    
        return -1
        