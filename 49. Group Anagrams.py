# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:54:32 2021

@author: Caven
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for w in strs:
            w_s = ''.join(sorted(w))
            if w_s in dic:
                dic[w_s].append(w)
            else:
                dic[w_s] = [w]
        
        res = []
        for key in dic:
            res.append(dic[key])
            
        return res