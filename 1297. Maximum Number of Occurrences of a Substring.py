# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:26:48 2021

@author: Caven
"""


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if not s:
            return 0
        
        all_substrings = collections.defaultdict(int)
        for i in range(minSize, len(s) + 1):
            w = s[i-minSize : i]
            
            if len(set(w)) <= maxLetters:
                all_substrings[w] +=1
                
        
        if all_substrings:
            return max(all_substrings.values())
        else:
            return 0
            