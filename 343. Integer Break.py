# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:38:04 2021

@author: Caven
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        if n == 3:
            return 2
        res = -float('inf')
        for y in range(int(n // 3) + 1):
            if (n - 3*y) % 2 == 0:
                x = (n - 3*y) // 2
                res = max(res, 2**x * 3**y)
                
        return res