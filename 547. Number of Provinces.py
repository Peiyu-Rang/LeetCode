# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:18:37 2021

@author: Caven
"""


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        res = 0
        n = len(isConnected)
        for i in range(n):
            if i not in visited:
                self.dfs(isConnected, visited, i)
                res +=1
        
        return res
    
    def dfs(self, isConnected, visited, i):
        n = len(isConnected)
        for j in range(n):
            if isConnected[i][j] and j not in visited:
                visited.add(j)
                self.dfs(isConnected, visited, j)
                



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0
        q = deque([])
        
        for i in range(n):
            if i not in visited:
                q.append(i)
                while q:
                    node = q.popleft()
                    visited.add(node)
                    for j in range(i+1, n):
                        if isConnected[node][j] and j not in visited:
                            q.append(j)
                            visited.add(j)
                res +=1
        return res