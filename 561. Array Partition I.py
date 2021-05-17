# -*- coding: utf-8 -*-
"""
Created on Sun May 16 16:20:43 2021

@author: Caven
"""


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums) // 2
        for i in range(n):
            res += nums[i * 2]
            
        return res
        