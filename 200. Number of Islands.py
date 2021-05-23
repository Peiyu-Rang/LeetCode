class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        DIRECTION = [[1,0], [-1,0],[0,1],[0,-1]]
        
        
        n_island = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    n_island +=1
                    grid[r][c] = '0'
                    
                    q = []
                    q.append((r,c))
                    
                    while q:
                        curr = q.pop(0)
                        row, col = curr
                        
                        for d in DIRECTION:
                            new_row = row + d[0]
                            new_col = col + d[1]
                            
                            if new_row >= 0 and new_col >= 0 and new_row <m and new_col < n and grid[new_row][new_col] == '1':
                                q.append((new_row, new_col))
                                grid[new_row][new_col] = '0'
                            else:
                                continue
                    
                    
        
        return n_island
        