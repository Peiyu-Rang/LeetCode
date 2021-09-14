# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 23:05:30 2021

@author: Caven
"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        island_map = {} # coordinates -> island id
        seen = set() # seen coordinates
        island_id = 0
        stack = []
        
        # use DFS to assign each unit to an island_id
        for i in range(N):
            for j in range(N):
                if (i,j) not in seen and grid[i][j] == 1:
                    seen.add((i,j))
                    island_map[(i,j)] = island_id
                    stack.append((i,j))
                    
                    while stack:
                        x, y = stack.pop()
                        for nei_x, nei_y in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                            if 0 <= nei_x < N and 0 <= nei_y < N:
                                if (nei_x, nei_y) not in seen and grid[nei_x][nei_y] == 1:
                                    seen.add((nei_x, nei_y))
                                    island_map[(nei_x, nei_y)] = island_id
                                    stack.append((nei_x, nei_y))
                                    
                    island_id +=1
                    
        # get the area of each island_id
        island_area = collections.Counter(island_map.values())
        
        # for each sea, curr_area is the sum of the neighbor islands areas
        max_area = -float('inf')
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    curr_area = 0
                    included_island = set()
                    for nei_x, nei_y in ((i-1, j), (i+1, j), (i,j-1), (i,j+1)):
                        if (nei_x, nei_y) in island_map and island_map[(nei_x, nei_y)] not in included_island:
                            curr_area += island_area[island_map[(nei_x, nei_y)]]
                            included_island.add(island_map[(nei_x, nei_y)])
                    max_area = max(max_area, curr_area + 1)
        
        
        # if no sea, return N*N
        return max_area if max_area > -float('inf') else N*N
                  