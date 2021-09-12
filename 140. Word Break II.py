# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 21:22:44 2021

@author: Caven
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordSet = set(wordDict)
        
        
        
        def backtrack(s, wordSet, comb):
            if s == '':
                res.append(comb[:])
                return
            for i in range(len(s)):
                if s[:i+1] in wordSet:
                    comb.append(s[:i+1])
                    backtrack(s[i+1:], wordSet, comb)
                    comb.pop()
            
            return
        
        backtrack(s, wordSet, [])
        
        return [' '.join(x) for x in res]
