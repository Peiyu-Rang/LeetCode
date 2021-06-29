class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        if not grid:
            return 0
        
        
        m = len(grid)
        n = len(grid[0])
        def dfs(grid, r,c):
            if (r < 0 or c < 0 or r >= m or c >=n or grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c -1)
            dfs(grid, r, c + 1)
        
        n_island = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    n_island +=1
                    dfs(grid, r, c)
                    
        return n_island
    