# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:46:58 2021

@author: Caven
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decodeStr = []
        
        for item in s:
            k = ''
            if item != ']':
                stack.append(item)
            else:
                while stack[-1] != '[':
                    decodeStr.append(stack.pop())
                
                #pop out the [
                stack.pop()
                
                while stack and stack[-1].isnumeric():
                    k += stack.pop()
                
                k = int(k[::-1])
                
                decodeStr *= k
                
                while decodeStr:
                    stack.append(decodeStr.pop())
                
        return ''.join([s for s in stack])