# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:56:05 2020

@author: Caven
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        dicR = {}
        dicM = {}
        for l in ransomNote:
            if l in dicR:
                dicR[l] +=1
            else:
                dicR[l] = 1
        
        for l in magazine:
            if l in dicM:
                dicM[l] +=1
            else:
                dicM[l] = 1
        
        for key in dicR:
            if key in dicM:
                if dicR[key] <= dicM[key]:
                    continue
                else:
                    return False
            else:
                return False
            
        return True