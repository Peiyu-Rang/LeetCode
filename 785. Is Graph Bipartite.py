# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:29:55 2021

@author: Caven
"""


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                stack = [i]
                
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = 0 if color[node] else 1
                        elif color[nei] == color[node]:
                            return False
                        
        return True
                