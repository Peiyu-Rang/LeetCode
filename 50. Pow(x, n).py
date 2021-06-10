# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 07:03:15 2021

@author: Caven
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        if n == 0:
            return 1.0
        
        half = self.myPow(x, n // 2)
        if n %2 == 0:
            return half * half
        else:
            return half * half * x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
            
        res = 1.0
        multiplier = x
        
        i = n
        while i > 0:
            if i % 2 == 1:
                res *= multiplier
            
            multiplier *= multiplier
            
            i //= 2
        return res