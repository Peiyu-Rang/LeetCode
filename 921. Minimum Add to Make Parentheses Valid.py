# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 17:10:11 2021

@author: Caven
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        res = 0
        
        for c in s:
            if c not in ('(',')'):
                continue
            elif c == '(':
                balance +=1
            else:
                balance -=1
            
            if balance == -1:
                res +=1
                balance +=1
                
        return res + balance