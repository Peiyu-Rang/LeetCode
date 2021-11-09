# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:24:11 2021

@author: Caven
"""


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        uf = UnionFind(n)
                
        

        for u, v in connections:
            uf.union(u,v)
                
        n_ssc = len(set([uf.find(x) for x in range(n)]))
        
        return n_ssc - 1