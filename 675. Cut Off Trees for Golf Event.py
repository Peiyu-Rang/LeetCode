# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:57:25 2021

@author: Caven
"""


class Solution:
    def shortestPath(self,i,j,row,col,forest, directions, m, n):
        steps = 0
        if i == row and j == col:
            return 0
        q = deque([(i,j)])
        visited = set()
        while q:
            cur_i, cur_j = q.popleft()
            
            if (cur_i, cur_j) not in visited:
                visited.add((cur_i, cur_j))
                
            steps += 1
            neighbors = [(cur_i + d[0], cur_j+d[1]) for d in directions]
            for new_i, new_j in neighbors:
                if (new_i, new_j) in visited:
                    continue
                if 0 <= new_i < m and 0 <= new_j < n and forest[new_i][new_j] > 0:
                    if row == new_i and col == new_j:
                        return steps
                    else:
                        q.append((new_i, new_j))
        return -1
    
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest[0][0]:
            return -1
        hq = []
        m = len(forest)
        n = len(forest[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        
        res = 0
        
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 0:
                    heapq.heappush(hq, (forest[i][j], i, j))
        i = 0
        j = 0
        while hq:
            node, row, col = heapq.heappop(hq)
            steps = self.shortestPath(i,j, row, col, forest, directions, m, n)
            if steps == -1:
                return -1
            
            res += steps
            forest[row][col] = 1
            i = row
            j = col
            
        return res
        