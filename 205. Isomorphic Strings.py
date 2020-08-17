# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:43:45 2020

@author: Caven
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for v1, v2 in zip(s,t):
            if v1 in dic:
                if dic[v1] == v2:
                    continue
                else:
                    return False
            else:
                dic[v1] = v2
                
        dic = {}
        for v1, v2 in zip(t,s):
            if v1 in dic:
                if dic[v1] == v2:
                    continue
                else:
                    return False
            else:
                dic[v1] = v2
            
        return True