# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:17:26 2021

@author: Caven
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] >= nums[left]:
                if nums[left] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[left] > nums[right]:
                    right = mid
                else:
                    left = mid + 1
                
        return nums[left]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: #nums[mid] <= nums[right]
                right = mid
        
        return nums[left]