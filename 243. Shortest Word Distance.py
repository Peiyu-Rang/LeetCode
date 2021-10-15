# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:01:05 2021

@author: Caven
"""


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        loc1 = -1
        loc2 = -1
        res = float('inf')
        
        for i, w in enumerate(wordsDict):
            if w == word1:
                loc1 = i
            elif w == word2:
                loc2 = i
                
            if loc1 != -1 and loc2 != -1:
                res = min(res, abs(loc1 - loc2))
                
        return res