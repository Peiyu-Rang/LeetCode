# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:08:47 2021

@author: Caven
"""


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        
        graph = [set(i) for i in graph]
        rgraph = [set() for i in range(n)]
        q = collections.deque([])
        
        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)
                
        while q:
            j = q.popleft()
            
            safe[j] = True
            
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)
                    
        return [i for i,v in enumerate(safe) if v]