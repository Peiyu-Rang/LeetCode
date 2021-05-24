# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:41:08 2021

@author: Caven
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*","/"]
        
        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                
                if s == '+':
                    c = a + b
                elif s == '-':
                    c = a - b
                elif s == '*':
                    c = a * b
                else:
                    c = int(a / b)
                
                stack.append(c)
                
        return stack.pop()