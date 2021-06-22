# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 17:17:03 2021

@author: Caven
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < -2147483648 or x > 2147483647:
            return 0
        res = int(str(x)[::-1]) if x > 0 else int('-' + str(-x)[::-1])
        
        if res < -2147483648 or res > 2147483647:
            return 0
        return res