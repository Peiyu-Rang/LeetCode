# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:27:36 2021

@author: Caven
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
            
        return True
        