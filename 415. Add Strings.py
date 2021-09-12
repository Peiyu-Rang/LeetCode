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
    

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        p1 = len(num1)-1
        p2 = len(num2)-1
        carry = 0
        
        while p1 >=0 or p2 >=0:
            x1 = ord(num1[p1]) - ord('0') if p1 >=0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >=0 else 0
            total = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(total)
            p1 -=1
            p2 -=1
            
        if carry:
            res.append(carry)
            
        return ''.join([str(x) for x in res[::-1]])