# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:38:45 2020

@author: Caven
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIdx = {c:i for i, c in enumerate(order)}
        
        n = len(words)
        
        newWords = []
        for word in words:
            newWord = []
            for l in word:
                newWord.append(orderIdx[l])
            newWords.append(newWord)
        
        for w1, w2 in zip(newWords, newWords[1:]):
            if w1 > w2:
                return False
        return True