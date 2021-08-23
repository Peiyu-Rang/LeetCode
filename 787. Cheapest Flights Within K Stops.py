# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:22:31 2021

@author: Caven
"""

# Approach 1: Dijkstra's Algorithm


import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_mat = [[0 for i in range(n)] for j in range(n)]
        for s,d,w in flights:
            adj_mat[s][d] = w
        
        distances = [float('inf') for i in range(n)]
        curr_stops = [float('inf') for i in range(n)]
        distances[src] = 0
        curr_stops[src] = 0
        
        minHeap = [(0,0,src)]
        
        while minHeap:
            cost, stops, node = heapq.heappop(minHeap)
            
            if node == dst:
                return cost
            
            if stops == k + 1:
                continue
                
            for nei in range(n):
                if adj_mat[node][nei] > 0:
                    dU, dV, wUV = cost, distances[nei], adj_mat[node][nei]
                    
                    if dU + wUV < dV:
                        distances[nei] = dU + wUV
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                    elif stops < curr_stops[nei]:
                        heapq.heappush(minHeap, (dU + wUV, stops + 1, nei))
                        
                    curr_stops[nei] = stops
            
        return -1 if distances[dst] == float('inf') else distances[dst]
    
    
# DFS
class Solution:
    def __init__(self):
        self.adj_mat = None
        self.memo = {}
        
    def findShortest(self, node, stops, dst, n):
        if node == dst:
            return 0
        
        if stops < 0:
            return float('inf')
        
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        res = float('inf')
        
        for nei in range(n):
            if self.adj_mat[node][nei] > 0:
                res = min(res, self.findShortest(nei, stops-1, dst, n) + self.adj_mat[node][nei])
                
        self.memo[(node,stops)] = res
        return res
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.adj_mat = [[0 for i in range(n)] for j in range(n)]
        self.memo = {}
        
        for s,d,w in flights:
            self.adj_mat[s][d] = w
            
        res = self.findShortest(src, k, dst, n)
        
        return -1 if res == float('inf') else res
    
    
#Bell Ford
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        p = [float('inf') for i in range(n)]
        c = [float('inf') for i in range(n)]
        
        graph = collections.defaultdict(list)
        
        for s,d,w in flights:
            graph[s].append((d,w))
            
        
        for at_most_edges in range(k+2):
            if at_most_edges == 0:
                p[src] = 0
                c[src] = 0
                continue
            
            for node in range(n):
                for dest, w in graph[node]:
                    c[dest] = min(c[dest], p[node] + w)
            
            p = c[:]
        
        
        return c[dst] if c[dst] < float('inf') else -1
                        
        