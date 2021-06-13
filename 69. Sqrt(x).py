# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 17:09:03 2020

@author: Caven
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        mid = (left + right) // 2
        
        while left <= right:
            if mid * mid > x:
                right = mid -1
            elif mid * mid <= x and (mid + 1) * (mid + 1) > x:
                return mid
            else:
                left = mid +1
            
            mid = (left + right) // 2