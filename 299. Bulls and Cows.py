# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:56:14 2021

@author: Caven
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        counter = collections.Counter(secret)
        bull = 0
        cow = 0
        bull_idx = set()
        
        for i,c in enumerate(guess):
            if guess[i] == secret[i]:
                counter[guess[i]] -=1
                bull +=1
                bull_idx.add(i)
                
        for i, c in enumerate(guess):
            if guess[i] in counter:
                if counter[guess[i]] > 0 and i not in bull_idx:
                    cow +=1
                    counter[guess[i]] -=1
        
        return str(bull)+'A' + str(cow) + 'B'
        