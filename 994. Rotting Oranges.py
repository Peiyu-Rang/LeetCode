# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:11:35 2021

@author: Caven
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
        
        q = deque([])
        num_orange = 0
        ini_rotten_orange = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                    ini_rotten_orange +=1
                if grid[i][j]:
                    num_orange +=1
        
        if ini_rotten_orange == num_orange:
            return 0
        
        if ini_rotten_orange == 0:
            return -1
        
        while q:
            x,y,time  = q.popleft()
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                
                if 0 <= new_x <m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    ini_rotten_orange +=1
                    if ini_rotten_orange == num_orange:
                        return time + 1
                    else:
                        q.append((new_x, new_y, time + 1))
                        
        return -1