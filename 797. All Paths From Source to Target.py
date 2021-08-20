# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:13:14 2021

@author: Caven
"""


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        stack = [[0]]
        visited = set()
        res = []
        
        while stack:
            curr = stack.pop()
            
            if curr[-1] == n-1:
                res.append(curr)
                continue
            elif len(curr) > n:
                continue
                     
            for nei in graph[curr[-1]]:
                stack.append(curr + [nei])
                
        return res