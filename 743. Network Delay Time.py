# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:14:22 2021

@author: Caven
"""

# Heap
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
            
        hq = [(0, k)]
        
        dist = {}
        
        while hq:
            d, curr = heapq.heappop(hq)
            
            if curr in dist:
                continue
                
            dist[curr] = d
            
            for nei, time in graph[curr]:
                if nei not in dist:
                    heapq.heappush(hq, (time + d, nei))
        
        return max(dist.values()) if len(dist) == n else -1
    
    
# Dijkstra's Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for u,v,w in times:
            graph[u].append((v, w))
            
        
        distances = {node: float('inf') for node in range(1, n + 1)}
        
        visited = [False] * (n + 1)
        
        distances[k] = 0
        
        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, n+ 1):
                if not visited[i] and distances[i] < cand_dist:
                    cand_dist = distances[i]
                    cand_node = i
                    
            if cand_node < 0: break
            
            visited[cand_node] = True
            
            for nei, time in graph[cand_node]:
                distances[nei] = min(distances[nei], time + distances[cand_node])
        
        res = max(distances.values()) 
        return res if res < float('inf') else -1