# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:02:05 2020

@author: Caven
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <3:
            return []
        if n == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums = sorted(nums)
        ans = []
        base = 0
        while base <= n-2:
            left = base +1
            right = n-1
            while (left < right):
                if nums[base] + nums[left] + nums[right] < 0:
                    left +=1
                elif nums[base] + nums[left] + nums[right] > 0:
                    right -=1
                else:
                    ans.append([nums[base], nums[left], nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left -1]:
                        left +=1
                     
            
            base +=1
            while (base <= (n-2))  and (nums[base -1] == nums[base]):
                base +=1
            