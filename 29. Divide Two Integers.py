# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:16:10 2021

@author: Caven
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i *= 2
                temp *=2
        if not positive:
            res = -res
        return min(max(MIN_INT, res), MAX_INT)