# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 21:37:40 2021

@author: Caven
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        d= 0
        x,y = 0,0
        x0, y0 = 0, 0
        for _ in range(4):
            for i in instructions:
                if i == 'G':
                    x += directions[d][0]
                    y += directions[d][1]
                elif i == 'L':
                    d = (d -1) % 4
                elif i == 'R':
                    d = (d + 1) % 4
        
            if x0 != x or y0 != y:
                continue
            else:
                return True
        return False
            