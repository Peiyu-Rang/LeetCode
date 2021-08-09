# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 16:29:00 2021

@author: Caven
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx2remove = set()
        stack = []
        
        for i,v in enumerate(s):
            if v not in "()":
                continue
            if v == '(':
                stack.append(i)
                
            elif not stack:
                idx2remove.add(i)
            else:
                stack.pop()
                
        idx2remove = idx2remove.union(set(stack))
        
        res = []
        for i in range(len(s)):
            if i not in idx2remove:
                res.append(s[i])
        
        return ''.join(res)