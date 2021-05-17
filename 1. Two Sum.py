# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:32:10 2020

@author: Caven
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,v in enumerate(nums):
            if target - v in seen:
                return [i, seen[target - v]]
            else:
                seen[v] = i