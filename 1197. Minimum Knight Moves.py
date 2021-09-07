# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:20:50 2021

@author: Caven
"""


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x < 0:
            x = -x
        if y < 0:
            y = -y

        moves = [(1, 2), (2, 1), (2, -1), (1, -2),
                   (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
        visited = set()
        q = deque([(0,0,0)])
        while q:
            cx, cy, step = q.popleft()
            if cx == x and cy == y:
                return step
            
            for dx, dy in moves:
                nx = cx + dx
                ny = cy + dy
                
                if (nx, ny) not in visited:
                    q.append((nx, ny, step + 1))
                    visited.add((nx, ny))
                    
        
            