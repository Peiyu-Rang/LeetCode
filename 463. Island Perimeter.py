# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:55:30 2020

@author: Caven
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        nrow = len(grid)
        ncol = len(grid[0])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    ans += 4
                
                    if i > 0 and grid[i-1][j] == 1:
                        ans -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        ans -= 2
        
        return ans