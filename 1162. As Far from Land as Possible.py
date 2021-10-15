# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:36:21 2021

@author: Caven
"""


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    
        q = deque(q)
        
        if len(q) == m*n or len(q) == 0: return -1
        dist = 0
        
        while q:
            size_q = len(q)
            
            for _ in range(size_q):
                r, c = q.popleft()
                
                for x, y in [[r+1, c], [r-1,c],[r, c+1], [r, c-1]]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        q.append((x,y))
                        grid[x][y] = 1
                        
            dist +=1
            
        return dist -1
                        
                    