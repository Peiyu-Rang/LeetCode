# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:22:55 2020

@author: Caven
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        if len(s) != len(t):
            return False
        for ss in s:
            if ss in dicS:
                dicS[ss] +=1
            else:
                dicS[ss] = 1
                
        for ss in t:
            if ss in dicT:
                dicT[ss] +=1
            else:
                dicT[ss] = 1
                
        for key in dicS:
            if key not in dicT:
                return False
            elif dicS[key] != dicT[key]:
                return False
        
        return True