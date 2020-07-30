# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:28:10 2020

@author: Caven
"""
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r,c):
            nr = len(grid)
            nc = len(grid[0])
            if (r < 0 or r>=nr or c<0 or c >= nc or grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'
            dfs(grid,r-1,c)
            dfs(grid,r+1,c)
            dfs(grid,r,c+1)
            dfs(grid,r,c-1)
        
        
        nRow = len(grid)
        if nRow == 0:
            return 0
        nCol = len(grid[0])
        if nCol == 0:
            return 0
        
        numIs = 0
        for r in range(nRow):
            for c in range(nCol):
                if grid[r][c] == '1':
                    numIs += 1
                    dfs(grid, r,c)
        
        return numIs

if __name__ == '__main__':
    grid = [["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]]
    
    sol = Solution()
    res = sol.numIslands(grid)
    
    print(res)