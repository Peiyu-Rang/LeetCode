# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:38:51 2021

@author: Caven
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        
        return False