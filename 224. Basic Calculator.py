# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:40:29 2021

@author: Caven
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        
        sign = 1
        stack = []
        curr = 0
        res = 0
        
        for l in s:
            if l not in ('+', '-', '(', ')'):
                curr = curr * 10 + int(l)
            
            elif l == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif l == '+':
                res += sign * curr
                sign = 1
                curr = 0
            elif l == '-':
                res += sign * curr
                sign = -1
                curr = 0
                
            elif l == ')':
                res += sign * curr
                res *= stack.pop()
                res += stack.pop()
                
                curr = 0
        
        return res + sign * curr
                
                
        
        