# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:40:48 2021

@author: Caven
"""


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = []
        par = [i for i in range(n)]
        mst = [[] for _ in range(n)]
        if n < 2:
            return 0
        
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances.append((i,j,dist))
                
        distances = sorted(distances, key = lambda x: x[2])
        
        dist_list = []
        for start, end, dist in distances:
            if self.unioncycle(start, end, par):
                dist_list.append(dist)
            
            if len(dist_list) == n-1:
                return sum(dist_list)
            
        
            
    def find(self,x, par):
        if par[x] == x:
            return x
        temp = self.find(par[x], par)
        par[x] = temp
        return temp
    
    def unioncycle(self, a, b, par):
        x = self.find(a, par)
        y = self.find(b, par)
        
        if x != y:
            par[x] = y
            return True
        return False
        
    
    
# Prims
        
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mappings = {}
        for i,v in enumerate(points):
            mappings[tuple(v)] = i
            
        n = len(points)
        
        visited = [False] * n
        distances = [float('inf')] * n
        distances[0] = 0
        
        min_dist = [(0, points[0])]
        
        while min_dist:
            _, curr = heapq.heappop(min_dist)
            if visited[mappings[tuple(curr)]]:
                continue
                
            visited[mappings[tuple(curr)]] = True
            
            for nei in points:
                if (not visited[mappings[tuple(nei)]]) and distances[mappings[tuple(nei)]] > (abs(nei[0] - curr[0]) + abs(nei[1] - curr[1])):
                    distances[mappings[tuple(nei)]] = abs(nei[0] - curr[0]) + abs(nei[1] - curr[1])
                    heapq.heappush(min_dist, (distances[mappings[tuple(nei)]], nei))
                    
        
        return sum(distances)
        