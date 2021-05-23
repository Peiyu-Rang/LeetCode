# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:56:05 2021

@author: Caven
"""


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        GATE = 0
        WALL = -1
        EMPTY = 2147483647
        DIRECTION = [[1,0], [-1,0], [0, 1], [0, -1]]
        
        m = len(rooms)
        n = len(rooms[0])
        
        queue = []

        for r in range(m):
            for c in range(n):
                if rooms[r][c] == GATE:
                    queue.append((r,c))
        
        while queue:
            curr = queue.pop(0)
            r, c = curr
            
            for d in DIRECTION:
                new_r = r + d[0]
                new_c = c + d[1]
                
                if new_r < 0 or new_c < 0 or new_r >=m or new_c >=n or rooms[new_r][new_c] != EMPTY:
                    continue
                rooms[new_r][new_c] = rooms[r][c] + 1
                
                queue.append((new_r, new_c))