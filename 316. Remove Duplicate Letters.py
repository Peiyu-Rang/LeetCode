# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:47:11 2021

@author: Caven
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        
        last_occurrence = {c:i for i, c in enumerate(s)}
        
        for i,c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                    
                seen.add(c)
                stack.append(c)
        
        return ''.join(stack)