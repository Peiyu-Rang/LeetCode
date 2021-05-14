# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:28:08 2021

@author: Caven
"""


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        n = len(nums)
        if n == 1:
            return 0
        
        max1 = nums[0]
        max2 = None
        
        for i in nums[1::]:
            if i > max1:
                max2 = max1
                max1 = i
                
            elif i <= max1 and not max2:
                max2 = i
            elif i <= max1 and i > max2:
                max2 = i
            else:
                continue
                
        return nums.index(max1) if max1 >= 2* max2 else -1