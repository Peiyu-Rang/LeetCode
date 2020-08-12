# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:24:15 2020

@author: Caven
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        dic = {}
        for ss in s:
            if ss in dic:
                dic[ss] +=1
            else:
                dic[ss] = 1
        
        for key in dic:
            if dic[key] == 1:
                return s.index(key)
            
        return -1