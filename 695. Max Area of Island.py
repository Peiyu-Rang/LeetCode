# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:08:33 2021

@author: Caven
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                
                area = 1
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    if (r,c) not in visited:
                        visited.add((r,c))
                    for x, y in [[r+1, c], [r-1,c], [r, c+1], [r, c-1]]:
                        if x < 0 or y < 0 or x >= m or y >=n or grid[x][y] == 0:
                            continue
                        
                        if (x,y) not in visited:
                            visited.add((x,y))
                            area +=1
                            q.append((x,y))
                            
                max_area = max(area, max_area)
                
        return max_area
                    
                
                