# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:31:50 2021

@author: Caven
"""


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        
        gardenMap = collections.defaultdict(list)
        
        for u, v in paths:
            gardenMap[u].append(v)
            gardenMap[v].append(u)
            
        
        for i in range(n):
            if not res[i]:
                res[i] = 1
                stack = [i+1]
                
                while stack:
                    node = stack.pop()
                    for nei in gardenMap[node]:
                        neighborFlowers = [res[x-1] for x in gardenMap[nei] if res[x-1]]
                        for col in [1, 2, 3, 4]:
                            if col not in neighborFlowers:
                                res[nei-1] = col
        
        return res
                                           