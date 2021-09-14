# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:47:02 2021

@author: Caven
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        idx2rm = set()
        for i,c in enumerate(s):
            if not stack:
                stack.append((i,c))
                continue
            if c == stack[-1][1]:
                idx2rm.add(stack.pop()[0])
                idx2rm.add(i)
            else:
                stack.append((i,c))
        
        res = []
        for i in range(len(s)):
            if i in idx2rm:
                continue
            res.append(s[i])
            
        return ''.join(res)
            