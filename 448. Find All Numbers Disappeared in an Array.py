# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:51:28 2020

@author: Caven
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            newIdx = abs(nums[i]) -1
            nums[newIdx] = abs(nums[newIdx]) * -1
            
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i)
        
        return ans