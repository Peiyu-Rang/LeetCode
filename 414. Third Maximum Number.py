# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:17:01 2021

@author: Caven
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = -float('inf')
        second= -float('inf')
        third = -float('inf')
        
        for n in nums:
            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                if n == first:
                    continue
                third = second
                second = n
            elif n > third:
                if n == second:
                    continue
                third = n
            
        return third if third > -float('inf') else first