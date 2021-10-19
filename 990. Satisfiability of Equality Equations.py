# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:47:52 2021

@author: Caven
"""


class Solution:
    def equationsPossible(self, equations):
        p = {a:a for a in 'abcdefghijklmnopqrstuvwxyz'}
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
                
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
        
        for a, e, _, b in equations:
            if e == "=":
                union(a,b)
        
        res = not any([e == "!" and find(a) == find(b) for a, e, _, b in equations])
        
        return res