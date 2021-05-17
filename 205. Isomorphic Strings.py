# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:43:45 2020

@author: Caven
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        for ss, tt in zip(s,t):
            if ss in seen:
                if seen[ss] == tt:
                    continue
                else:
                    return False
            else:
                seen[ss] = tt
                
        seen = {}
        for ss, tt in zip(t,s):
            if ss in seen:
                if seen[ss] == tt:
                    continue
                else:
                    return False
            else:
                seen[ss] = tt
        
        
        return True