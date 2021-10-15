# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:47:33 2021

@author: Caven
"""


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordLocation = collections.defaultdict(list)
        
        for i,w in enumerate(wordsDict):
            self.wordLocation[w].append(i)
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1 = self.wordLocation[word1]
        loc2 = self.wordLocation[word2]
        res = float('inf')
        l1, l2 = 0,0
        
        while l1 < len(loc1) and l2 < len(loc2):
            res = min(res, abs(loc1[l1] - loc2[l2]))
            
            if loc1[l1] < loc2[l2]:
                l1 +=1
            else:
                l2 +=1
                
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)