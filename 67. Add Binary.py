# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:20:01 2020

@author: Caven
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na = len(a)
        nb = len(b)
        ans = ''
        if na > nb:
            a, b = b, a
            na = len(a)
            nb = len(b)
        carry = 0
        i = -1
        while (-i <= nb):
            if (-i <= na):
                dig = int(a[i]) + int(b[i]) + carry
                if dig >=2:
                    dig %= 2
                    carry = 1
                else:
                    carry = 0
                
                ans = str(dig) + ans
            else:
                dig = int(b[i]) + carry
                if dig >=2:
                    dig %= 2
                    carry = 1
                else:
                    carry = 0
                
                ans = str(dig) + ans
            i -=1
        
        if carry ==1:
            ans = '1' + ans
        
        return ans