# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 23:35:58 2021

@author: Caven
"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        for (a, b), v in zip(equations, values):
            if a in graph:
                graph[a].append((b, v))
            else:
                graph[a] = [(b, v)]
                
            if b in graph:
                graph[b].append((a, 1 / v))
            else:
                graph[b] = [(a, 1 / v)]
        
        
        def findPath(query):
            a, b = query
            stack = [(a, 1)]
            visited = set()
            
            if a not in graph or b not in graph:
                return -1
            
            while stack:
                curr, temp_res = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    
                    for _next, v in graph[curr]:
                        if _next == b:
                            return temp_res * v
                        else:
                            if _next not in visited:
                                stack.append((_next, temp_res * v))
                                
            return -1
        
        res = [findPath(q) for q in queries]
        
        return res
            