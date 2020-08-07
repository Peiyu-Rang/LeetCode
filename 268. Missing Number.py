# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:23:03 2020

@author: Caven
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n)*(n+1)/2 -sum(nums))