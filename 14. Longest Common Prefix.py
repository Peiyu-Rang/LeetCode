# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:08:35 2018

@author: rpy
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        i = 0
        n = min([len(x) for x in strs])
        
        while i < n:
            if len(set([x[i] for x in strs])) == 1:
                res += strs[0][i]
                i +=1
            else:
                break
                
        return res
        