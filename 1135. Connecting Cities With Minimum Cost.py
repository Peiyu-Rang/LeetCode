# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:34:56 2021

@author: Caven
"""


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections_s = sorted(connections, key = lambda x: x[2])
        root = [i for i in range(n)]
        
        def find(x):
            while x != root[x]:
                x = root[x]
                
            return x
    
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                root[rootY] = rootX
                    
        def connected(x, y):
            return find(x) == find(y)
        
        def allConnected():
            cRoot = find(0)
            for r in range(1, n):
                if cRoot!= find(r):
                    return False
            return True

        res = 0
        edge_added = 0
        for i in range(len(connections_s)):
            a,b,c = connections_s[i]
            if connected(a-1, b-1):
                continue
            res += c
            union(a-1, b-1)
            edge_added +=1
            if edge_added == n-1:
                break
            
        if allConnected():
            return res

        return -1
