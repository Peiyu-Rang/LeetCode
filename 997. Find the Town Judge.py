# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:52:54 2021

@author: Caven
"""


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n-1:
            return -1
        
        
        trust_score = [0] * (n + 1)
        
        for a, b in trust:
            trust_score[a] -=1
            trust_score[b] +=1
            
        for i, v in enumerate(trust_score):
            if v == n-1 and i > 0:
                return i
        
        return -1