# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:06:35 2021

@author: Caven
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        
        while left <=right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid -1
                
        return False