# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:24:15 2020

@author: Caven
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for i,v in enumerate(s):
            if counter[v] == 1:
                return i
        return -1