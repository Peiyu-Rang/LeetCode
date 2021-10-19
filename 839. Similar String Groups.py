# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:21:21 2021

@author: Caven
"""


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        p = {x:x for x in strs}
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
        
        similar = lambda x, y: sum(a != b for a, b in zip(x, y)) <= 2
        for i in range(len(strs)):
            for j in range(i):
                if similar(strs[i], strs[j]):
                    union(strs[i], strs[j])
                    
        return len({find(x) for x in strs})