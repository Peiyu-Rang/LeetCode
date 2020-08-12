# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:30:59 2020

@author: Caven
"""

import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in string.punctuation:
            paragraph = paragraph.replace(i, ' ')
        
        words = paragraph.split(' ')
        dic = {}
        maxCount = ('', 0)
        
        for w in words:
            if w.lower() in banned or w.lower() == '':
                continue
            if w.lower() in dic:
                dic[w.lower()] +=1
            else:
                dic[w.lower()] = 1
                
        
        for key in dic:
            if dic[key] > maxCount[1]:
                maxCount = (key, dic[key])
                
        return maxCount[0]