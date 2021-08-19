# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 11:55:42 2021

@author: Caven
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s= s.replace(' ','')
        
        n = len(s)
        curr = ''
        op = '+'
        for i in range(n):

            if s[i] not in ('+', '-', '*', '/'):
                curr += s[i]
            elif op == '+':
                stack.append(int(curr))
                op = s[i]
                curr = ''
            elif op == '-':
                stack.append(-int(curr))
                op = s[i]
                curr = ''
            elif op == '*':
                stack.append(stack.pop() * int(curr))
                op = s[i]
                curr = ''
            elif op == '/':
                stack.append(int(stack.pop() / int(curr)))
                op = s[i]
                curr = ''
        
        if op == '+':
            stack.append(int(curr))
        elif op == '-':
            stack.append(-int(curr))
        elif op == '*':
            stack.append(stack.pop() * int(curr))
        elif op == '/':
            stack.append(int(stack.pop() / int(curr)))
        
        res = 0
        while stack:
            res += stack.pop()
            
        return res