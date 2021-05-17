# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:44:29 2020

@author: Caven
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            sq_sum = 0
            while n > 0:
                sq_sum += (n % 10) ** 2
                n = n // 10

            if sq_sum == 1:
                return True
            if sq_sum not in seen:
                seen.add(sq_sum)
            else:
                return False
            
            n = sq_sum