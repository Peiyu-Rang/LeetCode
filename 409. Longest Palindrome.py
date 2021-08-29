# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:51:25 2021

@author: Caven
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        has_odd = False
        for key in counter:
            if counter[key] % 2 == 0:
                res += counter[key]
            else:
                res += counter[key] - 1
                has_odd = True                
                
        return res + 1 if has_odd else res
        