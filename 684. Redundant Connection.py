# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:51:39 2021

@author: Caven
"""


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(1000)]
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            
            return root[x]
        
        def union(x, y):
            xr = find(x)
            yr = find(y)
            root[xr] = yr
            
        for u, v in edges:
            if find(u-1) == find(v-1):
                return [u, v]
            else:
                union(u-1, v-1)
                
        