# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:49:13 2021

@author: Caven
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_map = {'2':'abc',
                     '3':'def',
                     '4':'ghi',
                     '5':'jkl',
                     '6':'mno',
                     '7':'pqrs',
                     '8':'tuv',
                     '9':'wxyz'}
        
        
        res = []
        
        def backtrack(idx, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return
            
            possible_letters = digit_map[digits[idx]]
            
            for l in possible_letters:
                comb = comb + l
                backtrack(idx + 1, comb)
                comb = comb[:-1]
        
        backtrack(0, '')
        
        return res