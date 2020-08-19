# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 07:42:28 2020

@author: Caven
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minNum = min(nums)
        ans = 0
        for n in nums:
            ans += n - minNum
            
        return ans