# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:01:28 2021

@author: Caven
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def backtrack(idx, comb):
            if len(comb) == len(s):
                res.append(comb[:])
                return
            
            for i in range(idx, len(s)):
                l = s[i]
                if l.isdigit():
                    comb +=l
                    backtrack(i+1, comb)
                    comb = comb[:-1]
                else:
                    comb += l.lower()
                    backtrack(i+1, comb)
                    comb = comb[:-1]
                    
                    comb +=l.upper()
                    backtrack(i+1, comb)
                    comb = comb[:-1]
        
        backtrack(0, '')
        return res