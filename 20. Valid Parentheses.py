# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:44:06 2020

@author: Caven
"""

class Solution:
    def isValid(self, s: str) -> bool:
        open_p = {'(':')', '[':']', '{':'}'}
        stack = []
        for ss in s:
            if ss in open_p:
                stack.append(ss)
            elif len(stack) > 0:
                if ss == open_p[stack.pop()]:
                    continue
                else:
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False
        