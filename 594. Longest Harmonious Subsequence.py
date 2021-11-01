# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 06:35:50 2021

@author: Caven
"""


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        
        for key in counter:
            if key + 1 in counter:
                res = max(res, counter[key] + counter[key+1])
                
        return res