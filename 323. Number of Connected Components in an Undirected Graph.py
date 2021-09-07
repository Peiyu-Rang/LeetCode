# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:02:11 2021

@author: Caven
"""


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        q = deque()
        res = 0
        
        for node in range(n):
            if not q and node not in visited:
                res +=1
                q.append(node)
                visited.add(node)
            
            while q:
                curr = q.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                        
        return res
                    
                