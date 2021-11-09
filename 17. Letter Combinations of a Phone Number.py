# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:49:13 2021

@author: Caven
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
        
        res = []
        n = len(digits)
        if n == 0:
            return []
        
        def backtrack(idx, comb):
            if len(comb) == n:
                res.append(comb[:])
                return
            
            possible_letters = dic[digits[idx]]
            for l in possible_letters:
                comb = comb + l
                backtrack(idx + 1, comb)
                comb = comb[:-1]
                
        backtrack(0,'')
            
        return res