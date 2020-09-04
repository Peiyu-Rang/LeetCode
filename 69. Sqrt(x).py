# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:09:03 2020

@author: Caven
"""

class Solution:
    def mySqrt(self, x:int) -> int:
        if x <2:
            return x
        left = 2
        right = x//2 
        while left <= right:
            mid = left + (right - left)//2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right