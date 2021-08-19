# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:57:42 2021

@author: Caven
"""


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        i = 0
        j = 0
        n = len(s)
        label = [0 for i in range(n)]
        
        end = 0
        
        for i in range(n):
            for word in words:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            
            label[i] = i < end
            
                
        res = ''
        for i in range(n):
            if label[i] == 1 and (i == 0 or label[i-1] == 0):
                res += '<b>'
            
            res += s[i]
            
            if label[i] == 1 and (i == n-1 or label[i + 1] == 0):
                res += '</b>'
                
        return res
                