# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:08:15 2021

@author: Caven
"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        dic = {}
        for w in strings:
            first_letter_idx = letters.index(w[0])
            w_s = ''
            for ww in w:
                w_s += str((letters.index(ww) - first_letter_idx)%26)+ ' '
                
            if w_s in dic:
                dic[w_s].append(w)
            else:
                dic[w_s] = [w]
                
        res = []
        for key in dic:
            res.append(dic[key])
            
        return res