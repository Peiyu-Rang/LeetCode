# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:21:28 2020

@author: Caven
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        j = n-1
        if n == 1:
            if digits[0] < 9:
                return [digits[0] + 1]
            else:
                return [1,0]
        digits[j] = digits[j] + 1
        while(j > 0):
            if digits[j] <= 9:
                carry = 0
                return digits
            else:
                carry = 1
                digits[j] = 0
                digits[j -1]  = digits[j -1] + carry
                j -=1
                
        if digits[0] > 9:
            digits[0] = 0
            return  [1]+ digits
        else:           
            return digits