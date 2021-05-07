# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:03:13 2021

@author: Caven
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        before = 0
        after = 0
        maxi = 0
        seen0 = False
        n = len(nums)
        if n == 1:
            return 1
        i = 0
        while i < n:
            if nums[i] != 0:
                after +=1
            else:
                seen0 = True
                maxi = max(before + after + 1, maxi)
                before = after
                after = 0
            
            i +=1
        
        if seen0:
            return max(before + after + 1, maxi)
        else:
            return after