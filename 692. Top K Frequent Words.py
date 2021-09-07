# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:15:35 2021

@author: Caven
"""


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        
        counter_sorted = sorted(counter.items(), key = lambda x: (-x[1], x[0]))
        
        res= []
        for i in range(k):
            res.append(counter_sorted[i][0])
            
        return res