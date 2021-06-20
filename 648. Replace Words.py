# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:08:11 2021

@author: Caven
"""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dic_set = set(dictionary)
        
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in dic_set:
                    return word[:i]
            return word
            
        return " ".join(map(replace, sentence.split()))