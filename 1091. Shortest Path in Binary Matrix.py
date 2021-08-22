# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:29:11 2021

@author: Caven
"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        directions = [(0,-1), (0,1), (-1,0), (1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        n = len(grid)
        q = deque([(0,0,1)])
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        grid[0][0] = 1
        
        while q:
            curr = q.popleft()
            if curr[0] == n-1 and curr[1] == n-1:
                return curr[2]
            
            for move in directions:
                new_curr = (curr[0] + move[0], curr[1]+ move[1], curr[2] + 1)
                if 0 <= new_curr[0] < n and 0 <= new_curr[1] < n and grid[new_curr[0]][new_curr[1]] == 0:
                    q.append(new_curr)
                    grid[new_curr[0]][new_curr[1]] = 1
        return -1                
                