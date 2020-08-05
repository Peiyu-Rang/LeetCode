# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:44:06 2020

@author: Caven
"""

class Solution:
    def isValid(self, s: str) -> bool:
        cum = []
        for ss in s:
            if ss in '([{':
                cum.append(ss)
            else:
                if len(cum) == 0:
                    return False
                if ss == ')' and cum[-1] == '(':
                    cum.pop()
                    continue
                elif ss == ']' and cum[-1] == '[':
                    cum.pop()
                    continue
                elif ss == '}' and cum[-1] == '{':
                    cum.pop()
                    continue
                else:
                    return False
                
        return len(cum) == 0