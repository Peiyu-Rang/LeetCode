# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:08:32 2021

@author: Caven
"""


class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        p = {}
        for a in similarPairs:
            p[a[0]] = a[0]
            p[a[1]] = a[1]
            
        def find(x):
            if x not in p:
                p[x] = x
            if x != p[x]:
                p[x] = find(p[x])
                
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
            
        for a, b in similarPairs:
            union(a,b)
        
        if len(sentence1) != len(sentence2):
            return False
        
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or find(w1) == find(w2):
                continue
            else:
                return False
        
        return True