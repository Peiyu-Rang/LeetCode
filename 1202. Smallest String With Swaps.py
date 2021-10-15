# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:21:44 2021

@author: Caven
"""


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n):
                self.p = list(range(n))
                
            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                
                return self.p[x]
                
            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)
                
        
        n = len(s)
        
        uf = UF(n)
        
        res = []
        mapping = collections.defaultdict(list)
        
        for x, y in pairs:
            uf.union(x, y)
            
        for i in range(n):
            mapping[uf.find(i)].append(s[i])
            
        for key in mapping:
            mapping[key].sort(reverse = True)
            
        for i in range(n):
            res.append(mapping[uf.find(i)].pop())
            
        return ''.join(res)
        