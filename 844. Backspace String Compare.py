# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:38:46 2020

@author: Caven
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip +=1
                elif skip:
                    skip -=1
                else:
                    yield x
        
        return all([x == y for x,y in itertools.zip_longest(F(S), F(T))])