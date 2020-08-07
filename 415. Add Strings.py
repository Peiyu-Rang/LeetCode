# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:22:50 2020

@author: Caven
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        n1 = len(num1)
        n2 = len(num2)
        nMax = max(n1,n2)
        carry = 0
        
        for i in range(nMax):
            idx1 = n1 -1 -i
            if idx1 <0:
                v1 = 0
            else:
                v1 = ord(num1[n1 -1 -i])-ord('0')
            idx2 = n2 - 1 - i
            if idx2 < 0:
                v2 = 0
            else:
                v2 = ord(num2[n2 -1 -i])-ord('0')
                
            
            digSum = (v1+v2+carry)%10
            
            if v1+v2+carry >= 10:
                carry = 1
            else:
                carry = 0
            
            res = str(digSum) + res
        
        if carry > 0:
            res = str(carry) + res
        
        return res