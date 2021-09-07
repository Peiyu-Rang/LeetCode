# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:32:40 2021

@author: Caven
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        height = []
        for i in range(len(horizontalCuts)):
            if i == 0:
                height.append(horizontalCuts[i])
                continue
            height.append(horizontalCuts[i] - horizontalCuts[i-1])
        height.append(h-horizontalCuts[-1])
        
        verticalCuts.sort()
        width = []
        for i in range(len(verticalCuts)):
            if i == 0:
                width.append(verticalCuts[i])
                continue
            width.append(verticalCuts[i] - verticalCuts[i-1])
        width.append(w-verticalCuts[-1])
            
            
        return (max(height) * max(width)) % (10**9 + 7)