# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:28:59 2021

@author: Caven
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        max_len = 0
        while right < n:
            if nums[left] == 1:
                while right < n and nums[right] == 1:
                    right +=1
                if right - left > max_len:
                    max_len = right - left
                left = right
            else:
                left +=1
                right = left
                
        return max_len