# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:22:34 2021

@author: Caven
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        hasSign = False
        hasDecimal = False
        hasE = False
        hasNum = False
        
        numbers = [str(i) for i in range(10)]
        
        for i,v in enumerate(s):
            if v.isdigit():
                hasNum = True
            elif v in ('+', '-'):
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
                hasSign = True
            elif v in ('e', 'E'):
                if hasE or not hasNum:
                    return False
                hasE = True
                hasNum = False
            elif v == '.':
                if hasDecimal or hasE:
                    return False
                hasDecimal = True
            else:
                return False
            
        return hasNum
        
    
class Solution(object):
    def isNumber(self, s):
        # This is the DFA we have designed above
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},
            {"digit": 1, "dot": 4, "exponent": 5},
            {"digit": 1, "dot": 3},
            {"digit": 4},
            {"digit": 4, "exponent": 5},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7}
        ]
        
        current_state = 0
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]:
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[current_state]:
                return False
            
            current_state = dfa[current_state][group]
        
        return current_state in [1, 4, 7]