# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:17:01 2021

@author: Caven
"""


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = -inf
        max2 = -inf
        max3 = -inf
        for i in nums:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
                
            elif i == max1:
                continue
            elif i > max2:
                max3 = max2
                max2 = i
            elif i == max2:
                continue
            elif i > max3:
                max3 = i
            elif i == max3:
                continue
                
        return max3 if max3 > -inf else max1
        