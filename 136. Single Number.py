# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:45:06 2020

@author: Caven
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)