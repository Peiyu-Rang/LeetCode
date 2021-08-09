# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 22:26:25 2021

@author: Caven
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        distances = [[[0,0] for _ in range(col)] for _ in range(row)]
        
        houses = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    houses.append(((i,j),0))
        
        num_buildings = len(houses)
                            
        while houses:
            loc, d = houses.popleft()
            
            visited = set()
            q = deque()
            q.append((loc, d))
            
            while q:
                loc, d = q.popleft()
                r,c = loc
                for delta in directions:
                    new_r, new_c = r + delta[0], c + delta[1]
                    
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in visited and grid[new_r][new_c] == 0:
                        visited.add((new_r, new_c))
                        distances[new_r][new_c][0] += d +1
                        distances[new_r][new_c][1] += 1
                        q.append(((new_r, new_c), d +1))
                        
        min_dist = float('inf')
        
        for i in range(row):
            for j in range(col):
                if distances[i][j][1] == num_buildings:
                    min_dist = min(min_dist, distances[i][j][0])
                    
        return -1 if min_dist == float('inf') else min_dist
                    
                