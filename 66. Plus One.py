# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:21:28 2020

@author: Caven
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] +=1
                return digits
            
        return [1] + digits