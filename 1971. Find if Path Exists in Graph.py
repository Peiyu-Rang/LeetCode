# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:02:03 2021

@author: Caven
"""


from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node == end:
                return True
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)
                    
        return False