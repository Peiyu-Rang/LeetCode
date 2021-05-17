# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:20:01 2020

@author: Caven
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        n1 = len(a)
        n2 = len(b)
        
        i = n1-1
        j = n2-1
        
        carry = 0
        
        while i >=0  or j >= 0:
            if i < 0:
                x = 0
                y = int(b[j])
                j -=1
                
            elif j < 0:
                x = int(a[i])
                y = 0
                i-=1
            else:
                x= int(a[i])
                y= int(b[j])
                j-=1
                i-=1
                
            total = (carry + x + y) % 2
            carry = (carry + x + y) // 2
            res = str(total) + res
            
        if carry > 0:
            res = str(carry) + res
        
        return res
                